import isix.service.daemon as service
from isix.linux import fd
import logging, subprocess
import multiprocessing
from isix.service import daemon
import os

logger = logging.getLogger("isix")

# TODO add a logger for compilation purpose only

SUDO_CMD="/usr/bin/sudo "
MAKE = "usr/bin/make"




#
# start/stop
# 
class Program:

	# subclass
	class Target:

		#blocking=True,stdoutLogger=None, stderrLogger=None,daemon=False
		def __init__(self, program, command, need_root=False):
			self._need_root = need_root
			self._command = command
			self._program = program

		def __call__(self,**kwargs):
			print("Target called:", self._command )
			pass

		def getCommand(self,raw=False):
			if raw:
				return self._command

			return self._program._update_target(self._command)

		def launch(self,blocking=True,stdoutLogger=None, stderrLogger=None,daemon=False):
			# format the command 
			command = self.getCommand()
			
			proc = daemon.create_process(command,stdoutLogger,stderrLogger)
			if daemon:
				proc.daemon= True

			proc.start()
			if blocking:
				proc.join()



	"""
	Need_root
	"""
	# TODO start command , stop is optional
	# command,need_root=False
	# root_directory
	def __init__(self,name,targets=None):

		logger.debug("Creating program named [%s]"% name )
		self._dict = {
			"sudo": SUDO_CMD,
			"make": MAKE
		}
		self._name = name
		self._targets = {}
		for targetName, command in targets.items():
			self.add_target( targetName, command)
		# self._command = command
		# self._sudo = SUDO_CMD if need_root else ""


	def __repr__(self):
		# add available targets
		return "isix.program: %s"%self._name

	# check for targets, pass on arguments
	# def __call__(self):
		
	# only used when attribute not found
	# works for targets
# __getattribute__ hook. There is also the __getattribute__() hook, which is called (if defined) for both exisitng and non-exisitng attributes. If __getattribute__() is called and doesn't raise AttributeError then __getattr__() is not called. If __getattribute__() raises AttributeError then __getattr__ gets another change to save the day.

	def __getattr__(self, item):
		
		"""Maps values to attributes.
		Only called if there *isn't* an attribute with this name
		"""
		print("Start getattr")
		try:
			return self._targets[item]
		except KeyError:
			raise AttributeError(item)

	"""
	Block 
	"""
	# def start(self,blocking=True,stdoutLogger=None, stderrLogger=None,daemon=False):

	# 	#
	# 	# logger.warning("Not implemented: Starting program")
	# 	# returns a mp.Process
	# 	logger.info("Launching %s"% self._command)
	# 	process = service.create_process( self._command )
	# 	# if daemon:
	# 	process.daemon = daemon
	# 	process.start()
	# 	if blocking:
	# 		process.join()
	

	# self._dict.update()


	# TODO rename
	def _update_target(self, command):
		# Use ** to unpack dictionary
		# print("dict", self._dict )
		try:
			return command.format( **self._dict )
		except KeyError as e:
			logger.error("Absent key [%s] in %s's dict [%s]"%(e, self._name,self._dict ) )
			return command

	# Passer un param need root
	def add_target(self,name,command):
		self._targets[name] = self.Target(self,command)

	# def remove_target(self,target):
	# 	self._targets.remove(target)

	# TODO returns a process
	# expects dictionary
	def launch_target(self, targetName):
		# subprocess.call()
		target = self._targets.get(targetName)
		if not target:
			logger.error("Unregistered target [%s]"%targetName)
			return False

		target.launch()
		# self._launch_command(cmd)


	# def _launch_command(self, command):
	# 	proc = create_process(command)
	# 	proc.start()


	# def __repr__(self):	
	def list_targets(self,raw=False):
		result = "Targets:\n"
		for name,target in self._targets.items():
			
			# command =  if raw else command
			result +=  name + ":" + target.getCommand(raw) + "\n"
			

		return result

# class Command:
	



# need_root by default
# class InstallTarget(Target):



class BuildSystem:
	pass

# BuildSystem
# class CompilableProgram(Program):

# 	# TODO build(target)
# 	# capability to add targets
# 	# need_root qualifies the command
# 	# TODO pass the build system
# 	#, make_all, make_install=None
# 	def __init__(self,command, need_root, srcFolder):
		
# 		super().__init__(command,need_root )
# 		if not os.path.isdir(srcFolder):
# 			raise Exception( srcFolder + " is not a directory")

# 		# self.src_dir = src_dir
# 		self._dict = {
# 			"srcFolder" : srcFolder
# 		}
		# self._src = 

		# TODO check srcFolder exists
		# self._build = make_all

		# self._install = make_install 
		# self._targets = {
		# 	'install' : 
		# 	'all'
		# }


	# def install(self):
	# 	pass

	# def clean(self):
	# 	pass

	# def build(self):
		# subprocess.check_call(
		#, shell=True
		# subprocess.check_call( self._build  )
		
		# subprocess.check_call("make -C "+ self.src +" all platform=router", shell=True);

# """
# available jobs,target
# """
# class CompilableByMake(CompilableProgram):


# 	#command, need_root, 
# 	def __init__(self,srcFolder):

# 		super().__init__("", False, srcFolder)
# 		self._jobs = 1
# 		self._dict.update(
# 		# self._dict = 
# 			{
# 				"program": MAKE,
# 				"jobs": 1
# 			}
# 		)

# 		self.add_target("all", "make -C ${srcFolder} -j${jobs} all" )
# 		self.add_target("clean","make -C ${srcFolder} -j${jobs} clean" )
		
# 		self.set_jobs( multiprocessing.cpu_count() )


# 	"""
# 	Matches make -j 
# 	"""
# 	def set_jobs(self,jobs):
# 		self._jobs = int(jobs)


	# def launch_target(self,targetName):
	# 	# needs to format the command
	# 	#srcFolder=self._src, jobs=self._jobs
	# 	cmd = self._targets.get(targetName)
	# 	if not cmd:
	# 		logger.error("Unregistered target [%s]"%targetName)
	# 		return False

	# 	cmd = cmd.format()
	# 	# should launch commabnd
	# 	self._launch_command(cmd)



# if __name__ == "__main__":
# 	pass