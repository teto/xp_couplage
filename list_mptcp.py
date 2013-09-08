#!/usr/bin/python3

# Presentation of /proc/net/tcp here
#http://lkml.indiana.edu/hypermail/linux/kernel/0409.1/2234.html

import sys
import struct 
import socket
# import configparser
import argparse
from collections import OrderedDict

#"id",  
# sl  loc_tok  rem_tok  v6 local_address                         remote_address                        st ns tx_queue rx_queue inode
# 0: 2D0B85BA 39F8CCC5  0 6601A8C0:E89F                         2DE66882:0050                         01 01 00000000:00000000 21895

# define as dict for conversion
#subflows

def identity(value):
	return value

def convert_port( port):
	# expects str,base
	return int(port,16)

def ntoa( eid ):
	packed_value = struct.pack('I', int(eid,16) ) 
	return socket.inet_ntoa(packed_value)


mptcpNames = OrderedDict( [
("sl" , identity),
("local_token" , identity),
("rmt_token" , identity),
("v6" , identity), 
("local_addr" , ntoa),
("local_port" , convert_port),
("rmt_addr" , ntoa), 
("rmt_port" , convert_port),
("state" , identity),
("ns" , int ),
("tx_queue", identity),
("rx_queue", identity),
("inode"	, int)
] )

# care not to declare it as OrderedDict( {} ) but as a list of tuples
# otherwise the temporary {} dict loses order
tcpNames = OrderedDict ( [ 
("sl" , identity),
("local_addr", ntoa),
("local_port", convert_port),
("rmt_addr", ntoa),
("rmt_port" , convert_port),
("state", identity),
("tx_queue", identity),
("rx_queue", identity),
("timer active", identity),
("number of jiffies until timer expires", identity),
("nb of uncovered RTO timeouts", identity),
("uid", identity),
("unanswered probes", identity),
("inode", int),
("sk reference count", int)
] )

# list( enumerate(tokens) )

# print modulo % ns
# def maptest(descriptors, values):
def convert_tcp_state(state):
	# pass
	# states = ["Undefined", "TCP_ESTABLISHED",
	# "TCP_SYN_SENT",
	# "TCP_SYN_RECV",
	# "TCP_FIN_WAIT1",
	# "TCP_FIN_WAIT2",
	# "TCP_TIME_WAIT",
	# "TCP_CLOSE",
	# "TCP_CLOSE_WAIT",
	# "TCP_LAST_ACK",
	# "TCP_LISTEN",
	# "TCP_CLOSING"]
	return int(state)

class Entry:
	def __init__(self,entry):
		self.entry = entry

	def display(self):
		raise NotImplementedError;




# kind of a csv reader
def load_entries(file,descriptors, generator ):

	entries = []

	with open(file, newline='') as connections:

		# skip first line (title)
		for line in connections.readlines()[1:]:

			items = line.replace(':',' ').split() #[1:]
			

			# print ("lol", descriptors.keys() )
			# print ("Before transformations", items)
			# transform 
			for i,fn in enumerate(descriptors.values() ):
				items[i] =  ( fn(items[i]) )

			entry = generator( OrderedDict(zip(descriptors.keys(), items ) ) )

			entries.append ( entry )


	return entries




class TCPEntry(Entry):
	def __init__(self,entry):
		
		super().__init__(entry)

	# tcpEntry,mptcpEntry
	def format(self):
		#{0[local_port]}%{subflows} = {result}
		return "{protocol:>5}: {0[local_addr]:>15}:{0[local_port]:05} -> {0[rmt_addr]:>15}:{0[rmt_port]:05} ".format(
				self.entry,
				protocol="TCP",
				# subflows=mptcpEntry["ns"],
				# result = ( tcpEntry["local_port"]  % mptcpEntry["ns"] )
				 )
		

	@staticmethod
	def load_entries():
		return load_entries('/proc/net/tcp', tcpNames, TCPEntry )



#mptcpNames

class MPTCPEntry(Entry):

	def __init__(self,entry):
		
		super().__init__(entry)


	def format(self):
		return "{protocol:>5}: {0[local_addr]:>15}:{0[local_port]:05} -> {0[rmt_addr]:>15}:{0[rmt_port]:05} with {0[ns]} subflows. Inode: {0[inode]}".format(
						self.entry,
						protocol="MPTCP"
						 )

	@staticmethod
	def load_entries():
		return load_entries('/proc/net/mptcp', mptcpNames, MPTCPEntry )





def describe_timer(value):
	descriptions= [ "no timer is pending" , 
	"retransmit-timer is pending" , 
	"another timer (e.g. delayed ack or keepalive) is pending" ,
	"TIME_WAIT",
	"Zero window probe"

	]
	return descriptions[ value ]









# class MPTCPEntry():

# == HOW TO FORMAT ==
# '{:>12}  {:>12}  {:>12}'.format(word[0], word[1], word[2])
# where > means "align to right" and 8 is the width for specific value.
# add a 0 in front to fill width with 0s
# def display_mptcp_entry(entry):
# 	print ( "{protocol:>5}: {0[local_addr]:>15}:{0[local_port]:05} -> {0[rmt_addr]:>15}:{0[rmt_port]:05} with {0[ns]} subflows. Inode: {0[inode]}".format(
# 					entry,
# 					protocol="MPTCP"
# 					 )
# 	)

# def display_tcp_entry(tcpEntry,mptcpEntry):

# 	print ( "{protocol:>5}: {0[local_addr]:>15}:{0[local_port]:05} -> {0[rmt_addr]:>15}:{0[rmt_port]:05} {0[local_port]}%{subflows} = {result}".format(
# 			tcpEntry,
# 			protocol="TCP",
# 			subflows=mptcpEntry["ns"],
# 			result = ( tcpEntry["local_port"]  % mptcpEntry["ns"] )
# 			 )
# 	)





if __name__ == "__main__":

	parser = argparse.ArgumentParser(
		#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
		description=""
		# ,formatter_class=argparse.RawDescriptionHelpFormatter
		)

	parser.add_argument('mode', choices=(
								'mptcp',
								'tcp',
								),
							nargs="?",
							default="mptcp",
					  help="Choose"
					  )

	parser.add_argument('-e', dest="extended",
							action="store_true",
							# default="mptcp",
					  help="Detailed view of the entries"
					  )

	# parse arguments
	args = parser.parse_args( sys.argv[1:] )


	mptcpEntries 	= MPTCPEntry.load_entries()
	#mptcpEntries 	= load_entries('/proc/net/mptcp', mptcpNames)
	#tcpEntries 		= load_entries('/proc/net/tcp', tcpNames)
	tcpEntries 		= TCPEntry.load_entries()

	print("mode:", args.mode )

	# for tcpEntry in tcpEntries: 
	# # 	pass
	# 	print("tcpEntry", tcpEntry.format())
		


	# TODO add a summary (how many MPTCP connections/ subflows)
	for mptcpEntry in mptcpEntries:

		print( mptcpEntry.format() )

		# print("MPTCP:", mptcpEntry["local address"])
		for tcpEntry in tcpEntries: 
		# 	pass
			# print("tcpEntry", tcpEntry)
			if tcpEntry.entry["inode"] != mptcpEntry.entry["inode"]:
				continue

			#print("TCP subflow", tcpEntry["inode"])
			print(tcpEntry.format() + 
			"{0[local_port]}%{subflows} = {result}".format(
				tcpEntry.entry,
	 			subflows=mptcpEntry.entry["ns"],
				result = ( tcpEntry.entry["local_port"]  % mptcpEntry.entry["ns"] ) 
					
				)
			)
