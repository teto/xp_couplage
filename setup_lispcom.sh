#!/bin/bash

debugFolder="/sys/kernel/debug/tracing"
#ppwd="$(pwd)"
moduleFolder="/home/teto/lig_module"
lispMS=""
daemonFolder="/home/teto/lig_daemon_nl/"

#export NLCB=debug
#export NLDBG=4



source "$LIB_BASH/lib_generic.sh"




# load lig_module for tests if not loaded yet
if [ `lsmod | grep -c lig_module ` -ne 0 ]; then
	sudo rmmod lig_module
fi

echo " ===> Loading module"	
sudo "$moduleFolder/compile.sh" compile load
if [ $? -ne 0 ]; then
		echo "compilation failed"
		exit 1
fi



# -r => regex
sudo killall -r 'lig_daemon*'

echo "===> Launching daemon"
# launch debug versioN
$daemonFolder/lig_daemon_d&

