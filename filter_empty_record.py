import pandas as pd
import os
import time

location_dict = {}

location_dict['xjllb']= '/home/greetlist/extract_company_data/xjllb_csvs'
location_dict['lrb']= '/home/greetlist/extract_company_data/lrb_csvs'
location_dict['zcfzb']= '/home/greetlist/extract_company_data/zcfzb_csvs'

empty_list_dict = {}
empty_list_dict['xjllb'] = []
empty_list_dict['lrb'] = []
empty_list_dict['zcfzb'] = []

start = time.time()
# 遍历所有csv文件，找出不含任何数据的csv
for name, location in location_dict.items():
    for f in os.listdir(location):
        file_location = os.path.join(location, f)
        cur_df = pd.read_csv(file_location, encoding='gbk')
        if len(cur_df) <= 1:
            empty_list_dict[name].append(f.split('_')[1])
print('iter total csv files cost : {}'.format(time.time() - start))

'''
查找出空表的公司代码，可能包含x表张空，3-x张表有的情况 x E [1, 2]
对于这种情况，可能需要把对应公司的表删掉
'''
total_dict = {}
for name, elist in empty_list_dict.items():
    for item in elist:
        if total_dict.get(item, None) == None:
            total_dict[item] = 1
        else:
            total_dict[item] += 1

all_empty_company_code_list = []
part_empth_company_code_list = []

for name, count in total_dict.items():
    if count != 3:
        part_empth_company_code_list.append(name)
    else:
        all_empty_company_code_list.append(name)

'''
删掉所有空或者部分空的公司数据
'''
for file_name, _ in total_dict.items():
    for name, location in location_dict.items():
        #os.remove(os.path.join(location, name + '_' + file_name))
        print(os.path.join(location, name + '_' + file_name))

