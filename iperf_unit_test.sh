#!/bin/bash
if [ $# -ne 3 ]; then
#	echo "Usage: <serverIP> <perf filename> <log filename>"
	echo "Usage: <serverIP> <bindTo> <number of Kbytes>" 
	exit 1
fi

SERVER=$1
bindTo=$2
toTransfer=$3

#echo "-- Unit test start with server $SERVER,transfering $toTransfer KBytes" # filename $filename" 


# -k [kmKM] bits/bytes
#line=$(iperf -c $SERVER -f K -F $filename  -t 30 -y C)
# be really careful !! -n => number of bytes be sure to set K or M otherwise sends 
# -B ${bindTo} 
line=$(iperf -c $SERVER -n${toTransfer}KB -y C)




#read date senderip senderport receiverip receiverport id interval transfered bandwidth 
#line=$(echo "$line" | cut -d, -f7 )
#read interval <<< $line

#keep only second field
interval=$(echo "$line" | cut -d, -f7 |cut -d- -f2)
#interval=$(echo $interval|cut -d- -f2)
echo $interval

# convert into bytes

#echo "$toTransfer $interval" >> $LOG
#echo "$line" >> $LOG


 
#echo "-- Unit test end)" # | tee -a $LOG
