import isix.service.daemon as service
from isix.linux import fd
import logging, subprocess

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








class CompilableProgram(Program):

	# TODO build(target)
	# capability to add targets
	# need_root
	def __init__(self,command, need_root, srcFolder, make_all, make_install=None):
		
		super().__init__(command,need_root )
		
		self._src = srcFolder
		self._build = make_all

		self._install = make_install 
		# self._targets = {
		# 	'install' : 
		# 	'all'
		# }

	def launch_target(self, targetName):
		#subprocess.call()
		pass

	def install(self):
		pass

	def clean(self):
		pass

	def build(self):
		# subprocess.check_call(
		#, shell=True
		subprocess.check_call( self._build  )
		
		# subprocess.check_call("make -C "+ self.src +" all platform=router", shell=True);
