#!/usr/bin/python3
import socket



print (socket.if_nameindex() )
# from pyroute2 import IPRoute

# # get access to the netlink socket
# ip = IPRoute()

# # print interfaces
# print("links",ip.get_links()) 

# # stop working with netlink and release all sockets
# ip.release()