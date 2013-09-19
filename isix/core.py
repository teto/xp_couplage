import argparse,sys

from isix.linux import *
from isix.network import natutils

logger = logging.getLogger("isix")

def parse_cli(args):

	logger.debug("Parsing command line")
	
	parser = argparse.ArgumentParser(
		#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
		description='ISIX parser. More info on http://github.com/teto/isix'
	)

	#there must be at most one ?
	parser.add_argument('config_file', 
				type=argparse.FileType('r'),
			  help="Choose the host config file")

	# parser.add_argument('action', 
	# 	choices=('program','module','network'), 
	# 	action="store"
	# 	)

	subparsers = parser.add_subparsers(dest="subparser")

	#get_module_parser() 
	module_parser = subparsers.add_parser( "module", parents=[get_module_parser() ] )

	return parser.parse_args(args)



if __name__ == "__main__":
	args = parse_cli( sys.argv[1:] )
	print("Args", args)
