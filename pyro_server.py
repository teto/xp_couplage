#!/usr/bin/python3
# IMPORTANT launch naming service beforehand
# python3 -Wignore -m Pyro4.naming --host [your ip] --port [your port]
# TODO remove UPnP rules on closing (catch signal ?)
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
import signal 



logger = logging.getLogger( __name__)
logger.setLevel(logging.DEBUG)

# self.address = address
config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )

# set variable MainDir in config file
config.set("DEFAULT", "MainDir", os.path.realpath( os.path.dirname(__file__) ))
config.read( "tests.ini")


# def launch_nameserver(ip,port):
	# python3 -Wignore -m Pyro4.naming --host ip --port port

def sigint_handler(signum, frame):
	print( 'Stop pressing the CTRL+C!', frame )
	daemon.close()

signal.signal(signal.SIGINT, sigint_handler)


# can only be set as env var
# Pyro4.config.LOGLEVEL = DEBUG

class PyroServer(Pyro4.Daemon):

	default_daemon_port=4242
	default_ns_port=4242


	def getHostname(self):
		# return super().locationStr;
		res= self.locationStr.split(":");
		return res[0], int(res[1])

	def getNatHostname(self):
		res = self.natLocationStr.split(":");
		return res[0], int(res[1])

	# def look_for_nat():
	# TODO pass **kwargs
	# nat_port=None, 
	def __init__(self, port=default_daemon_port, localhostname=None, nat_host=None, **kwargs):

		if not localhostname:
			localhostname = Pyro4.socketutil.getIpAddress("localhost", workaround127=True, ipVersion=None)
			# logger
		# ip2= Pyro4.socketutil.getInterfaceAddress("eth0")

		logger.info("Trying to bind daemon on ip %s"%localhostname)
		#Pyro4.config

		if not nat_host:
			# natd = nat device ?!
			self.nat = natutils.Nat.look_for_nat()
			if self.nat:
				# self.nat = natutils.Nat(nat_found)
				logger.info("NAT detected")
				# make a Pyro daemon, port=0 => random port

				logger.info("Trying to add port mapping")

				nat_host = self.nat.getExternalIp()
				#port_mapping_add(self, protocol, external_port, lanaddr, local_port, description ):
				# self.nat.addportmapping('TCP')
				nat_port = 4242 
				


		# daemon=Pyro4.Daemon( host="192.168.1.102", port=4242, natport=4242,nathost="82.121.111.63")
		# daemon=
		# logger.info("Launching daemon ")
		super().__init__( port=port, natport=nat_port, nathost=nat_host, host=localhostname)

		print ( "Hostname configuration", self.getHostname() )
		print ( "Nat configuration", self.getNatHostname() )


	# You may want to launch the nameserver by hand
	# python3 -m Pyro4.naming
	# port=None,host=None, nat_host=None,nat_port=None
	# ,*args, **keywords
	def startNameServer(self, port ):
		# threading.Thread(target=)
		#bchost=None, bcport=None, unixsocket=None,
		#enableBroadcast=True,
		#host=None, port=None,   nathost=nat_host, natport=nat_port
		logger.info("Starting nameserver ...")
		# nat_host = nathost
		hostname,daemon_port = self.getHostname()
		nat_host, nat_port = self.getNatHostname()
		# natport=nat_port
		# Unixsocket
		(nameserverUri, self.ns_daemon, broadcastServer) = Pyro4.naming.startNS(
					host=hostname,
					# host=hostCfg[0],
					port=port,
					unixsocket=False, 
					nathost=nat_host,
					natport=nat_port
					# **keywords 
					)
		print("Nameserver available on Uri %s"%nameserverUri)

		# # find the name server
		# locateNS returns a proxy towards
		self.ns = Pyro4.core.Proxy( nameserverUri )
		# self.ns = Pyro4.locateNS( host=ip, port=config['pyro'].getint("ns_port") )
		# register the object with a name in the name server
		# ns.register("host", uri)
		# print ("Registered host:",uri)
		print ("Ready.")


	# def register
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
# def parse_extra (parser, namespace):
#   namespaces = []
#   extra = namespace.extra
#   while extra:
#     n = parser.parse_args(extra)
#     extra = n.extra
#     namespaces.append(n)

#   return namespaces


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



def ns_cli_parser(args,namespace=None):
	ns_parser = argparse.ArgumentParser(
			description='Nameserver parser'
		)

	# REMAINDER

	ns_parser.add_argument('port',type=int,help="Port on which the nameserver is running")
	return ns_parser.parse_args(args,namespace)





if __name__ == '__main__':



	# TODO need to create one parser per optional subcommand
	# pass it the namespace




	parser = argparse.ArgumentParser(
			description='Run a Pyro4 server, sharing objects with remote scripts'
			)

	#argparse.FileType('r')
	parser.add_argument('config', default="tests.ini", action="store", type=str,  help="Config filename. Describe experiment settings")

	# should give the opportunity to override settings

	parser.add_argument('remotehost', action="store",help="remote ip or hostname")
	parser.add_argument('localhost', action="store", nargs="?", help="local ip or hostname")
	parser.add_argument('--ns', action="store", nargs="?", help="hello" ) #ns_parser.print_help() )
	parser.add_argument('--nat', action="store", help="world") #nat_parser.print_help() )
	#nargs="*",
	# parser.add_argument('--ns', action="store", nargs="?", help="nameserver parameters")
	# define it into config file for now
	# parser.add_argument('remoteport', action="store",type=int, help="ssh port ? in order to launch server")
# parents=[parent_parser]
	# subparsers  = parser.add_subparsers(dest="subcommand", title="test", help='sub-command help')
	# main_subparser = subparsers.add_parser('--ns',help='nameserver external IP or associated hostname')
	# main_subparser.add_subparsers(dest="subcommand")
	# ns_parser = subparsers.add_parser('--ns',help='nameserver external IP or associated hostname')
	# ns_parser.add_argument('extra', nargs = "*", help = 'Other commands')
	# nat_parser = subparsers.add_parser('external_ip',help='external IP or associated hostname')
	# nat_parser.add_argument('external_port', action="store",type=int, help="port")
	# parser.add_argument('extra', nargs = "*", help = 'Other commands')
	# Actually launch the thing here
	# config['pyro'].getint("daemon_port")
	#there must be at most one ?
	# if config['pyro'].getboolean("use_nameserver"):

	args = parser.parse_args( sys.argv[1:] )


	nat_port = None
	nat_host = None

	if args.nat:
		# list of arguments + namespace
		nat_args = natutils.nat_cli_parser( args.nat, args );
		nat_port = nat_args.external_port
		nat_host = nat_args.external_host


	print("Remote Hostname: " , args.remotehost )
	# print("Local Hostname: " , args.localhost )

	print("natport: " , nat_port)
	print("nathost: " , nat_host)
	# print("ns: " , args.ns_port )

	daemon = PyroServer( 
				port= config['pyro'].getint("daemon_port")
					#localhostname=args.localhost,
						)

	use_nameserver = config['pyro'].getboolean("use_nameserver")
	ns_port = None
	if args.ns:
		logger.info("Asked for a nameserver ...")
		ns_args = ns_cli_parser(args.ns)
		# print (args.ns) #,"3232" ["4242"]
		# ns_args = ns_parser.parse_args( args.ns );
		ns_port = ns_args.port
		print( "override configuration file ns_port", ns_port )


	#there must be at most one ?
	if use_nameserver:
		daemon.startNameServer(port= ns_port )

	# register the greeting object as a Pyro object
	localhost = host.Host("server.ini")

	# TODO ptet ecraser la fonction register
	uri=daemon.register(localhost)
	daemon.ns.register(uri)
	# ns=Pyro4.locateNS( host=ip, port=config['pyro'].getint("ns_port") )
	daemon.run()