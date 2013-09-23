import isix.service.daemon as service
from isix.linux import fd
import logging, subprocess
import multiprocessing
from isix.services import daemon
import os

logger = logging.getLogger("isix")

# TODO add a logger for compilation purpose only

SUDO_CMD="/usr/bin/sudo "
MAKE = "usr/bin/make"


class Program:

	"""
	Need_root
	"""
	# TODO start command , stop is optional
	def __init__(self,command,need_root=False):

		logger.debug("Creating program with command %s"%command )
		
		self._command = command
		self._sudo = SUDO_CMD if need_root else ""



	def __repr__(self):
		return "isix.program: %s"%self._command



	"""
	Block 
	"""
	def start(self,blocking=True,stdoutLogger=None, stderrLogger=None,daemon=False):

		#
		# logger.warning("Not implemented: Starting program")
		# returns a mp.Process
		logger.info("Launching %s"% self._command)
		process = service.create_process( self._command )
		# if daemon:
		process.daemon = daemon
		process.start()

		if blocking:
			process.join()




class Command:
	


class Target:

	def __init__(self, program, command, need_root=False):
		self._need_root = need_root
		self._command = command
		self._program = program

	def launch(self):
		command = self._program._update_target(self._command)
		proc = daemon.create_process(command)
		proc.start()

# need_root by default
# class InstallTarget(Target):





# BuildSystem
class CompilableProgram(Program):

	# TODO build(target)
	# capability to add targets
	# need_root qualifies the command
	# TODO pass the build system
	#, make_all, make_install=None
	def __init__(self,command, need_root, srcFolder):
		
		super().__init__(command,need_root )
		if not os.path.isdir(srcFolder):
			raise Exception( srcFolder + " is not a directory")

		# self.src_dir = src_dir
		
		self._src = srcFolder
		# TODO check srcFolder exists
		# self._build = make_all

		# self._install = make_install 
		# self._targets = {
		# 	'install' : 
		# 	'all'
		# }


	def _update_target(self, command):
		# 
		return command.format( self._dict )

	# Passer un param need root
	def add_target(self,name,command):
		self._targets["name"] = command

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
	def list_targets(self):
		for target,command in self._targets:
			print( "target name", target, "command ", command )

	# def install(self):
	# 	pass

	# def clean(self):
	# 	pass

	# def build(self):
		# subprocess.check_call(
		#, shell=True
		# subprocess.check_call( self._build  )
		
		# subprocess.check_call("make -C "+ self.src +" all platform=router", shell=True);

"""
available jobs,target
"""
class CompilableByMake(CompilableProgram):


	#command, need_root, 
	def __init__(self,srcFolder):

		super().__init__("", False, srcFolder)
		self._jobs = 1
		self._dict.update(
		# self._dict = 
			{
				"program": MAKE,
				"jobs": 1
			}
		)

		self.add_target("all", "make -C ${srcFolder} -j${jobs} all" )
		self.add_target("clean","make -C ${srcFolder} -j${jobs} clean" )
		
		self.set_jobs( multiprocessing.cpu_count() )


	"""
	Matches make -j 
	"""
	def set_jobs(self,jobs):
		self._jobs = int(jobs)


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