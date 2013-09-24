import yaml

def loadVM(configFile):
	pass

# def build_initramfs()

class UMLVM:

	def __init__(self,config):
		self._rootfs = None
		self._kernel = None

	def setKernel(self, kernel):
		self._kernel = kernel

	def setRootfs(self,rootfs):
		self._rootfs = rootfs

	# def prepare

	# need to setup tuntap
	def launch(self):
		# TODO setup tuntaps
		pass
