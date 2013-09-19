import argparse
# from . import logging as llogging
import logging


logger = logging.getLogger("isix.module")


# TODO resort to __getitem__ or override __dir__ in 
# Module class 
MODULE_ACTIONS=[ "compile", "load", "unload" ]

def get_module_parser():

	parser = argparse.ArgumentParser(
	#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
	description='practice module',
	# TODO this is important to prevent duplication of -h keyword
	add_help=False
	)

	# parser = subparsers.add_parser('module',help='module help')
	# 
	parser.add_argument('name')

	# TODO build the list of choice from a class
	parser.add_argument('action', choices=MODULE_ACTIONS
						)

	# parser.set_defaults()
	return parser