#!/bin/bash

file_location=/home/greetlist/extract_company_data/xjllb_csvs
file_list=$(ls $file_location)

for file in $file_list
do
    sed -i 's/^ //g' $file_location/$file
done
