#!/usr/bin/python
import os;
import subprocess;
import string;

# TODO 
# define RunningKernel 
#

class KernelSource:
	
	def __init__(self, src_dir):
		if not os.path.isdir(src_dir):
			raise Exception( src_dir + " is not a directory")
		self.src_dir = src_dir
		self.arch= "x86_64" # by default

	#def set_arch() /get_arch

	def compile_module(self, module_dir ):
		# if not os.path.isdir(module_dir):
		# 	raise Exception( src_dir + " is not a directory")
		#M= 
		return subprocess.check_call("make -C "+ self.src_dir + " M="+module_dir, shell=True)
		#return CompiledModule 


	def install_module( self , module_dir ):
		return subprocess.check_call("sudo make -C "+ self.src_dir + " M="+module_dir +" modules_install ", shell=True)


	def install_modules( self ):
		
		return subprocess.check_call("sudo make -C "+ self.src_dir + " modules_install ", shell=True)
		#return False



class LoadedKernel:
	#def __init__(self):

	def version():
		return subprocess.check_output("uname -v", shell=True);


#
# Assumes module is installed and compiled
# 
#class CompiledModule:
class InstalledModule:

	# should be statique
	#KDIR=""
	# fullpath
	def __init__(self, name):
		self.name = name;
		# self.src  = src_dir
	
	def load(self):
		return subprocess.check_call("sudo modprobe " + self.name, shell=True)
		#return False

	def for_kernel(self):
		return subprocess.check_output("modinfo "+ self.name +" -F vermagic | cut -d' ' -f1", shell=True);

	def is_loaded(self):
		output = subprocess.check_output("lsmod", shell=True).decode();
		return  os.path.basename ( self.name) in  output

	def unload(self):
		if not self.is_loaded():
			print("Module not loaded");
			return True;

		return subprocess.check_call("sudo rmmod " + self.name , shell=True);
		


# TODO
#class InstalledModule():


#
# need to be run as a sudo
# 
class Ftrace:

	debugFolder="/sys/kernel/debug/tracing"

	def __init__(self):
		# todo check ftrace was compiled into current kernel
		self.test= "hello"

	def add_to_filter(filter):
		os.system(" echo "+ filter +" >> "+ debugFolder +"/set_ftrace_filter");


	def start(command, graph):
		#echo 0 > "$debugFolder/tracing_on"
		# run command subprocess.call()
		# then stop
		return False;


	def stop():
		os.system("echo 0 > "+ debugFolder + "/tracing_on");
		return False;

