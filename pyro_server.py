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
# import host
# import subprocess
# import natutils
import argparse
import configparser
import logging
import os
import threading
import sys
import signal 
import socket
import select
import multiprocessing
from Pyro4 import threadutil
from isix.network import natutils
import isix.host as host

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
	# server.close()
	exit(1)

signal.signal(signal.SIGINT, sigint_handler)


Pyro4.config.SOCK_REUSE = True
# Pyro4.config.SOCK_REUSE = True

# TODO split this into a 
# MORE ABOUT THreads:
# http://docs.python.org/3/library/threading.html#module-threading
# 
#    A factory function that returns a new event object. An event manages a flag that can be set to true with the set() method and reset to false with the clear() method.
#    The wait() method blocks until the flag is true.
class NameServer(threadutil.Thread):
	def __init__(self, **kwargs):
		# super(NameServer,self)
		super().__init__()

		#A thread can be flagged as a “daemon thread”.
		# The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. 
		# The flag can be set through the daemon property.
		self.setDaemon(1)
		self.args=kwargs
		self.started=threadutil.Event()

	def run(self):
		self.uri, self.ns_daemon, self.bc_server = Pyro4.naming.startNS( **self.args)
		self.started.set()
		logger.info("Starting nameserver %s NAt: %s"%(self.ns_daemon.locationStr,self.ns_daemon.natLocationStr))
		self.ns_daemon.requestLoop()


# def startNameServer(host):
# 	ns=NameServer(host)

# 	# start calls run function in another thread
# 	ns.start()
# 	ns.started.wait()
# 	return ns


# can only be set as env var
# Pyro4.config.LOGLEVEL = DEBUG
# 
# call shutdown
class PyroServer(threading.Thread):

	# default_daemon_port=4242
	# default_ns_port=4242


	def getHostname(self):
		# return super().locationStr;
		res= self.daemon.locationStr.split(":");
		return res[0], int(res[1])

	def getNatHostname(self):
		# print('res',self.daemon.natLocationStr)
		if self.daemon.natLocationStr:
			res = self.daemon.natLocationStr.split(":");
			return res[0], int(res[1])
		return None,None

	def getLogger(self):
		return self.h

	# def look_for_nat():
	# TODO pass **kwargs
	# nat_port=None, 
	def __init__(self, port, localhostname=None, nat_host=None, nat_port=None, **kwargs):

		self.q = multiprocessing.Queue()
		self.logger = logging.getLogger("Main")

		self.qh = logging.handlers.QueueHandler(self.q)
		
		self.h = logging.StreamHandler()
		
		# a chaque fois qu'on ecrit dans le logger Main,
		# il va ecrire dans le QueueHandler
		self.logger.addHandler( self.qh )
		# root = logging.getLogger()
		# root.addHandler( self.h )
		
		# pass handlers
		# when listener discovers records, it will forward them to 
		# the stream handler
		self.listener = logging.handlers.QueueListener( self.q, self.h )

		print("=== Starting logger listener ===")
		self.listener.start()

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
		threading.Thread.__init__(self)

		self.setDaemon(True)

		self.daemon = Pyro4.Daemon( port=port, natport=nat_port, nathost=nat_host, host=localhostname)

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
		self.ns = NameServer(
		#(nameserverUri, self.ns_daemon, self.broadcastServer) = Pyro4.naming.startNS
			
					host=hostname,
					# host=hostCfg[0],
					port=port,
					#unixsocket=None, 
					nathost=nat_host,
					natport=nat_port
					# **keywords 
					)
		# print("Nameserver available on Uri %s"%nameserverUri)
		# print("ns daemon location string=%s" %self.ns_daemon.locationStr)
		# print("ns daemon sockets=%s" % self.ns_daemon.sockets)
		# # find the name server
		# locateNS returns a proxy towards
		# Pyro4.core.Proxy( self.getNameServer().uri )
		# self.ns = Pyro4.locateNS( host=ip, port=config['pyro'].getint("ns_port") )
		# register the object with a name in the name server
		# ns.register("host", uri)
		# print ("Registered host:",uri)
		print ("Ready" )
		self.ns.start()


	def locateNameServer(self):
		pass


	# TODO 
	# display available services 
	# cleanup isix on except (KeyboardInterrupt, SystemExit):
	# def register
	# requestLoop() is blocking :/
	def run(self):

		# below is our custom event loop.
		# while True:

		logger.info("Starting ");

		# TODO be able to change behavior on certain key press,
		# to display that help at some interval
		# except KeyboardInterrupt:

		# 	print("Waiting for events...")
		# 	# create sets of the socket objects we will be waiting on
		# 	# (a set provides fast lookup compared to a list)
		# 	nameserverSockets = set(self.ns_daemon.sockets)
		# 	pyroSockets = set(self.daemon.sockets)
		# 	rs=[self.broadcastServer] # only the broadcast server is directly usable as a select() object
		# 	# what does that mean ?
		# 	rs.extend(nameserverSockets)
		# 	rs.extend(pyroSockets)
		# 	rs,_,_ = select.select(rs,[],[],3)
		# 	eventsForNameserver=[]
		# 	eventsForDaemon=[]
		# 	for s in rs:
		# 		if s is self.broadcastServer:
		# 			print("Broadcast server received a request")
		# 			self.broadcastServer.processRequest()
		# 		elif s in nameserverSockets:
		# 			eventsForNameserver.append(s)
		# 		elif s in pyroSockets:
		# 			eventsForDaemon.append(s)
		# 		if eventsForNameserver:
		# 			print("Nameserver received a request")
		# 			self.getDaemon().events(eventsForNameserver)

		# 		# handle events
		# 		if eventsForDaemon:
		# 			print("Daemon received a request")
		# 			self.getDaemon().events(eventsForDaemon)
		 # start the event loop of the server to wait for calls
		self.getDaemon().requestLoop()


	def getDaemon(self):
		return self.daemon

	def getNameServer(self):
		return self.ns

	def __exit__(self):
		# if self.ns:
			# self.ns_daemon.close()
		#shutdown
		self.getDaemon().close()


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




def worker_process():
	logger = logging.getLogger("Main")
	logger.warning("worker working")






if __name__ == '__main__':


	# List of all options there: http://pythonhosted.org/Pyro4/config.html
	# Pyro4.config.COMMTIMEOUT = 60


	parser = argparse.ArgumentParser(
			description='Run a Pyro4 server, sharing objects with remote scripts'
			)

	#argparse.FileType('r')
	parser.add_argument('xpconfig', default="tests.ini", action="store", type=str,  help="Config filename. Describe experiment settings")

	# should give the opportunity to override settings

	parser.add_argument('hostconfigfile', action="store", type=argparse.FileType('r'), help="remote ip or hostname")

	parser.add_argument('localhost', action="store", nargs="?", help="local ip or hostname")
	parser.add_argument('--ns', action="store", nargs="?", help="hello" ) #ns_parser.print_help() )
	parser.add_argument('--nat', action="store", help="world") #nat_parser.print_help() )

	args = parser.parse_args( sys.argv[1:] )


	nat_port = None
	nat_host = None

	if args.nat:
		# list of arguments + namespace
		nat_args = natutils.nat_cli_parser( args.nat, args );
		nat_port = nat_args.external_port
		nat_host = nat_args.external_host


	#print("Remote Hostname: " , args.remotehost )
	# print("Local Hostname: " , args.localhost )

	# print("natport: " , nat_port)
	# print("nathost: " , nat_host)
	# print("ns: " , args.ns_port )

	server = PyroServer( 
				port= config['pyro'].getint("daemon_port"),
				localhostname=args.localhost
						)

	use_nameserver = config['pyro'].getboolean("use_nameserver")
	ns_port = config['pyro'].getint("ns_port")

	if args.ns:
		logger.info("Asked for a nameserver ...")
		ns_args = ns_cli_parser(args.ns)
		# print (args.ns) #,"3232" ["4242"]
		# ns_args = ns_parser.parse_args( args.ns );
		ns_port = ns_args.port
		print( "override configuration file ns_port", ns_port )


	#there must be at most one ?
	if use_nameserver:
		server.startNameServer(port= ns_port )



	server.start()

	# register the greeting object as a Pyro object
	localhost = host.Host( args.hostconfigfile)

	logger.info("Registering host")
	# # TODO ptet ecraser la fonction register
	uri=server.getDaemon().register(localhost)
	
	print(uri)
	# 
	ip =server.getHostname()[0]
	ns=Pyro4.locateNS( host=ip, port=ns_port )
	# uri = 
	ns.register("host", uri)


	logger.info("Host registered. New uri %s"% uri)


	print("port ", localhost.config["webfs"]["port"])
	server.run()

