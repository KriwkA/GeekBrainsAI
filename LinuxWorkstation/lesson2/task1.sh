#!/bin/bash

#print content of /etc /proc /home
ls /etc 
ls /proc 
ls /home


#print two random files from /etc directory
let file_cnt=0
files=()
for file in "/etc"/*
do
    if [ ! -d $file ]
    then
        files+=($file)
        let file_cnt=file_cnt+1;
    fi
done

if [ $file_cnt = 0 ]
then
   	echo "Directory has not files"
else
	if [ $file_cnt = 1 ]
	then
		echo "Directory has just one file:"
		echo ${files[0]}
    else
		echo "Directory has $file_cnt files"
        echo "Two random files of them:"
		let first=$((RANDOM % $file_cnt))
	    let second=$((RANDOM % $file_cnt))
        while [ $first = $second ]
		do
			let second=$((RANDOM % $file_cnt))
		done

		echo ${files[first]}
   		echo ${files[second]}
	fi
fi
