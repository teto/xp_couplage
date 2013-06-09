#!/bin/bash

XP_NAME=""
BASE_URL="http://153.16.49.120:8000/xpfiles"
TIMES_TO_REPEAT_EACH_XP=3
MAX_NUMBER_OF_BLOCKS=30

source "$LIB_BASH/lib_generic.sh"
source "$LIB_BASH/lib_mptcp.sh"


# for i in {1..30}; do 
# 	./wget_test.sh monxp  50
# done

function display_main_list()
{
echo "=================================="
echo "Current Params"
echo "Times to repeat each xp: '$TIMES_TO_REPEAT_EACH_XP' "
echo "MAx number of blocks: '$MAX_NUMBER_OF_BLOCKS' "
echo "Base url: $BASE_URL"
echo "=================================="
echo "What do you want to do ?"
echo "a) set number of times to repeat each xp"
echo "z) set max number of blocks of the file to downloads"
echo "e) set base url ('$BASE_URL')"
echo "1) generate results for TCP"
echo "2) generate results for MPTCP"
echo "3) generate results for my XP"
echo "q) quit"
}


# @param xp_name
# @param command to launch
function launch_xp()
{
	local xp_name=""
	local cmdToExecute="$1"

	echo "Please enter the test name:"
	read xp_name
	echo "Launching test '$xp_name'"
	cmdToExecute="$cmdToExecute $xp_name"
	for i in $(seq 1 $TIMES_TO_REPEAT_EACH_XP); do 
		# ./wget_test.sh $BASE_URL mptcp  $MAX_NUMBER_OF_BLOCKS
		# eval "$cmdToExecute $xp_name"
		gen_launch_command "$cmdToExecute"

	done


	./convert_data_to_scattered_format.sh "$xp_name"
}



KEY="a"
while [ "$KEY" != "q" ]; do
		

	# TODO 
	if [ ! -z "$( ps -ea | grep lig_daemon)" ]; then
		echo "Killing lig_daemon still running"
		$(sudo killall -r lig_daemon*)
	fi

	display_main_list

	read KEY




	case "$KEY" in
		[aA]) echo "Enter number of times to repeat each XP"
			gen_enter_bounded_number 1 40 TIMES_TO_REPEAT_EACH_XP

			;;
		[zZ]) echo "Enter number of times to repeat each XP"
			gen_enter_bounded_number 1 100 MAX_NUMBER_OF_BLOCKS

			;;		

		[eE]) echo "Enter base url ('$BASE_URL') "
			echo "For instance http://79.141.8.227:8000/xpfiles"
			echo "or http://153.16.49.120:8000/xpfiles"
			result=1;
			while [ $result -ne 0 ]; do

				read url
				wget  --timeout 3 -O -  $url > /dev/null
				result="$?"
				#if [ $? -eq 0 ]
			# timeout in sec
			done

			BASE_URL="$url"

			;;

		1) echo "Generate results for TCP\nDisabling mptcp..."
			mptcp_set_global_state 0

			cmd="./wget_test.sh $BASE_URL $MAX_NUMBER_OF_BLOCKS"
			launch_xp "$cmd"

			# for i in $(seq 1 $TIMES_TO_REPEAT_EACH_XP); do 
			
			# 	if [ $? -ne 0 ];then
			# 		echo "FAILURE"
			# 		exit 1
			# 	fi
			# done
			;;

		2) echo "Generate results for MPTCP\nEnabling mptcp..."
			mptcp_set_global_state 1

			echo "/!\\ MAKE SURE SERVER AND HOST ROUTING TABLES ARE OK /!\\"
			echo "Else launch the script mptcp_config.sh"

			cmd="./wget_test.sh $BASE_URL $MAX_NUMBER_OF_BLOCKS"
			launch_xp "$cmd"

			# for i in $(seq 1 $TIMES_TO_REPEAT_EACH_XP); do 
			# 	./wget_test.sh $BASE_URL mptcp  $MAX_NUMBER_OF_BLOCKS
			# done

			# ./convert_data_to_scattered_format.sh
			;;

		3) echo "Generate results with my solution\nEnabling mptcp"
			echo "Depending on the sate of the module check your mptcp configuration"
			mptcp_set_global_state 1
			
			# setup env (source ?)
			echo "Setup environment (compilation etc)..."
			sudo ./setup_lispcom.sh

			cmd="./wget_test.sh $BASE_URL  $MAX_NUMBER_OF_BLOCKS"
			launch_xp "$cmd"

			# TODO change
			# for i in $(seq 1 $TIMES_TO_REPEAT_EACH_XP); do 
				
			# 	if [ $? -ne 0 ];then
			# 		echo "FAILURE"
			# 		exit 1
			# 	fi
			# done
			;;
	esac

done;

# ./convert_data_to_scattered_format.sh $XP_NAME
