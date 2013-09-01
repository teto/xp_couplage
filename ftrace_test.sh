#!/bin/bash

# todo to remove

if [ $# -ne 1 ]; then
	echo "Usage: $0 <commandToLaunch>"
	echo " Might be:"
	echo "iperf -c mptcp.info.ucl.ac.be -t 5"
	echo "$HOME/xp_couplage/wget_test.sh 153.16.49.120:8000/xpfiles temp 3"
	exit 1
fi

CMD="$1"
debugFolder="/sys/kernel/debug/tracing"

# to clear file
read -r -d '' command  <<EOF
echo 0 > "$debugFolder/tracing_on"
echo function_graph > "$debugFolder/current_tracer"

# setup ftrace filter to record mptcp functions only
echo 'mptcp*' > "$debugFolder/set_ftrace_filter"
echo 'queue_work' >> "$debugFolder/set_ftrace_filter"

echo ":mod:lig_module" >> "$debugFolder/set_ftrace_filter"



# enable ftrace
echo 1 > "$debugFolder/tracing_on";

$CMD

echo 0 > "$debugFolder/tracing_on"

EOF

eval "$command"

#|grep -n
echo -e "To see trace, exec:\nless $debugFolder/trace"
