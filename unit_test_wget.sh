#!/bin/bash

# waits for url and file to save to
fileToDownload="$1"
appendTo="$2"
#http://153.16.49.120:8000/xpfiles/1.log
# -q = quiet, prevents wget from displaying data

TIME_PROGRAM=$(which time)
$TIME_PROGRAM --append -o "$appendTo" -f "%e" wget -q -O - "$fileToDownload" > /dev/null