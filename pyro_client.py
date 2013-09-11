#!/usr/bin/python3
import Pyro4
import natutils
import pyro_server
import sys
import argparse

# import host

# passer

# name=input("What ? ").strip()
# nameserver hostname

# nat = natutils.look_for_nat()

#
#NS running on 192.168.1.102:4242 (192.168.1.102)
#internal URI = PYRO:Pyro.NameServer@192.168.1.102:4242
#external URI = PYRO:Pyro.NameServer@82.121.111.63:4242


if __name__ == '__main__' :
	
	parser = argparse.ArgumentParser(
			description='Pyro4 client. For testing purpose'
			)

	# ns_args = pyro_server.ns_cli_parser( sys.argv[1:])
	parser.add_argument('ns_host', action="store", help="nameserver ip or hostname")
	parser.add_argument('ns_port', action="store", type=int, help="nameserver port")

	# ip="192.168.1.102"
	# port=4243
	# hostname= ip + ":" + str(port)

	args = parser.parse_args( sys.argv[1:] )

	print("looking for hostname", args.ns_host )
	ns=Pyro4.naming.locateNS( host=args.ns_host, port=args.ns_port )

	#ns=Pyro4.Proxy("PYRO:Pyro.NameServer@82.121.111.63:424")    
	#host=Pyro4.Proxy("PYRO:obj_a62ace2aeb7749968234033597d4a6db@82.121.111.63:4242")    
	#host=Pyro4.Proxy("PYRO:obj_ddc3dc5aa75043d99f72902b7c0d5eee@82.121.111.63:4242")

	print("Finding uri for host")
	uri = ns.lookup( "host")
	print (" uri", uri)


# host= Pyro4.Proxy("PYRONAME:host@"+hostname);
# use name server object lookup uri shortcut
#print(ns)
#print ( greeting_maker.get_fortune(name) )
# host.echo("hello world")
# host.daemon("compile")
