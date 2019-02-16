#!/bin/bash

ls -a -l -I '..' -I '.' /dev |
    grep -v '^\(total\)' | 
    cut -c 1-10 | 
    sort | uniq | wc -l
