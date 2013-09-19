import logging
import argparse



logger = logging.getLogger("isix.network")

# setup logger
def get_network_parser( ):

	parser = argparse.ArgumentParser(
		description='Will run tests you precise'
	)

	# parser = subparsers.add_parser('module',help='module help')
	# 
	# parser.add_argument('name')

	# # TODO build the list of choice from a class
	# parser.add_argument('action', choices=(
	# 							'compile','load','unload','is_loaded'
	# 							) 
	# 					)

	return parser