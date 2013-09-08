#!/usr/bin/python3

# Presentation of /proc/net/tcp here
#http://lkml.indiana.edu/hypermail/linux/kernel/0409.1/2234.html

import binascii
import struct 
import socket
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
	pass
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

def describe_timer(value):
	descriptions= [ "no timer is pending" , 
	"retransmit-timer is pending" , 
	"another timer (e.g. delayed ack or keepalive) is pending" ,
	"TIME_WAIT",
	"Zero window probe"

	]
	return descriptions[ value ]


def load_entries(file,descriptors):

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

			entry = OrderedDict(zip(descriptors.keys(), items ) )
	#		print ("After transformations", entry )
			# 
			# entry["local address"] = ntoa( entry["local address"])
			# entry["local port"]		= binascii.unhexlify

			# dict( name, value ) 
			# for (name,value) in 

			entries.append ( entry )


	return entries



mptcpEntries 	= load_entries('/proc/net/mptcp', mptcpNames)
tcpEntries 		= load_entries('/proc/net/tcp', tcpNames)


# for tcpEntry in tcpEntries: 
# # 	pass
# 	print("tcpEntry", tcpEntry)

# # def associated_subflows():

# class MPTCPEntry():

# == HOW TO FORMAT ==
# '{:>12}  {:>12}  {:>12}'.format(word[0], word[1], word[2])
# where > means "align to right" and 8 is the width for specific value.
def display_mptcp_entry(entry):
	print ( "{protocol:>7}: {0[local_addr]:12}:{0[local_port]:5} -> {0[rmt_addr]}:{0[rmt_port]:5} with {0[ns]} subflows. Inode: {0[inode]}".format(
					mptcpEntry,
					protocol="MPTCP"
					# local_addr=mptcpEntry["local_addr"],
					# local_port=mptcpEntry["local_port"],
					# rmt_addr=mptcpEntry["rmt_addr"],
					# rmt_port=mptcpEntry["rmt_port"],
					# subflows=mptcpEntry["ns"],
					# inode=mptcpEntry["inode"]
					 )
	)

def display_tcp_entry(tcpEntry,mptcpEntry):

	print ( "{protocol:>7}: {0[local_addr]}:{0[local_port]} -> {0[rmt_addr]}:{0[rmt_port]} {local_port}%{subflows} = {result}".format(
			tcpEntry,
			protocol="TCP",
			# local_addr=tcpEntry["local_addr"],
			# local_port=tcpEntry["local_port"],
			# rmt_addr=tcpEntry["rmt_addr"],
			# rmt_port=tcpEntry["rmt_port"],
			# subflows=mptcpEntry["ns"],
			result = ( tcpEntry["local_port"]  % mptcpEntry["ns"] )
			 )
	)

for mptcpEntry in mptcpEntries:

	display_mptcp_entry(mptcpEntry)
	#,value
	# for key in mptcpEntry:


		# print ("Key" , key, ":", value ); #, ":", mptcpEntry[key])

	# print("MPTCP:", mptcpEntry["local address"])
	for tcpEntry in tcpEntries: 
	# 	pass
		# print("tcpEntry", tcpEntry)
		if tcpEntry["inode"] != mptcpEntry["inode"]:
			continue

		#print("TCP subflow", tcpEntry["inode"])
		display_tcp_entry(tcpEntry, mptcpEntry )

# with open('/proc/net/mptcp', newline='') as mptcpConnections:


# 	# skip first line (title)
# 	for mptcpLine in mptcpConnections.readlines()[1:]:

# 		items = mptcpLine.replace(':',' ').split()[1:]

# 		mptcpSk = dict(zip(tcpNames, items))

# 		with open('/proc/net/tcp', newline='') as tcpConnections:

# 			for tcpLine in tcpConnections.readlines()[1:]:

# 				if mptcpSk

		# print ( "test ", items["local address"] , items["inode"])
		# print( "lol?", ntoa(items["local address"]) )
		# print( "lol?", ntoa(items["local port"]) )
		
		# for key,item in enumerate( items ):
			# print ( "key", key, "item", item );


		# with open('/proc/net/tcp', newline='') as sockets:


	# spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	# for row in spamreader:
	# 	print(', '.join(row))
