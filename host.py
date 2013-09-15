#!/usr/bin/python3
import mptcp
import lispmob

import configparser
import argparse
import sys
import os
# import inspect
import subprocess
import linux
import Pyro4
import logging
import io

logger = logging.getLogger( __name__ )
logger.setLevel(logging.DEBUG)

class Interface:
	def __init__(self):
		pass

# en fait pourl'instant cette commande on s'en moque
# we should be able to add ability to the host 
# every ability should be self documented 
class Host:
	#, port

	# @staticmethod
	# def 

	# config might be of several types
	def __init__(self, config):
		# self.address = address
		mainDir = os.path.realpath( os.path.dirname(__file__) ) 
		logging.info("Loading file  with as default MainDir="+ mainDir)
		
		# if already loaded as a config parser instance
		# if isinstance(configFile, configparser.ConfigParser ):
		# 	logger.warning("Config should already be loaded")
		# 	self.config = config

		# else:
			# need to instantiate
		self.config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )
		# set variable MainDir in config file

		self.config.set("DEFAULT", "MainDir", mainDir )
		


		# if we gave the config filename
		if type(config) is str: 
			
			self.config.read(config)

		elif isinstance(config, io.TextIOWrapper):
			logger.info("Config file already opened")
			self.config.read_file(config)
		else:
			logger.error("Invalid filetype for config: %s"%type(config))
			return 





		# first need to compile module
		#


		self.kernel = linux.KernelSource( self.config['kernel']['src'] );

		self.router = lispmob.LISPmob( self.config['lispmob']['src'], self.config['lispmob']['bin'], self.config['lispmob']['config'])

		self.mod = linux.InstalledModule( self.config['module']['bin'])
			#,self.config['module']['src'] )

		self.lisp_daemon = lispmob.LISPdaemon( self.config['daemon']['src'], self.config['daemon']['bin'])
		#self.port 
		self.config.set("DEFAULT", "hostname", self.getEID() )

	# TODO check
	def getEID(self):
		if self.router.is_running():
			return self.config["network"]["eid"]
		return self.getIp()

	def getRLOC(self):
		# if not self.router.is_running():
		return self.getIp()

	def getIp(self):
		return Pyro4.socketutil.getIpAddress("localhost", workaround127=True, ipVersion=None)

	# TODO should use pyroute2 
	# or libnl python wrapper 
	def getInterfaces(self):
		pass


	def getWebfsUrl(self):
		return "http://"+self.getEID()+ ":"+ self.config["webfs"]["port"];


	""" ping timeouts after 3 sec"""
	def ping(self, remotehost,timeout=None):
		timeout = timeout if timeout else 1
		return subprocess.check_call( [ "ping","-w",str(timeout),remotehost])
		# return (os.system("ping -w 2 "+ remotehost ) == 0)

	""" for testing purposes """
	def echo(self,msg):
		print(msg)


	def mptcp_set_state(self,state):
		logger.info("changing mptcp state: %s")
		return mptcp.MPTCP.set_global_state(state)

	# should check if it's in its abilities
	# def __call__():

	def lispmob(self,action):
		logger.info("Lipsmob action: %s"%action )
		return getattr(self.router,action)();

	def kernel(self,action):
		return getattr(self.kernel,action)();

	def daemon(self,action):
		print ("daemon subparser:", action );
		#daemon = lispmob.Program();
		# special usecase
		if action == "compile":
			cmd = "{1}/build.sh {2} {1} {0}".format(
				self.config['daemon']['bin'],
				self.config['daemon']['src'],
				self.config['kernel']['src']) 
			return subprocess.check_call( cmd ,shell=True)
		else:
			return getattr(self.lisp_daemon,action)();



	#     
		
	# elif action == "load":
	#     return subprocess.check_call("sudo "+ self.config['daemon']['bin'])
	# else:
	#     #
	#     return os.system("sudo killall -r lig_daemon*)")

	def module(self,action):

		print("Handling module with action:" + action);

		
		if action == "compile":
			kernel = linux.KernelSource( self.config['kernel']['src']);
		
			kernel.compile_module( self.config['module']['src'])
			kernel.install_module( self.config['module']['src'])
		elif action == "load":
			self.mod.load()
		else:
			self.mod.unload()

		print ("Module loaded ", self.mod.is_loaded())



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

	module_parser = subparsers.add_parser(help='module help')
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

	getattr(host, args.mode)( args.action)
