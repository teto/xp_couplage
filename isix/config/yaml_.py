#!/usr/bin/python3
# named so to prevent collusions with pyyaml
import configparser
import sys
import argparse
import os
import io
import logging
import isix.service.program as isprog
import isix.network.interface as isnet
import yaml


logger = logging.getLogger("isix.loader")


logger.setLevel( logging.WARNING )



	# configparser.NoOptionError

def load_interface(section):
	logger.warning("load_interface not implemented")
	return isnet.Interface(**section)



# def load_umlvm():


def load_program_section(section):
	return isprog.Program(**section)






def describe_section( section ):
	pass

sectionCallbacks = {
# 'logger' :  isix.log.build_from_ini
# logging.basicConfig
'program' : load_program_section,
# 'program.compilable' : load_compilable_program_section,
# TODO could add 'program.compilable(program.compilable.make)'
# ou bien program.compilable.make
'network.interface' : load_interface
# 'program.compilable': 
}


#def loadLoggerFromFile():

# TODO shoudl return a list of programs
# network objects ?
"""

return programs and config (somehow a hack)
"""
def loadYamlFile(configFile):

	# for program/compilable program
	modules = {}

	# for users sections
	userSections = {}
	
	# for unhandled sections (error ?)
	extras = {}


	if type(configFile) is str:
		configFile = open(configFile,"r" )
	#hasattr(fname, 'readline') seems to be a better way
	elif hasattr(configFile, 'readline'):
	# elif isinstance(configFile,  io.TextIOWrapper):
		pass



	config = yaml.load( configFile )


	# print("List sections")
	for sectionType, value  in config.items():

		try:
			print("Section name", sectionType)
			# elements = sectionFullname.split(' ')
			# print("Splitted", elements)

			# sectionName = elements[-1]
			# section = config[sectionFullname]
			# if len(elements) > 1:
			
			if sectionType in sectionCallbacks:
				# TODO pass sthg into parenthesis eventually
				# TODO check no duplicate 
				# 
				sectionName, val = sectionCallbacks[ sectionType ]( value )
				print("Module name ", sectionName)
				modules [sectionName] = val

				# logger.debug("Section taken into account by isix", elements)
				# for option,value in config.items( section ):
				# 	print("Option", option, "=", value)
			else:
				logger.warning("freestyle section")

		except KeyError as e:
			logger.error("Option [%s] unavailable , ignoring module [%s] "%(e, sectionName ) )

	# print("programs", modules )
	return modules , config




def main():
	parser = argparse.ArgumentParser(
			description='Test isix loading utility'
			)

	#argparse.FileType('r')
	parser.add_argument('config', action="store", type=argparse.FileType('r'), help="Config file")

	# should give the opportunity to override settings
	args = parser.parse_args( sys.argv[1:] )

	res = loadYamlFile(args.config)

	print("res" , res)





if __name__ == '__main__':
	main()