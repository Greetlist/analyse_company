#!/bin/bash

sudo apt-get update
sudo apt-get install -y curl wget git gcc g++ lsof python3
cd && mkdir current && cd current
wget https://dev.mysql.com/get/mysql-apt-config_0.8.15-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.15-1_all.deb
sudo apt-get update && sudo apt-get install mysql-server
sudo service mysql stop && sudo service mysql start

wget https://dl.google.com/go/go1.4-bootstrap-20171003.tar.gz
tar -xvzf go1.4-bootstrap-20171003.tar.gz
cd go1.4/src && CGO_ENABLED=0 bash make.bash
cd && git https://github.com/golang/go.git
cd goroot && git checkout go1.14.1
cd src && ./all.bash

cd ~/current
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
sudo add-apt-repository "deb https://packages.grafana.com/enterprise/deb stable main"

sudo apt-get update
sudo apt-get install grafana-enterprise""
