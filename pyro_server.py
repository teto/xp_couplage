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
import nat
import argparse
import configparser
import logging
import os


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




ip= Pyro4.socketutil.getIpAddress("localhost", workaround127=True, ipVersion=None)

# ip2= Pyro4.socketutil.getInterfaceAddress("eth0")

logger.info("Trying to bind daemon on ip ", ip)
#Pyro4.config




#self.localhost  = 127.0.0.1
# self.remotehost = remoteHost
# TODO enable at some point nat detection
# IGD = Internet Gateway Device
nat_port = None
nat_host = None

# natd = nat device ?!
natd = nat.Nat.look_for_nat()
if natd:
	logger.info("NAT detected")
	# make a Pyro daemon, port=0 => random port

	nat_port = 4242
	nat_host = natd.getExternalIp()

# daemon=Pyro4.Daemon( host="192.168.1.102", port=4242, natport=4242,nathost="82.121.111.63")
daemon=Pyro4.Daemon( port= config['pyro'].getint("daemon_port"), natport=nat_port, nathost=nat_host, host=ip)


# register the greeting object as a Pyro object
localhost = host.Host("server.ini")
uri=daemon.register(localhost)


# # find the name server
if config['pyro'].getboolean("use_nameserver"):
	ns=Pyro4.locateNS( host=ip, port=config['pyro'].getint("ns_port") )

	# register the object with a name in the name server
	ns.register("host", uri)

print ("Registered host:",uri)
print ("Ready.")
daemon.requestLoop()                  # start the event loop of the server to wait for calls


# Pyro4.Daemon.serveSimple(
#         {
#             warehouse: "example.warehouse"
#         },
#         ns = True)


if __name__ == '__main__':

	parser = argparse.ArgumentParser(
		description='Run a Pyro4 server, sharing objects with remote scripts'
	    )
	parser.add_argument('config', type=str,  default="tests.ini", help="Config filename. Describe experiment settings")

	# should give the opportunity to override settings
	parser.add_argument('localhost', action="store",help="local ip or hostname")

	parser.add_argument('remotehost', action="store",help="remote ip or hostname")
	# define it into config file for now
	# parser.add_argument('remoteport', action="store",type=int, help="ssh port ? in order to launch server")


	subparsers    		  = parser.add_subparsers(dest="nat", help='sub-command help')
	nat_parser = subparsers.add_parser('external_ip',help='external IP or associated hostname')
	# tcpwithoutlisp_parser.add_argument('remotehost', action="store",help="ip or hostname")
	nat_parser.add_argument('external_port', action="store",type=int, help="port")


	#there must be at most one ?
	
