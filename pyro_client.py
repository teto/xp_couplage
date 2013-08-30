# saved as client.py
import Pyro4
import sys

# passer

# name=input("What ? ").strip()
# nameserver hostname
hostname= "192.168.1.102:4242"
host=Pyro4.Proxy("PYRONAME:host@"+hostname)    
# use name server object lookup uri shortcut

#
#print ( greeting_maker.get_fortune(name) )
host.echo("hello world")
host.daemon("compile")