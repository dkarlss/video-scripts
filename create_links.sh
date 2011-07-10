#!/bin/bash
find "$1" -name "*.mp4" -type f -exec ln -s {} \;
find . -name "*.mp4" | sort -h > filelist.txt
python /home/username/bin/buildpage.py filelist.txt