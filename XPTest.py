#!/usr/bin/python

import linux
import tempfile
import mptcp
import lispmob

#
#
#	echo "iperf -c mptcp.info.ucl.ac.be -t 20"
#	echo "$HOME/xp_couplage/wget_test.sh 153.16.49.120:8000/xpfiles temp 3"
# should also create remote and local hosts
class XPTest:
	#name = property()
	
	#client = config['lispmob']['src']
	#server = config['lispmob']['src']

	def __init__(self, name, localhost, remotehost):
		self.name = name
		self.localhost  = localhost
		self.remotehost = remotehost

		
		# TODO creer les hotes ICI
		# enable_mptcp, enable_lispmob
		#self.
		#plutot un host que l'on doit creer 
		self.module = linux.InstalledModule( config['module']['name'] )
		self.lispmob = lispmob.LISPmob( config['lispmob']['src'],config['lispmob']['config'] )
		MPTCP.set_global_state(enable_mptcp)
		if enable_lispmob:
			lispmob.launch();





	def check_connectivity():
		# TODO localhost.check_connectivity( remotehost )
		return subprocess.call("ping ") ;

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
		super( __class__.__name__, self).__init__(self, __class__.__name__, False, True )
		

	def prepare(self):
		MPTCP.disable();
		LISPmob.enable()

	



class TCPWithoutLISP(XPTest):
	def __init__(self):
		super( __class__.__name__, self).__init__(self, __class__.__name__, True, False )
		


class MPTCPWithLisp(XPTest):
	
	def __init__(self):
		super( __class__.__name__, self).__init__(self, __class__.__name__, True, True )
		



class MPTCPWithoutLISP(XPTest):
	pass


# TODO we should have a test to check Lispmob load balancing behavior
