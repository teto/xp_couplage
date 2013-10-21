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


logger.setLevel( logging.WARNING )

# TODO retrieve main logger 
# test derives de 
# test( isix.program ) lispmob
# command= 
def load_compilable_program_section( sectionName, options ):
	# start = options.get("start")
	start = options["start"]

	# TODO could be git/svn
	sourceFolder	= options.get("src")
	# make -C suivi 
	make_install	= options.get("install_cmd","make -C {src} install".format(src=sourceFolder) )
	make_all 		= options.get("build_cmd","make -C {src} all".format(src=sourceFolder) )

	# install = options.get("sources")
	# make cleans
	return program.CompilableProgram( start, sourceFolder, make_all, make_install )



# eventually pass the 
def load_program_section(sectionName, options):

	# for option in options:
	# 	print ("option" , option, "value = ", options[option] )

	# print(section)
	start = options.get("start")
	need_root = options.getboolean("need_root",False)
	# command to stop
	# stop= 
	return program.Program( start, need_root )


	# configparser.NoOptionError

def load_interface(section):
	logger.warning("load_interface not implemented")
	pass

sectionCallbacks = {
# 'logger' :  isix.log.build_from_ini
# logging.basicConfig
'program' : load_program_section,
'program.compilable' : load_compilable_program_section,
# TODO could add 'program.compilable(program.compilable.make)'
# ou bien program.compilable.make
'network.interface' : load_interface
# 'program.compilable': 
}


# TODO test the interpolation
def convert_section_to_dict(section):
	options= {}
	for option,value in section:
		# print("Option", option, "=", value)
		options[option] = value

	return options




def describe_section( section ):
	pass

#def loadLoggerFromFile():

# TODO shoudl return a list of programs
# network objects ?
"""

return programs and config (somehow a hack)
"""
def loadHostFromIni(configFile):

	# for program/compilable program
	modules = {}

	# for users sections
	userSections = {}
	
	# for unhandled sections (error ?)
	extras = {}

	config = configparser.ConfigParser(
				interpolation=configparser.ExtendedInterpolation() 
		)

	# set variable MainDir in config file
	# mainDir = os.path.realpath( os.path.dirname(__file__) )
	# config.set("DEFAULT", "MainDir",  mainDir )

	if type(configFile) is str:
		config.read( configFile )
	#hasattr(fname, 'readline') seems to be a better way
	elif hasattr(configFile, 'readline'):
	# elif isinstance(configFile,  io.TextIOWrapper):
		config.read_file( configFile )
	else:
		logger.error("Unhandled case")

	# print("List sections")
	for sectionFullname in config.sections():

		try:
			# print("Section name", sectionFullname)
			elements = sectionFullname.split(' ')
			# print("Splitted", elements)

			sectionName = elements[-1]
			section = config[sectionFullname]
			if len(elements) > 1:
				sectionType = elements[0]
				if sectionType in sectionCallbacks:
					# TODO pass sthg into parenthesis eventually
					# TODO check no duplicate 
					modules [sectionName] = sectionCallbacks[ sectionType ]( sectionName , section)

					logger.debug("Section taken into account by isix", elements)
					# for option,value in config.items( section ):
					# 	print("Option", option, "=", value)
				else:
					logger.warning("freestyle section", elements)
					
			else:
				# print("simple element", sectionName )
				# userSections[ sectionName ]
				modules [sectionName] = convert_section_to_dict( section.items() )
			# split to detect the kind of config
			# if no kind specified than let it accessible
			# else load the object and remove the section from the config
		except configparser.NoOptionError as e:
			logger.error("Option not available %s"%e )

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

	loadConfigFile(args.config)





if __name__ == '__main__':
	main()