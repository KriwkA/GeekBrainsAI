#!/bin/bash

mkdir temp
cd temp


#task 1
echo "some text" > file1.txt
cat file1.txt > file2.txt

ln -s file2.txt file3.txt
ln    file2.txt file4.txt

stat file1.txt
stat file2.txt
stat file3.txt
stat file4.txt

rm file1.txt

cat file2.txt
cat file3.txt
cat file4.txt

#task 2

mv file2.txt file2_renamed.txt
mkdir links_dir
ln -s file2_renamed.txt file5.txt
mv file3.txt links_dir/file3.txt
mv file4.txt links_dir/file4.txt
mv file5.txt links_dir/file5.txt

#task 3

mkdir task3
cd task3

touch file1
touch file2

chmod u=rw- file1
chmod g=rw- file1
chmod o=r-- file1

chmod u=rw- file2
chmod g=--- file2
chmod o=--- file2

ls -l

chmod 664 file1
chmod 600 file2

ls -l

cd ..

#task 4

adduser -G sudo new_super_user

#task 5

groupadd developers
adduser -G developers dev1
adduser -G developers dev2
adduser -G developers dev3

mkdir dev_folder
chgrp developers dev_folder
chmod 660 dev_folder

#task 6

mkdir dev_folder2
chgrp developers dev_folder2
chmod 640 dev_folder2

#task 7

mkdir temp2
touch temp2/temp_file
chmod -x temp2

#clear
cd ..
rm -rf temp

