#!/bin/bash



if [ $# -ne 1 ]; then
	echo "Usage: $0 <commandToLaunch>"
	echo " Might be:"
	echo "iperf -c mptcp.info.ucl.ac.be -t 20"
	echo "$HOME/xp_couplage/wget_test.sh 153.16.49.120:8000/xpfiles temp 3"

	exit 1
fi

CMD="$1"

# debugFolder="/sys/kernel/debug/tracing"
# #ppwd="$(pwd)"
# moduleFolder="/home/teto/lig_module"
# lispMS=""
# daemonFolder="/home/teto/lig_daemon_nl/"

# #export NLCB=debug
# #export NLDBG=4



# if [ $# -lt 1 ]; then
# 	echo "Usage: $0 <commandToLaunch>"
# 	echo " Might be:"
# 	echo "iperf -c mptcp.info.ucl.ac.be -t 20"
# 	echo "$HOME/xp_couplage/wget_test.sh 153.16.49.120:8000/xpfiles temp 3"

# 	exit 1
# fi

# source "$LIB_BASH/lib_generic.sh"


# CMD="$@"

# # load lig_module for tests if not loaded yet
# if [ `lsmod | grep -c lig_module ` -ne 0 ]; then
# 	sudo rmmod lig_module
# fi

# echo " ===> Loading module"	
# sudo "$moduleFolder/compile.sh" compile load
# if [ $? -ne 0 ]; then
# 		echo "compilation failed"
# 		exit 1
# fi



# # -r => regex
# sudo killall -r 'lig_daemon*'

# echo "===> Launching daemon"
# # launch debug versioN
# $daemonFolder/lig_daemon_d&

source ./setup_lispcom.sh

# sudo alone is not enough to allow us to cd to that directory
#sudo su
# cd $debugFolder

# to clear file
echo 0 > "$debugFolder/tracing_on"
echo function_graph > "$debugFolder/current_tracer"

# setup ftrace filter to record mptcp functions only
echo 'mptcp*' > "$debugFolder/set_ftrace_filter"
echo 'queue_work' >> "$debugFolder/set_ftrace_filter"
# to display calls to all functions from our module
echo ":mod:lig_module" >> "$debugFolder/set_ftrace_filter"
#echo 'mptcp_doit:traceon' >>  set_ftrace_filter



# echo "Please enter the command you want to launch :"
# echo " Might be:"
# echo "iperf -c mptcp.info.ucl.ac.be -t 20"
# echo "$HOME/xp_couplage/wget_test.sh 153.16.49.120:8000/xpfiles temp 3"

# read cmd

# enable ftrace
echo 1 > "$debugFolder/tracing_on";

gen_launch_command "su -c \"$CMD\""

# cmdpid=$!
# sleep 3
# echo "Killing "
# kill -9 $cmdpid

echo 0 > "$debugFolder/tracing_on"


echo -e "To see trace, exec:\nless $debugFolder/trace|grep -n fucking"
