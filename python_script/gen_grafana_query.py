from jinja2 import Environment, PackageLoader
from globals_define import *

f = open('grafana_query.j2', 'r')
string = f.read()
env = Environment()
template = env.from_string(string)

column_name_list = []
for table in TABLE_LIST:
    column_name_list += list(table.items())

content = template.render(tname_list = column_name_list)

with open('grafana_query.txt', 'w+') as f:
    f.write(content)
