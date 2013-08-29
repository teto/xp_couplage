#!/usr/bin/python3

import subprocess
import argparse
import sys
import os

#
#/proc/net/mptcp/mptcp
# only "static" functions
class MPTCP:
	def __init__(self):
		pass


	@staticmethod
	def get_global_state():
		return subprocess.check_output("sysctl -n net.mptcp.mptcp_enabled")

	#def switch_state():

	@staticmethod
	def set_global_state(state):
		os.system("sudo bash -c 'sysctl -w net.mptcp.mptcp_enabled="+ str(state) + "'")

	@staticmethod
	def get_if_capability(if_name):
		return subprocess.check_output("ip addr show "+ if_name +" | grep -o NOMULTIPATH")

	@staticmethod
	def set_if_capability(if_name, state):
		return subprocess.check_output("sudo ip link set dev " + if_name + " multipath " + state)
	#	return False
	#local cmd="$SUDO "

	@staticmethod
	def enable():
		return MPTCP.set_global_state(1)
		
	@staticmethod
	def disable():
		return MPTCP.set_global_state(0)




# in case script is called directly
if __name__ == '__main__':
	parser = argparse.ArgumentParser(
	#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
	description='Will run tests you precise'
	)

	#, required=True
	parser.add_argument('action', choices=('enable','disable'), action="store")
	parser.add_argument('interfaces', nargs='*', action="store")
	args = parser.parse_args( sys.argv[1:] )

	if args.action == "enable":
		if len(args.interfaces) > 0:
			for if_name in args.interfaces:
				print ("Setting mptcp for interface ", if_name,"to ","on")
				MPTCP.set_if_capability( if_name , "on" )
		else:
			MPTCP.enable()
	# disable MPTCP
	else:
		# don't 
		MPTCP.disable()


