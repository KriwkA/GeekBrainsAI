#!/bin/bash
function pause() {
read -p "Press enter to continue..."
}

# task 2
echo "Creating task2_dir directory for second task files"
pause
mkdir task2_dir

echo "Enter the file1.txt's text:"
cat > task2_dir/file1.txt

echo "Enter the file2.txt's text:"
cat > task2_dir/file2.txt

echo "Concatenate task2_dir/file1.txt task2_dir/file2.txt to ask2_dir/file3.txt"
pause
cat task2_dir/file1.txt task2_dir/file2.txt > task2_dir/file3.txt

echo "Renaming task2_dir/file3.txt to task2_dir/file3_renamed.txt"
pause
mv task2_dir/file3.txt task2_dir/file3_renamed.txt

# task 3
echo "Creating task3_dir directory for third task files"
pause
mkdir task3_dir

echo "Creating files: task3_dir/task3_file{1..5}.txt"
pause
touch task3_dir/task3_file{1..5}.txt

echo "Creating task3_dir/temp directory."
pause
mkdir task3_dir/temp

echo "Moving task3_dir/task3_file1.txt to task3_dir/temp/task3_file1.txt"
pause
mv task3_dir/task3_file1.txt task3_dir/temp/task3_file1.txt

echo "All created files at second and third tasks will be removed"
pause
mv task3_dir task2_dir/task_3dir
rm -rf task2_dir

#task 4
echo "Count of hiden files in '/home' is:"
ls -a /home | grep ^'\.' | wc -l

#task 5
echo "Printing all files from /etc:"
pause
for file in "/etc"/*
do
    cat $file 2> errors.txt
done

echo "Count of read file error is:"
cat errors.txt | wc -l
