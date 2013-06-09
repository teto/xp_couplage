#!/bin/bash

if [ $# -lt 3 ]; then
	echo "Use: <baseUrl> <nb of files> <nameOfTheTest>"
	echo baseurl likely to be 79.141.8.227 or http://153.16.49.120:8000/xpfiles
	exit 1
fi

#<>
BASE_URL="$1"
NAME_OF_THE_TEST="$3"
NBOFFILES=$2
OUTPUT_FOLDER="$HOME/xp_couplage/$NAME_OF_THE_TEST"
# ="$NAME_OF_THE_TEST.data"
blockSize=128
blockSize=256

if [ ! -d "$OUTPUT_FOLDER" ]; then
	echo "Trying to create folder $OUTPUT_FOLDER "
	mkdir $OUTPUT_FOLDER

fi


# look for appropriate filename
no=0
until [ ! -f "$OUTPUT_FOLDER/$no.data" ];do

	no=$(( no + 1))
done

OUTPUT_FILE="$OUTPUT_FOLDER/$no.data"
echo "Output file $filename "

echo -e "=================================="
echo -e " Launching test '$NAME_OF_THE_TEST'"
echo -e "=================================="
#generate_list_of_urls_to_download_from list_urls

#echo "saved list $list_urls"


# for url in $list_urls; do
for no in $( seq 1 $NBOFFILES);do

	TIME_PROGRAM=$(which time);
	size=$(( no * blockSize))

	$TIME_PROGRAM --append -o "$OUTPUT_FILE" -f "$size %e" wget -q -O - "$BASE_URL/$size.bin" > /dev/null
	
	if [ $? -ne 0 ];then
		echo "An error happened "
		exit
	else
		echo "step $no successful"
	fi

done

# change rights
chown -R teto:teto "$OUTPUT_FOLDER"


cat "$OUTPUT_FILE"
