#!/usr/bin/python3
# import mptcp


import configparser
import argparse
import sys
import os
import netlink as nl
import netlink.route.link as nl_link
import netlink.route.address as nl_addr

# import inspect
import subprocess

import Pyro4
import logging
import io

# call it core or common
from .linux import kernel as linux_core
# from .config import ini as loader
# from .config import yaml_ as loader
from .config import loader as loader
from .linux import module as linux_module
from .network import mptcp as mptcp


logger = logging.getLogger( "isix" )
logger.setLevel(logging.DEBUG)


def getInterfaceIP(if_name):
	# eth = nl_link.get(if_name)
	# print( eth )

	cache = nl_addr.AddressCache()
	cache.refill()

	for addr in cache:
	    if addr.label == "lispTun0":
	        return (addr.local)

	return None


# en fait pourl'instant cette commande on s'en moque
# we should be able to add ability to the host 
# every ability should be self documented 
class Host:
	#, port

	# @staticmethod
	def __getitem__(self,name):
		return self._programs[ name ]

	# def __getattr__(self,name):

	# config might be of several types
	def __init__(self, config):

		# configLoader = loader.createLoader(config)

		self._programs, self.config = loader.loadConfigFile( config )
		# self.config = config

	# define to launch server
	# def __enter__(self):
	# def __exit__(self):

	# TODO use LIBnl
	def getEID(self):
		if_name = "lispTun0"
		addr = getInterfaceIP( if_name )
		# tun = nl_link.get(if_name)

		if not addr:
			logger.debug("Could not retrieve link for interface [%s]"%if_name)
			return self.getIp()	

		return addr
		# if self.router.is_running():
			# return self.config["network"]["eid"]
		

	# Don't use it.
	def getRLOC(self):
		# if not self.router.is_running():
		return self.getIp()

	def getIp(self):
		# return "127.0.0.1"
		# TODO use my libnl there
		return Pyro4.socketutil.getIpAddress("localhost", workaround127=True, ipVersion=None)

	# TODO should use pyroute2 
	# or libnl python wrapper 
	def getInterfaces(self):
		pass


	def getWebfsUrl(self):
		# print ( "webfs port" , self.config["webfs"]["port"] )
		# return "http://"+ str(self.getEID() ) + ":" + str( self.config["webfs"]["port"] )
		# print("self EID", self.getEID() )
		# print("Webfs port", self.config["webfs"]["port"] )
		return "http://{host}:{port}".format( host=self.getEID(), port=self.config["webfs"]["port"])


	""" ping timeouts after 3 sec"""
	def ping(self, remotehost,timeout=None):
		timeout = timeout if timeout else 1
		return subprocess.check_call( [ "ping","-w",str(timeout),remotehost])
		# return (os.system("ping -w 2 "+ remotehost ) == 0)

	""" for testing purposes """
	def echo(self,msg):
		print(msg)


	def mptcp_set_state(self,state):
		logger.info("changing mptcp state to :%s"%state)
		return mptcp.set_global_state(state)

	# should check if it's in its abilities
	# def __call__():


# raise NotImplementedError
# TODO move the parser here
# in case script is called directly
if __name__ == '__main__':
	
	# run tests
	parser = argparse.ArgumentParser(
	#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
	description='Will run tests you precise'
	)

	#there must be at most one ?
	parser.add_argument('config_file', 
				type=argparse.FileType('r'),
		# choices=(
		# 		  'server.ini',
		# 		  'client.ini',
		# 		  ), 
			  help="Choose")

	subparsers	  = parser.add_subparsers(
			dest="mode", help='sub-command help',
			title='Subcommands'
			)
	daemon_parser = subparsers.add_parser('daemon',help='daemon help')
	daemon_parser.add_argument('action', choices=('compile','start','stop'), action="store")
	# daemon_parser.set_defaults(func=handle_daemon)

	module_parser = subparsers.add_parser('module',help='module help')
	module_parser.add_argument('action', choices=('compile','load','unload','is_loaded') )
	# module_parser.set_defaults(func=handle_module)

	kernel_parser = subparsers.add_parser('kernel', help='module help')
	kernel_parser.add_argument('action', choices=('compile','install') )

	# all params get passed to mptcp.py ?
	# mptcp_parser  = subparsers.add_parser('mptcp', help='tests help')
	# mptcp_parser.add_argument('params',nargs="*")

	# generate choices from available methods
	#print ( "sys.module" ,sys.modules["lispmob"].__class__)
	# print ( "dir" ,dir (lispmob.lispmob) )
	# # print ( "test:",  lispmob.lispmob.__dir__() )
	# lisp_choices = members = inspect.getmembers( lispmob.lispmob, inspect.ismethod);
	# print( 'lisp_choices', lisp_choices )

	lispmob_parser  = subparsers.add_parser('lispmob', help='tests help')
	lispmob_parser.add_argument('action', 
	choices=('build','start','stop','is_running') 
	# choices=lisp_choices
	)
	# lispmob_parser.set_defaults(func=handle_lispmob)


	# parse arguments
	args = parser.parse_args( sys.argv[1:] )



	# config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )

	# set variable MainDir in config file	
	# config.set("DEFAULT", "MainDir", os.path.realpath( os.path.dirname(__file__))  )

	# first need to compile module
	# config.read(args.config_file)
	# TODO complete absolute path towards config file
	host = Host( args.config_file )

	# getattr(host, args.mode)( args.action)
