#!/usr/bin/python3
import configparser
import sys
import argparse
import os
import io
import logging
from isix.service import program

# import 
# import file


logger = logging.getLogger("isix.loader")


logger.setLevel( logging.DEBUG )


class Loader:
	def __init__(self):
		pass

	def loadHost(self,):
		pass

	@staticmethod
	def loadUMLVM(self,):
		pass

	# def load_program_section():
	# 	pass

	# configparser.NoOptionError

# def load_interface(section):
# 	logger.warning("load_interface not implemented")
# 	pass


# sectionCallbacks = {
# # 'logger' :  isix.log.build_from_ini
# # logging.basicConfig
# 'program' : load_program_section,
# 'program.compilable' : load_compilable_program_section,
# # TODO could add 'program.compilable(program.compilable.make)'
# # ou bien program.compilable.make
# 'network.interface' : load_interface
# # 'program.compilable': 
# }



def main():
	parser = argparse.ArgumentParser(
			description='Test isix loading utility'
			)

	#argparse.FileType('r')
	parser.add_argument('config', action="store", type=argparse.FileType('r'), help="Config file")

	# should give the opportunity to override settings
	args = parser.parse_args( sys.argv[1:] )

	loadConfigFile(args.config)





if __name__ == '__main__':
	main()