#!/bin/bash
# base operating system: ubuntu 18.04

sudo apt-get update
sudo apt-get install -y curl wget git gcc g++ lsof python3
cd && mkdir -p current && cd current
wget https://dev.mysql.com/get/mysql-apt-config_0.8.15-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.15-1_all.deb
sudo apt-get update && sudo apt-get install -y mysql-server
sudo service mysql stop && sudo service mysql start

wget https://dl.google.com/go/go1.4-bootstrap-20171003.tar.gz
tar -xvzf go1.4-bootstrap-20171003.tar.gz
cd go/src && CGO_ENABLED=0 bash make.bash
cd && git clone https://github.com/golang/go.git
cd go && git checkout go1.14.1
cd src && GOROOT_BOOTSTRAP=~/current/go ./all.bash

echo "
PATH=$PATH:~/go/bin:~/clang/bin:~/.local/bin
PYTHONPATH=~/.local/lib/python3.6/site-packages
GOPATH=~/.go_path" >> ~/.bashrc
source ~/.bashrc

cd ~/current
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo add-apt-repository "deb https://packages.grafana.com/enterprise/deb stable main"

sudo apt-get update
sudo apt-get install -y grafana-enterprise
sudo service grafana-server start

# python related
sudo apt-get install -y libssl-dev python-dev libmysqlclient-dev
sudo apt-get -y install python3-pip
pip3 install numpy pandas SQLAlchemy mysqlclient -i https://mirrors.aliyun.com/pypi/simple/
