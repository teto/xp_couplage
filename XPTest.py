#!/usr/bin/python3

import linux
import tempfile
import mptcp
import lispmob


# TODO replace with external libraries such as Fabric or paramiko or spur etc...
# ServerAliveInterval X sends information every X sec to keep the connection alive
# ServerAliveCountMax X tells the client to kill the connection after X timeouts
# port might be optional ? , port
# host can be 127.0.0.1
def do_ssh(host, cmd):
	# TODO retrieve return value
    #return os.system("ssh -o ServerAliveInterval=10 -o ServerAliveCountMax=2 -p "+port+" root@127.0.0.1 \""+cmd+"\"")
    output = subprocess.check_output("ssh -o ServerAliveInterval=10 root@"+host+" \""+cmd+"\"; echo $?")
    return output 

def do_ssh_back(host, cmd):
    #return os.system("ssh -o ServerAliveInterval=10 -o ServerAliveCountMax=2 -p "+port+" root@127.0.0.1 "+cmd)
    return os.system("ssh -o ServerAliveInterval=10 -o ServerAliveCountMax=2 root@"+host+" "+cmd +" echo $?")


# used to download files
def do_scp(host, rem, loc):
    return os.system("scp root@"+host+":"+rem+" "+loc)



def 

#	echo "iperf -c mptcp.info.ucl.ac.be -t 20"
#	echo "$HOME/xp_couplage/wget_test.sh 153.16.49.120:8000/xpfiles temp 3"
# should also create remote and local hosts
class XPTest:
	#name = property()
	
	#client = config['lispmob']['src']
	#server = config['lispmob']['src']

	# hosts should be instances of RemoteHost
	def __init__(self, name,  remotehost, enable_lisp, enable_mptcp):
		self.name = name
		#self.localhost  = 127.0.0.1
		self.remotehost = remoteHost

		
		# TODO creer les hotes ICI
		# enable_mptcp, enable_lispmob
		#self.
		#plutot un host que l'on doit creer 
		# self.module = linux.InstalledModule( config['module']['name'] )
		# self.lispmob = lispmob.LISPmob( config['lispmob']['src'],config['lispmob']['config'] )
		# MPTCP.set_global_state(enable_mptcp)
		if enable_lisp:
			self.localhost.start_lispmob();
		else:
			self.localhost.stop_lispmob();

		local ( command )
		remote( command )

	# run a command locally
	def local(self, cmd):
		do_ssh("127.0.0.1", cmd );

	def remote(self, ):
		pass

	# run a command remotely


	# def download_file():
	def check_connectivity(self):
		# TODO localhost.check_connectivity( remotehost )
		return os.system("wget  --timeout 3 -O -  "+ self.remotehost.address +" > /dev/null")
		#return subprocess.call("ping ") ;

	# should be called from each child 
	# before launching tests
	def prepare(self):
		return check_connectivity();


	# after launching tests
	def launch(self):
		# should launch a run 

		return True;




class TCPWithLISP(XPTest):
	def __init__(self):
		super( ).__init__(self, __class__.__name__, False, True )
		

	# def prepare(self):
	# 	self.remotehost.set_mptcp_state(False);
	# 	self.localhost.enable()

	



class TCPWithoutLISP(XPTest):
	def __init__(self):
		super().__init__(self, __class__.__name__, False, False )
		


class MPTCPWithLisp(XPTest):
	
	def __init__(self):
		super().__init__(self, __class__.__name__, True, True )
		



class MPTCPWithoutLISP(XPTest):
	pass


# TODO we should have a test to check Lispmob load balancing behavior



def run_tests(settings_file, remote_ip, args):

	#if args.run_tests:
	print("Using settings from ", settings_file, )
	print("TEsts run with remote host :", remote_ip )

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
		test.process_results()


# run tests
parser = argparse.ArgumentParser(
    #description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
    description='Will run tests you precise'
    )

#there must be at most one ?
# type = FileType("w")
parser.add_argument('config_file', help="Describe experiment settings")
parser.add_argument('remote_ip', help="IP of the other host of the experiment")


# if __name__ == '__main__':
# tests_parser  = subparsers.add_parser('tests', help='tests help')
parser.add_argument('tests',choices=('TCPWithoutLISP'), nargs="+", help='list of tests, their ')
# tests_parser.set_defaults(func=run_tests)


# parse arguments
args = parser.parse_args( sys.argv[1:] )


run_tests( args.config_file, args.remote_ip, args.tests )