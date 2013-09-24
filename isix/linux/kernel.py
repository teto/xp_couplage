#!/usr/bin/python
import os;
import subprocess;
import string;
import logging;

# TODO 
# define RunningKernel 
#
logger = logging.getLogger( __name__)
logger.setLevel( logging.DEBUG )


# list architectures from 
SUPPORTED_ARCHITECTURES="x86 "


# hérite de CompilableProgram ?
# TODO set O option => Output folder 
class KernelSource:
	
	def __init__(self, src_dir, arch="x86_64"):

		# self.arch= "x86_64" # by default
		# super().__init__(src_dir)
		self.set_arch(arch)
		# self._supported_architectures

		# add targets
		# add_target("all","")

	
	"""
	"""
	#,outputFolder
	def set_arch(self,arch):
		if os.path.isdir( "{srcFolder}/arch/{architecture}".format(srcFolder=self.src_dir,architecture=arch) ):
			self._arch = arch
			return True
		else:
			logger.error("Unsupported architecture")
			return False

	def get_arch(self):
		return self._arch

	# Tout ca ce sont des targets
	def compile(self):
		pass
		# return subprocess.check_call("make -C "+ self.src_dir + " -j5 all", shell=True)

	def install(self):
		pass
		# return subprocess.check_call("make -C "+ self.src_dir + " install", shell=True)

	def compile_module(self, module_dir ):
		# if not os.path.isdir(module_dir):
		# 	raise Exception( src_dir + " is not a directory")
		#M= 
		target = add_target()
		target.launch()
		# return subprocess.check_call("make -C "+ self.src_dir + " M="+module_dir, shell=True)
		#return CompiledModule 


	def install_module( self , module_dir ):
		# return subprocess.check_call("sudo make -C "+ self.src_dir + " M="+module_dir +" modules_install ", shell=True)
		pass

	# def install_modules( self ):
		
	# 	return subprocess.check_call("sudo make -C "+ self.src_dir + " modules_install ", shell=True)
	# 	#return False



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
	def __init__(self, bin):
		# self.name = name;
		# self.src  = src_dir
		self.bin = bin
	
	def get_name(self):
		return os.path.splitext ( os.path.basename( self.bin ) )[0]

	def load(self):
		#modprobe
		if self.is_loaded():
			logger.info( "Module already loaded. Unloading first...")
			self.unload()

		return subprocess.check_call("sudo insmod " + self.bin, shell=True)
		#return False

	def for_kernel(self):
		return subprocess.check_output("modinfo "+ self.bin +" -F vermagic | cut -d' ' -f1", shell=True);

	def is_loaded(self):
		print( "name", self.get_name() )
		output = subprocess.check_output("lsmod", shell=True).decode();
		return  os.path.basename ( self.get_name() ) in  output

	def unload(self):
		if not self.is_loaded():
			logger.info("Module not loaded");
			return True;

		return subprocess.check_call("sudo rmmod " + self.bin, shell=True);
		


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

	def add_to_filter(self,filter):
		os.system(" echo "+ filter +" >> "+ self.debugFolder +"/set_ftrace_filter");


	def start(self,command, graph):
		#echo 0 > "$debugFolder/tracing_on"
		# run command subprocess.call()
		# then stop
		return False;


	def stop(self):
		os.system("echo 0 > "+ self.debugFolder + "/tracing_on");
		return False;

