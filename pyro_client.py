# saved as client.py
import Pyro4
import sys

# passer

# name=input("What ? ").strip()
# nameserver hostname

# #
#
#NS running on 192.168.1.102:4242 (192.168.1.102)
#internal URI = PYRO:Pyro.NameServer@192.168.1.102:4242
#external URI = PYRO:Pyro.NameServer@82.121.111.63:4242
ip="82.121.111.63"
port=4243
hostname= ip + ":" + str(port)
ns=Pyro4.naming.locateNS( host=ip,port=port )

#ns=Pyro4.Proxy("PYRO:Pyro.NameServer@82.121.111.63:424")    
#host=Pyro4.Proxy("PYRO:obj_a62ace2aeb7749968234033597d4a6db@82.121.111.63:4242")    
#host=Pyro4.Proxy("PYRO:obj_ddc3dc5aa75043d99f72902b7c0d5eee@82.121.111.63:4242")

host= Pyro4.Proxy("PYRONAME:host@"+hostname);
# use name server object lookup uri shortcut
#print(ns)
#print ( greeting_maker.get_fortune(name) )
host.echo("hello world")
host.daemon("compile")
