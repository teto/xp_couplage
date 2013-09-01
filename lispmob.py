#!/usr/bin/python3

import subprocess
import os
import logging

logger = logging.getLogger( __name__ )

#
# TODO to finish
class Program:
	# absolute 
	def __init__(self, binary, need_root):
		
		if need_root:
			self.sudo = "sudo "
		else:
			self.sudo = ""

		# self.src = src_dir
		self.bin = binary


	# in case there are additionnal commands
	def start(self,cmd_line):
		# 
		subprocess.check_call( self.sudo + self.bin + cmd_line ,shell=True)

	def get_bin_name(self):
		return os.path.basename( self.bin);

	#
	def is_running(self):
		output = subprocess.check_output("ps -e", shell=True).decode();
		result = self.get_bin_name() in  output
		#print ('Is ', self.bin, " running ?",result )
		return  result

	#
	def stop(self):
		# we don't care if it fails
		if not self.is_running():
			logger.info ("Program '"+ self.bin +"'' not running")
			return True

		return subprocess.check_call( self.sudo + "killall -9 "+ self.get_bin_name() ,shell=True)





#
# Allow control over lispmob
# 
class LISPdaemon(Program):


	def __init__(self, src_dir, binary ):
		super().__init__(binary, False)
		if not os.path.isdir(src_dir):
			raise Exception( src_dir + "is not a directory");

		self.src = src_dir
		

	def build(self):
		logging.info("Building daemon")
		# subprocess.check_call("make -C "+ self.src +" all platform=router",shell=True);
		subprocess.check_call( self.src +"/build.sh", shell=True);

#config_file
	# def start(self):
	# 	# 
	# 	return super.start( "-D -f "+ self.config)
		#subprocess.check_call( "sudo "+ self.src + "/lispd/lispd -D -f "+ self.config,shell=True)

	# def is_running(self):
	# 	output = subprocess.check_output("ps -e ", shell=True).decode();
	# 	return  os.path.basename ( "lispd") in  output

	# def stop(self):
	# 	# we don't care if it fails
	# 	if not self.is_running():
	# 		print ("Lispmob not running")
	# 		return True

	# 	subprocess.check_call( "sudo killall -9 lispd ",shell=True)


#
# Allow control over lispmob
# 
class LISPmob(Program):


	def __init__(self, src_dir, bin, config_file):
		# need root
		super().__init__( bin, True)
		# Program.__init__
		if not os.path.isdir(src_dir):
			raise Exception( src_dir + "is not a directory");

		# self.bin = bin
		self.src = src_dir
		self.config = config_file

		# check binary present, otherwise build
		if not os.path.isfile( self.bin ):
			self.build()

	#
	# def __dir__():
	# 	return ('build', 'start' )


	def build(self):
		print("Building LISPmob")
		subprocess.check_call("make -C "+ self.src +" all platform=router", shell=True);

#config_file
	def start(self):
		# 
		#subprocess.check_call( "sudo "+ self.src + "/lispd/lispd -D -f "+ self.config,shell=True)
		return super().start( " -D -f "+ self.config)

	# def is_running(self):
	# 	output = subprocess.check_output("ps -e ", shell=True).decode();
	# 	return  os.path.basename ( "lispd") in  output

	# def stop(self):
	# 	# we don't care if it fails
	# 	if not self.is_running():
	# 		print ("Lispmob not running")
	# 		return True

	# 	subprocess.check_call( "sudo killall -9 lispd ",shell=True)
