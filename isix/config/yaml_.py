#!/usr/bin/python3
# named so to prevent collusions with pyyaml
import configparser
import sys
import argparse
import os
import io
import logging
from ..service import program as isprog
from ..network import interface as isnet
from ..uml import core as ixuml
import yaml


logger = logging.getLogger("isix.loader")


logger.setLevel( logging.WARNING )



	# configparser.NoOptionError

def load_interface(section):
	logger.warning("load_interface not implemented")
	return isnet.Interface(**section)


"""
Returns a list of UML vms
"""
def load_umlvms(configFile):

	if type(configFile) is str:
		configFile = open(configFile,"r" )
	#hasattr(fname, 'readline') seems to be a better way
	elif hasattr(configFile, 'readline'):
	# elif isinstance(configFile,  io.TextIOWrapper):
		pass

	# load_all
	vms = []
	data = yaml.load_all( configFile )
	for item in data:
		print("data",data)
		vms.append( ixuml.UMLVM(**item) )
	return vms


def load_program_section(section):
	return isprog.Program(**section)






def describe_section( section ):
	pass

sectionCallbacks = {
# 'logger' :  isix.log.build_from_ini
# logging.basicConfig
'vm' : load_umlvms,
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

def loadHostFromYaml(configFile):

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
	else:
		logger.error("unhandled case")



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
				module = sectionCallbacks[ sectionType ]( value )
				modName = module.getName()
				print("Module name [%s]"%modName )
				modules [modName] = module

				# logger.debug("Section taken into account by isix", elements)
				# for option,value in config.items( section ):
				# 	print("Option", option, "=", value)
			else:
				logger.warning("freestyle section")

		except KeyError as e:
			logger.error("Option [%s] unavailable , ignoring module [%s] "%(e, modName) )

	# print("programs", modules )
	return modules , config

# for compatibility reasons
# loadHostFromYamlFile = loadConfigFile



def main():
	parser = argparse.ArgumentParser(
			description='Test isix loading utility'
			)

	#argparse.FileType('r')
	parser.add_argument('config', action="store", type=argparse.FileType('r'), help="Config file")

	# should give the opportunity to override settings
	args = parser.parse_args( sys.argv[1:] )

	#load_all
	mods,extra = loadYamlFile(args.config)

	print("res" , mods["lispmob"])





if __name__ == '__main__':
	main()


