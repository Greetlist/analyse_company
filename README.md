[TOC]

# 目的
从网易财经上面拉取上市公司的财报数据：现金流量表，资产负债表，利润表,并把这些数据存入数据库，最后在Grafana里面展示出来

# 如何使用
## 数据准备

1. 运行Golang脚本拉取csv文件
2. 运行filter_empty_record.py 脚本去掉空的csv文件
3. 运行shell_script/erase_blank.sh 脚本去掉现金流量表中每行首的空格
4. 运行python_script/gen_all_table.py 生成所有感兴趣的报表ORM类，具体的列可以在python_script/globals_define.py文件里面找到
5. 运行python_script/dump_csv_to_mysql.py 把所有的数据dump到数据库里面

## 环境安装
会准备一个shell脚本，主要是Golang，Python，Grafana，Mysql的安装

# 配置相关
python_script/config/config.yaml 为配置文件，现在只有mysql的配置，后面可以再添加其他的配置，这里只是说明配置文件的路径和文件名
模板如下:
```
mysql:
  host: localhost
  port: 3306
  user: your_account
  passwd: your_password
  database: your_database_name
```
