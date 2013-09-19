#!/usr/bin/python3
import configparser
import argparse
import sys
import logging

# call it core or common
import isix.host as host
import isix.linux.core as linux
import isix.linux.module
import isix.network.mptcp as mptcp
import isix.core
import time
# import lispmob

logger = logging.getLogger( __name__ )
logger.setLevel(logging.DEBUG)




# raise NotImplementedError
# TODO move the parser here
# in case script is called directly
if __name__ == '__main__':

	args = isix.core.parse_cli( sys.argv[1:])
	# first need to compile module
	# config.read(args.config_file)
	# TODO complete absolute path towards config file
	host = host.Host( args.config_file )
	# print("webfs cfg", host["webfs"] )
	host["test"].start()
	time.sleep(10)
	# getattr(host, args.mode)( args.action)
