#!/bin/bash

mkdir task9_dir
cd task9_dir

let file_cnt=500
let sec_per_day=60*60*24

let day=0
let start_date=$(date -d '01/01/2019' +"%s")
while [ $day != $file_cnt ]
do
   let time_stamp=start_date+sec_per_day*day
   file_name=$(date -d @$time_stamp '+%Y-%m-%d')
   touch $file_name.txt
   echo $file_name.txt > $file_name.txt
   let day=day+1
done

cd ..
read -p "Press enter to continue..."
rm -rf task9_dir
