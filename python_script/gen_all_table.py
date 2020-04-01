from jinja2 import Environment, PackageLoader
from globals_define import *

f = open('db_define.j2', 'r')
string = f.read()
env = Environment()
template = env.from_string(string)

column_name_list = []
for table in TABLE_LIST:
    for _, column_name in table.items():
        column_name_list.append(column_name)

content = template.render(tname_list = column_name_list)

with open('db_relative.py', 'w+') as f:
    f.write(content)
