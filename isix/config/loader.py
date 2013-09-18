#!/usr/bin/python3
import configparser
import sys
import argparse
import os
import io
import logging
# import 
# import file

# TODO retrieve main logger 


sectionCallbacks = {
'logger' :  isix.logging.build_from_ini
# logging.basicConfig
# 'program' : 
# 'program.compilable': 
}


#def loadLoggerFromFile():


def loadConfigFile(configFile):
	config = configparser.ConfigParser(
				interpolation=configparser.ExtendedInterpolation() 
		)

	# set variable MainDir in config file
	mainDir = os.path.realpath( os.path.dirname(__file__) )
	config.set("DEFAULT", "MainDir",  mainDir )

	if type(configFile) is str:
		config.read( configFile )
	#hasattr(fname, 'readline') seems to be a better way
	elif hasattr(configFile, 'readline')
	# elif isinstance(configFile,  io.TextIOWrapper):
		config.read_file( configFile )
	else:
		print("Unhandled case")

	print("List sections")
	for section in config.sections():
		print("Section name", section)
		elements = section.split(' ')
		print("Splitted", elements)
		
		if elements[0] in sectionCallbacks:
			print("Section taken into account by isix", elements)
		else:
			print("freestyle section", elements)
		# split to detect the kind of config
		# if no kind specified than let it accessible
		# else load the object and remove the section from the config

		




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