#!/usr/bin/python3

import subprocess
import os
import logging

logger = logging.getLogger( __name__ )



# represents an instance of a program, is associated to its pid
# TODO need to provide full path or  env $PATH as an argument ?
class Program:
	# absolute 
	def __init__(self, binary, need_root):
		
		if need_root:
			self.sudo = "/usr/bin/sudo "
		else:
			self.sudo = ""

		# self.src = src_dir
		self.bin = binary
		self.process = None;

	# in case there are additionnal commands
	# by default will launch programs in background
	def start(self, cmd_line="", background=True):
		#
		self.process = subprocess.Popen( self.sudo + self.bin + cmd_line )
		if background:
			return self.process.poll()
			# subprocess.check_call( ,shell=True)
		else:
			# self.pid = subprocess.
			return self.process.wait( )

	def get_bin_name(self):
		return os.path.basename( self.bin);

	#
	def is_running(self):
		# check if process exists with registered PID ?
		if self.process:
			return self.process.poll()
		return False;

		# output = subprocess.check_output("ps -e", shell=True).decode();
		# result = self.get_bin_name() in  output
		# #print ('Is ', self.bin, " running ?",result )
		# return  result

	def get_pid(self):
		if self.is_running():
			return self.process.pid
		else:
			return False;

	#
	def stop(self):
		# we don't care if it fails
		if self.is_running():
			return self.process.kill()
			#os.kill(pid, sig)
		else:
			logger.info ("Program '"+ self.bin +"'' not running")
		return True
		# if not self.is_running():
		# 	
		# 	return True

		# return subprocess.check_call( self.sudo + "killall -9 "+ self.get_bin_name() ,shell=True)



# need to pass srcd_ir
# class BuildableProgram(Program):
#

# TODO pass targets associated with install, make etc...
# class BuildableViaMake(BuildableProgram):



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
		# need root True
		super().__init__( bin, False )
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
	# def start(self):
	# 	# -D to run in background
	# 	#subprocess.check_call( "sudo "+ self.src + "/lispd/lispd -D -f "+ self.config,shell=True)
	# 	return super().start( " -f "+ self.config)

	# def is_running(self):
	# 	output = subprocess.check_output("ps -e ", shell=True).decode();
	# 	return  os.path.basename ( "lispd") in  output

	# def stop(self):
	# 	# we don't care if it fails
	# 	if not self.is_running():
	# 		print ("Lispmob not running")
	# 		return True

	# 	subprocess.check_call( "sudo killall -9 lispd ",shell=True)
