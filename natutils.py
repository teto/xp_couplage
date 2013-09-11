#! /usr/bin/python3


# import the python miniupnpc module
import miniupnpc
import sys
import argparse
import logging



logger = logging.getLogger(__name__)


# Binding for miniupnp
class Nat:

	# upnpc of type miniupnpc.UPnP()
	def __init__(self,upnpc):
		self.u = upnpc
		try:
			self.u.selectigd()
		except Exception as e:
			logging.error ('Exception :', e)
			# sys.exit(1)

	def getLocalIp(self):
		return self.u.lanaddr

	def getExternalIp(self):
		# self.u.selectigd()
		return self.u.externalipaddress()

	# protocol might be TCP or UDP
	def port_mapping_add(self, protocol, external_port, lanaddr, local_port, description ):

	    return self.u.addportmapping(external_port, protocol, lanaddr, local_port,
                            description, '')
	    
	# delete
	def port_mapping_del(self, external_port, protocol):
		return self.u.deleteportmapping( external_port, protocol)

	@staticmethod
	def look_for_nat():
		# create the object
		u = miniupnpc.UPnP()
		# print ('inital(default) values :')
		# print (' discoverdelay', u.discoverdelay)
		# print (' lanaddr', u.lanaddr)
		# print (' multicastif', u.multicastif)
		# print (' minissdpdsocket', u.minissdpdsocket)
		u.discoverdelay = 200;
		#u.minissdpdsocket = '../minissdpd/minissdpd.sock'
		# discovery process, it usualy takes several seconds (2 seconds or more)
		logging.debug ('Discovering... delay=%ums' % u.discoverdelay)
		nb_devices = u.discover()
		logging.info ( '%d device(s) detected'%nb_devices)

		if nb_devices == 0:
			return None
		# select an igd
		try:
			u.selectigd()
		except Exception as e:
			logging.error ('Exception :', e)
			sys.exit(1)

		# display information about the IGD and the internet connection
		logging.info ("local ip address : %s" % u.lanaddr)
		logging.info ("external ip address :%s" % u.externalipaddress())
		# print u.statusinfo(), u.connectiontype()
		return Nat(u)

# time
#print u.addportmapping(64000, 'TCP',
#                       '192.168.1.166', 63000, 'port mapping test', '')
#print u.deleteportmapping(64000, 'TCP')

# port = 0
# proto = 'UDP'
# # list the redirections :
# i = 0
# while True:
# 	p = u.getgenericportmapping(i)
# 	if p==None:
# 		break
# 	print i, p
# 	(port, proto, (ihost,iport), desc, c, d, e) = p
# 	#print port, desc
# 	i = i + 1

# print u.getspecificportmapping(port, proto)


if __name__ == '__main__':
	print('Looking for a nat');
	nat = Nat.look_for_nat()

	if not nat:
		print ("No Nat found")
		exit

	# NAT found
	print ("Nat found")
	print("External IP",nat.getExternalIp() )
	parser = argparse.ArgumentParser(description='Will run tests you precise')


    # 
    # module_parser.add_argument('action', choices=('compile','load','unload') )
    # module_parser.set_defaults(func=handle_module)


	subparsers = parser.add_subparsers(dest="mode", help='sub-command help')
    
	add_parser = subparsers.add_parser('add', help='module help')
	add_parser.add_argument('port', type=int, help="External port")
	add_parser.add_argument('protocol', choices=('TCP','UDP') )

	del_parser = subparsers.add_parser('del', help='module help')
	del_parser.add_argument('port', type=int, help="External port")
	del_parser.add_argument('protocol', type=str, help="External port")


	args = parser.parse_args( sys.argv[1:] )

	print ("chosen mode" , args.mode )

	#
	if args.mode == "add":
	# args.func( nat, args)
	# otocol, external_port, lan_addr, local_port, description
		nat.port_mapping_add(  args.protocol,args.port, nat.getLocalIp(), args.port,"Test rule")
	elif args.mode == "del":
		nat.port_mapping_del( args.port, args.protocol )