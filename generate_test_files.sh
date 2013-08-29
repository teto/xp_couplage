#!/bin/bash
#folder="$HOME/xpfiles"
#initialSize=1
#blockSize=128
#nbOfTimes=4 # nb of files to create

folder="$1"
blockSize=$2
nbOfTimes=$3

if [ $# -ne 3 ]; then
	echo "Usage: $0 <dirToPutFiles> <BlockSize> <nbOfFiles>"
	exit 1
fi

if [ ! -d "$folder" ]; then

	mkdir $folder
fi

#rm -R $folder/*


until [ $nbOfTimes -le 0 ]; do
	size=$((nbOfTimes * blockSize))

	echo Creating file with random content of size "$size"
	dd if=/dev/urandom of="$folder/$size.bin" bs="${blockSize}k" count=${nbOfTimes}
	nbOfTimes=$(( $nbOfTimes - 1 ))
done
