#!/bin/bash
folder="$HOME/xpfiles"
initialSize=1
blockSize=128
nbOfTimes=4


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
