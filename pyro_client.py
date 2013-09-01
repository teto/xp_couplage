#!/usr/bin/python3
import Pyro4
# import sys
# import host

# passer

# name=input("What ? ").strip()
# nameserver hostname
hostname= "192.168.1.102:4242"


h=Pyro4.Proxy("PYRONAME:host@"+hostname)
# use name server object lookup uri shortcut



# 82.121.111.63
#print ( greeting_maker.get_fortune(name) )
h.echo("hello world")
h.daemon("compile")