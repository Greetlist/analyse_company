import pandas as pd
from db_relative import *
from globals_define import *
import importlib
import os

table_defined_module = None

def read_single_csv(file_location, csv_type):
    column_list = ['报告日期'] + list(TABLE_LIST[csv_type].keys())
    #转置矩阵取所有关心的列
    data_df = pd.read_csv(file_location, encoding='gbk').set_index('报告日期').T
    data_df = data_df.reset_index().rename(columns={'index':'报告日期'})
    return data_df[column_list]

def import_total_table_defined_class():
    global table_defined_module
    table_defined_module = importlib.import_module('db_relative')

def extract_csv_data_to_orm_list(data_df, company_code, csv_type):
    orm_object_list = []
    data_len = len(data_df)
    for key, value in TABLE_LIST[csv_type].items():
        specific_class = getattr(table_defined_module, value)
        column_data_list = data_df[['报告日期', key]].to_dict('record')
        for item in column_data_list:
            if item['报告日期'] != ' ':
                real_value = 0
                if item[key] != '--' and item[key] != ' ':
                    real_value = int(item[key])
                orm_object_list.append(specific_class(inst_code=company_code, date=item['报告日期'], value=real_value))

    return orm_object_list

def do_dump_data_to_database(data_list):
    session.add_all(data_list)
    session.commit()

if __name__ == '__main__':
    load_configs()
    set_up_session()
    import_total_table_defined_class()

    for csv_type in range(CSV_TYPE_MAX):
        csv_dir_location = CSV_DIR_LOCATION[csv_type]
        for file_name in os.listdir(csv_dir_location):
            read_single_csv(os.path.join(csv_dir_location, file_name), csv_type)
            company_code = file_name.split('_')[1].split('.')[0]
            single_csv_data_list = extract_csv_data_to_orm_list(data_df, company_code, CSV_TYPE_CASH)
            do_dump_data_to_database(single_csv_data_list)
            break


