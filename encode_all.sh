#!/bin/bash
find /home/username -name "*.avi" -exec /home/username/bin/h264encode.sh "{}" \;
find /home/username -name "*.mkv" -exec /home/username/bin/h264encode.sh "{}" \;