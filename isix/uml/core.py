import logging,os 
import shutil

def loadVM(configFile):
	pass

# def build_initramfs()

# ./mptcp_kernel initrd=./initramfs_mptcp mem=512M con0=fd:0,fd:1 xterm=urxvtc,--title,-e
# ./mptcp_kernel initrd=initramfs_mptcp init=init_client.sh  

logger = logging.getLogger("isix")




class UMLVM:
	"""
	Expects a list of interfaces
	set memory in Mb
	"""
	def __init__(self,kernel, init=None, rootfs=None, initramfs=None, interfaces=None,mem=512):
		self._rootfs = rootfs
		self._kernel = kernel
		self._init = init
		self._mem = mem
		self._initramfs = initramfs
		self.setKernel( kernel )
		self.setRootfs( rootfs )
		
		self._interfaces = interfaces

	def __str__(self):
		return "%s with kernel %s"%(self.__class__.__name__, self._kernel)

	def __repr__(self):
		return "%s with kernel %s repr"%(self.__class__.__name__, self._kernel)

	# TODO check it's for the correct arch
	def setKernel(self, kernel):
		self._kernel = kernel

	def setMemory(self,mem):
		self._mem = int(mem)

	def setRootfs(self,rootfs):
		self._rootfs = rootfs

	# def is_executable()

	"""
	Expects a list of interfaces
	"""
	def setInterfaces(self, interfaces):
		self._interfaces = interfaces

	def generateCommand(self, check=False):

		command= self._kernel

		command += " mem=%dM"%self._mem
		
		if check and not shutil.which(self._kernel):
			logger.error("Specified kernel [%s] does not exist or is not executable"%(self._kernel))

		# UML accepts interfaces with names ethXX
		for no,interface in enumerate(self._interfaces):
			command += " eth"+str(no)+"=tuntap,tap0"


		if self._initramfs:
			if os.path.isfile(self._initramfs):
				command += " initrd="+self._initramfs;
			else:
				logger.error("Specified initramfs [%s] does not exist"%(self._initramfs))

		if self._rootfs:
			if os.path.isfile(self._rootfs):
				command += " rootfs="+self._rootfs;
			else:
				logger.error("Specified rootfs [%s] does not exist"%(self._rootfs))

		return command

	

	# need to setup tuntap
	# add parameters such as enableInternet etc...
	# if autoBuild set, will build rootfs and initramfs in case they are 
	# missing ?
	def launch(self, autoBuild=True, accessWan=False):
		# TODO setup tuntaps
		# compute command line 
		# check that all elements exists
		command = self.generateCommand(check=True)
		print("Launching with  command", command)
		# command= self._kernel 

		pass
