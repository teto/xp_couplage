#!/usr/bin/python3
# IMPORTANT launch naming service beforehand
# python3 -Wignore -m Pyro4.naming --host [your ip] --port [your port]
# 
# when closed incorrectly, socket keeps opened
# netstat -pn | grep CLOSE_WAIT
# or more thorough 
# netstat -tonp
# 
import Pyro4
import host
# import subprocess
import natutils
import argparse
import configparser
import logging
import os
import threading
import sys


logger = logging.getLogger( __name__)

# self.address = address
config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )

# set variable MainDir in config file
config.set("DEFAULT", "MainDir", os.path.realpath( os.path.dirname(__file__) ))
config.read( "tests.ini")


# def launch_nameserver(ip,port):
	# python3 -Wignore -m Pyro4.naming --host ip --port port



# can only be set as env var
# Pyro4.config.LOGLEVEL = DEBUG

class PyroServer(Pyro4.Daemon):

	default_daemon_port=4242
	default_ns_port=4242

	# def look_for_nat():
	def __init__(self, port=default_daemon_port, localhostname=None, nat_port=None, nat_host=None):

		if not localhostname:
			localhostname = Pyro4.socketutil.getIpAddress("localhost", workaround127=True, ipVersion=None)

		# ip2= Pyro4.socketutil.getInterfaceAddress("eth0")

		logger.info("Trying to bind daemon on ip ", localhostname)
		#Pyro4.config

		if not nat_host:
			# natd = nat device ?!
			nat = natutils.Nat.look_for_nat()
			if nat:
				logger.info("NAT detected")
				# make a Pyro daemon, port=0 => random port

				logger.info("Trying to add port mapping")

				nat_host = nat.getExternalIp()

				# nat.addportmapping(64000, #time
				# 					'TCP', # protocol
				# 				nat_host, 
				# 				63000, 
				# 				'port mapping test', 
				# 				''
				# 				)
				# TODO create a forwarding rule
				#find one with the name of 
				# by default
				nat_port = 4242 
				


		# daemon=Pyro4.Daemon( host="192.168.1.102", port=4242, natport=4242,nathost="82.121.111.63")
		# daemon=
		super().__init__( port=port, natport=nat_port, nathost=nat_host, host=localhostname)


	# You may want to launch the nameserver by hand
	# python3 -m Pyro4.naming
	# port=None,host=None, nat_host=None,nat_port=None
	def startNS(self, *args):
		# threading.Thread(target=)
		#bchost=None, bcport=None, unixsocket=None,
		#enableBroadcast=True,
		#host=None, port=None,   nathost=nat_host, natport=nat_port
		Pyro4.naming.startNS(args)
		# self.ns = 

		# # find the name server
		
			# TODO
			# ns=Pyro4.locateNS( host=ip, port=config['pyro'].getint("ns_port") )

			# register the object with a name in the name server
			# ns.register("host", uri)

		# print ("Registered host:",uri)
		print ("Ready.")



	def run(self):

		logger.info("Starting ");
		self.requestLoop()                  # start the event loop of the server to wait for calls


# Pyro4.Daemon.serveSimple(
#         {
#             warehouse: "example.warehouse"
#         },
#         ns = True)




## This function takes the 'extra' attribute from global namespace 
# and re-parses it to create separate namespaces for all other chained commands.
def parse_extra (parser, namespace):
  namespaces = []
  extra = namespace.extra
  while extra:
    n = parser.parse_args(extra)
    extra = n.extra
    namespaces.append(n)

  return namespaces


# accept parser and arguments
def parse_and_accept_several_subcommands(parser, *args):
	namespaces = {}
	#sys.argv[1:]
	namespaces["default"] = parser.parse_args( args )
	
	# extra_namespaces = parse_extra( parser, args )
	# associate it with a subcommand
	extra = namespaces["default"].extra
	while extra:
		new_namespace = parser.parse_args(extra)
		extra = new_namespace.extra
		namespaces[new_namespace.subcommand](new_namespace)

	return namespaces




if __name__ == '__main__':

	parser = argparse.ArgumentParser(
			description='Run a Pyro4 server, sharing objects with remote scripts'
			)

	parser.add_argument('config', type=argparse.FileType('r'),  default="tests.ini", help="Config filename. Describe experiment settings")

	# should give the opportunity to override settings

	parser.add_argument('remotehost', action="store",help="remote ip or hostname")
	parser.add_argument('localhost', action="store", nargs="?", help="local ip or hostname")
	# parser.add_argument('--ns', action="store", nargs="?", help="nameserver parameters")

	# define it into config file for now
	# parser.add_argument('remoteport', action="store",type=int, help="ssh port ? in order to launch server")



	subparsers  = parser.add_subparsers(dest="subcommand", title="test", help='sub-command help')

	ns_parser = subparsers.add_parser('ns',help='nameserver external IP or associated hostname')
	ns_parser.add_argument('port',type=int,help="Port on which the nameserver is running")
	ns_parser.add_argument('extra', nargs = "*", help = 'Other commands')



	nat_parser = subparsers.add_parser('external_ip',help='external IP or associated hostname')
	nat_parser.add_argument('external_port', action="store",type=int, help="port")

	
	parser.add_argument('extra', nargs = "*", help = 'Other commands')


	# Actually launch the thing here
	# config['pyro'].getint("daemon_port")
	#there must be at most one ?
	# if config['pyro'].getboolean("use_nameserver"):

	# args = parser.parse_args( sys.argv[1:] )
	

	# extra_namespaces = parse_extra( parser, args )

	namespaces = parse_and_accept_several_subcommands(parser, sys.argv[1:])

	if namespaces["nat"]:
		print (" nat", namespaces["nat"].external_port )


	if namespaces["ns"]:
		print (" ns", namespaces["ns"].port )

	# # port
	# print("Remote Hostname: " , args.remotehost )
	# print("Local Hostname: " , args.localhost )
	# print("ns: " , args.ns )
	# print("mode: " , args.mode )
	# print("ns: " , args.ns_port )

	# daemon = PyroServer( localhostname=args.localhost  )

	# register the greeting object as a Pyro object
	localhost = host.Host("server.ini")

	# TODO ptet ecraser la fonction register
	# uri=daemon.register(localhost)

	# ns=Pyro4.locateNS( host=ip, port=config['pyro'].getint("ns_port") )
