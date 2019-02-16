#!/bin/bash

# task 7
lsof -u kriwka | grep ' /dev/' | less

# task 8
mkdir task8_dir
mkdir task8_dir/photos/{2015..2019}/{1..12}


