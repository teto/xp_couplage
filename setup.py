#!/usr/bin/python3

# echo "For instance http://79.141.8.227:8000/xpfiles"
# echo "or http://153.16.49.120:8000/xpfiles"

import linux
import XPTest
import glob
import argparse
import sys
import os
import apt
import configparser
import lispmob
#from configparser import ExtendedInterpolation

global config



# modes= {
# "install" : 
# "compile" : 
# "load"    : 
# "unload"  : "rmmod "+lig_module+ " 2>&1" 

# }


config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )

def check_config( config_file):
	# TODO
	# check for pyroute, lispmob etc...
	return False

	#if not os.path.is_file( config_file ):






def run_tests(args):

	#if args.run_tests:

	# TODO check test exists
	for test_name in args.run_tests:
		# instantiate a test 
		members = inspect.getmembers(sys.modules["XPTest"], inspect.isclass)
		if not test_name in members:
			print("Invalid test :", test_name)
			continue

		test = test_name();
		print ("Prelaunching operations");
		if not test.prepare():
			print ( "Test '"+ test.name + "' failed")
			continue;

		test.launch()



# config.set("DEFAULT", "MainDir", os.path.realpath( os.path.dirname(__file__))  )

# first need to compile module
config.read("config.ini")


#available_tests = glob.glob("./tests/*.py")
available_tests =('TCPWithoutLISP', 'MPTCPWithLisp','MPTCPWithoutLISP')

# run tests
parser = argparse.ArgumentParser(
	#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
	description='Will run tests you precise'
	)

#there must be at most one ?
# parser.add_argument('mode', choices=(
# 								'download',
# 								'compile',
# 								'tests',
# 								'daemon', 
# 								'module',
# 								'kernel'
# 								'mptcp'
# 								), 
# 					help="Choose what mode you wanna control")

subparsers    = parser.add_subparsers(dest="mode", help='sub-command help')
daemon_parser = subparsers.add_parser('daemon',help='daemon help')
daemon_parser.add_argument('action', choices=('compile','load','unload'), action="store")
daemon_parser.set_defaults(func=handle_daemon)

module_parser = subparsers.add_parser('module', help='module help')
module_parser.add_argument('action', choices=('compile','load','unload') )
module_parser.set_defaults(func=handle_module)

tests_parser  = subparsers.add_parser('tests', help='tests help')
tests_parser.add_argument('tests',nargs="*")
tests_parser.set_defaults(func=run_tests)

# all params get passed to mptcp.py ?
mptcp_parser  = subparsers.add_parser('mptcp', help='tests help')
mptcp_parser.add_argument('params',nargs="*")

lispmob_parser  = subparsers.add_parser('lispmob', help='tests help')
lispmob_parser.add_argument('action', choices=('compile','load','unload') )
lispmob_parser.set_defaults(func=handle_lispmob)
#mptcp_parser  = subparsers.add_argument('') 
#parser.add_argument('--download',action="store_true", help="will try to install everything necessary, to the extent of download and compiling from git")
#parser.add_argument('--compile-module',action="store_true", help="recompile everything and install it")
#parser.add_argument('--module', choices=('load','unload') , action='store' , help = "Use it to load or unload kernel module" )

#parser.add_argument('--run-tests',action="store_true", help="Generate the random files that will be downloaded during the XP")
#parser.add_argument('--module', choices=('load','unload') ,action='store', dest='action' )


parser.add_argument('--prepare',action="store_true", help="Check the environment, recompile everything and install it")
parser.add_argument('--generate-files',action="store_true", help="Generate the random files that will be downloaded during the XP")

# subparser for run-test command
# we then need to know remote rloc and local rloc
#parser_a = subparsers.add_parser('run-tests', help='a help')

#parser.add_argument('--run-tests', nargs="+", choices=available_tests , help="List of tests taken from the \"tests\" subfolder");



#nargs=argparse.REMAINDER
args = parser.parse_args( sys.argv[1:] )

print ( "Chosen mode: ", args.mode  );
args.func( args )


# TO DEBUG
#print(args)

# if  args.mode == "module":
# 	handle_module( args.mode )
#if args.daemon.action:
	# module = linux.InstalledModule( config['module']['name'])
	# if args.module == "load":
	# 	module.load()
	# else:
	# 	module.unload()
	# print ("Module loaded ", module.is_loaded())

# if args.download:
# 	print('Downloading complementary files')
# 	# install libnl for
# 	# subprocess.check_call("git clone git://git.infradead.org/users/tgr/libnl.git libnl",shell=True)
# 	# ./autogen.sh
# 	# check swig and source-highlight/ascii docs are installed 
# 	# ./configure
# 	# cd python 
# 	# python setup.py build
# 	# sudo python setup.py install
# 	# install custom lispmob
# 	#"git clone "
# 	print('Finished')


# compile module and install it
# should generate files as well
if args.prepare:
	kernel = linux.KernelSource( config['kernel']['src']);
	
	kernel.compile_module( config['module']['src'])
	kernel.install_module( config['module']['src'])

	# module = linux.InstalledModule( config['module']['name'])
	# module.load();
	# print ("Module loaded ", module.is_loaded() )
	# #module.unload();
	# print ("Module loaded ", module.is_loaded() )


# will launch tests



# uname -r

# TODO need to set $MainDir
#config.set()



# will recompile module just to be sure
# need to check kernel version against module version
