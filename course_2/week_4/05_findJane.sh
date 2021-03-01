#!/bin/bash

> oldFiles.txt
user=$(whoami)
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)

for item in $files; do
    if test -e /home/$user$item; then
        echo "/home/$user$item" >> oldFiles.txt
    fi
done
