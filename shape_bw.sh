#!/bin/bash
if [ $# -lt 1 ]; then
	echo "Use $0 [ clean | install] , if install add upload rate "
	exit 1
fi

DL_RATE=4000
UL_RATE=$2
IF_LIST="eth0 eth1"


function clean()
{
	for if_name in $IF_LIST; do
		wondershaper clear $if_name
	done;
}

function install()
{
for if_name in $IF_LIST; do
	echo "Setting up rate of $UL_RATE for $if_name"
	wondershaper $if_name $DL_RATE $UL_RATE
done
}

case $1 in 
	"clean") clean 
		;;
	"install") if [ -z "$2" ]; then
			echo "give upload rate"
			exit 1
		fi
		clean
		install
		;;
esac
