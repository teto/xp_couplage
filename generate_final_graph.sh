#!/bin/bash

# todo should be run 

#generer un fichier temporaire a partir du log

if [ $# -lt 1 ]; then
	echo "Usage: Specify at least one folder name "
	exit 1
fi

# source ./config.sh

# find . -wholename "$0" -print



#filename="$1"

OUTPUT_GNUPLOT_SCRIPT="final_plot.plot"
FOLDERS="$@"

# TODO add different styles
# declare -a STYLES=("" "")


cat "initial_plot.plot" > "$OUTPUT_SCRIPT"

#output="/tmp/$(basename $filename)"

# wait for what follows 
echo "plot " >> "$OUTPUT_GNUPLOT_SCRIPT"

# for each folder
for folder in "$FOLDERS"; do 

	# we first aggregate the data from the different XPs
	./convert_data_to_scattered_format.sh "$folder"

	# TODO faire en sorte que cela soit synchro avec le script présent
	# datafile="$folder/scattered.matrix"

	# echo "'$datafile'  using 1:2 with linespoint  linewidth 3 title titre, \
	# 	'$datafile' with errorbars linewidth 2 linecolor rgb 'blue' notitle" \
	# 		 >> "$OUTPUT_GNUPLOT_SCRIPT"

done

#echo $IFS
# gnuplot trace_plot.plot


# asks user if he wants to see graph
# echo "===> voulez vous générer et voir le graphe (y) ?"
# read answer

# if [ $answer == "y" ]; then

# 	gnuplot -e "datafile=$OUTPUT_FILE;titre='ceci est le titre'" trace_plot.plot

# 	echo "eog $OUTPUT_FOLDER/output.png"
# 	eog output.png&
# fi