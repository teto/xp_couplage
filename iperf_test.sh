#!/bin/bash

if [ $# -lt 3 ]; then
	echo "Use: <server> <localIp> <nb of iterations>"
	echo server likely to be 79.141.8.227 or 153.16.49.122
	exit 1
fi

SERVER="$1"
bindTo="$2"
NBOFFILES=$3

# repeat iperf for each size MAX_REPEAT times
MAX_REPEAT=3 # $2
delta=128
#iter_size=0

#source config.sh


#SERVER="153.16.49.122"
#LOG="client-iperf.log"
#TIME="5

logfilename=$(printf "iperf_%s.log" `date +"%Hh%M"`)
echo "--> Saving test into $logfilename" 


rm -f $logfilename


iter_size=$NBOFFILES

export RESULT=0;
 
until [ $iter_size -le 0 ]; do
	
	line=""
	iter_attempt=$MAX_REPEAT		
	results="0"
	toTransfer=$(($iter_size*$delta))
	until [ $iter_attempt -le 0 ]; do
		#result=$( ./iperf_unit_test.sh $SERVER "$(($iter_size*$delta))" )
		result=`./iperf_unit_test.sh $SERVER $bindTo "$toTransfer"`
		if [ $? -ne 0 ]; then
			echo Erreur dans le programme
			exit 1
		fi

		echo "Result $iter_size.$iter_attempt: $result (s)"

		results=" $results + $result"
		echo "REsults: $results"
		iter_attempt=$((iter_attempt-1))

	done
	#echo "results 	
	echo "$toTransfer $(echo $results|bc)" >> $logfilename
	iter_size=$((iter_size-1))
done

echo "--> Results saved in $logfilename"

if [ ! -z $2 ]; then

	./generate_graph.sh $logfilename
fi
