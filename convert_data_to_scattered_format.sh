#!/bin/bash

# gnuplot scattered waits for 4 columns:
# X/Y value/Y lowest value/Y Max Value
# in our case Y value should be min

# accept a list of files 

if [ $# -ne 1 ]; then
	echo "Use $0 <nameOfTheFolderWithDAtaFiles> "
	exit 1
fi

# <=> name of the xp
OUTPUT_FOLDER="$1"
if [ ! -d "$OUTPUT_FOLDER" ]; then
	echo "sorry but folder '$OUTPUT_FOLDER' does not exist"
	exit 1
fi

OUTPUT_FILE="$OUTPUT_FOLDER/scattered.matrix"
TEMP_FILE="$OUTPUT_FILE.tmp"


# in case they already exist, empty files
> "$OUTPUT_FILE"
> "$TEMP_FILE"



temp="$TEMP_FILE"


no=0
# does not give absolute paths
# for i in $( ls "$OUTPUT_FOLDER" ); do
#  find '/home/teto/xp_couplage/monxp' -name \*.data -type f -print

file_list=$( find "$OUTPUT_FOLDER" -name \*.data -type f -print );

echo "================================="
echo "Mergind data from datafiles:"
for file in $file_list; do
	echo "$file"
done 
echo "================================="

for i in $( find "$OUTPUT_FOLDER" -name \*.data -type f -print ); do


	# triggers only on first iteration
	# register the file in case it is the only file
	if [ $no -eq 0 ]; then
		cat "$i" > "$TEMP_FILE"
		no=42
	else 
		join "$i" "$temp" > "$TEMP_FILE"
	fi

	# shift 1
	temp="$i"
done 



# then for each entry we compute the average, min, max and create matrix accordingly
while read size values; do
	#echo "Size : $size"
	#echo "Values : $values"
# END {printf "Min: %f\tMax: %f\tAverage: %f\n", min, max, sum/NR}'

	# compute in order, average, min, max
	res=$( echo "$values"| 
	  awk '{ min=$1; max=$1; tot=0; for (i=1; i<=NF; i++){ if($i > max) max=$i; if($i < min) min=$i; tot += $i;}  print tot/NF,min,max; }'
	  )
	echo "Size: '$size' Avg/Min/Max: $res" 
	echo "$size $res" >> "$OUTPUT_FILE"
done < "$TEMP_FILE"


echo "===> voulez vous générer et voir le graphe (y) ?"
read answer

if [ $answer == "y" ]; then

	plotFilename="$OUTPUT_FOLDER/output.png"
	gnuplot -e "datafile='$OUTPUT_FILE';titre='$OUTPUT_FOLDER';graphe='$plotFilename'" trace_plot.plot

	echo "eog $plotFilename"
	eog "$plotFilename"&
fi