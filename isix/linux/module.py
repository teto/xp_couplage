
import argparse
import logging


logger = logging.getLogger("isix.module")


# def parse_module( args ):

# 	parser = argparse.ArgumentParser(
# 	#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
# 	description='Will run tests you precise'
# 	)

# 	# parser = subparsers.add_parser('module',help='module help')
# 	# 
# 	parser.add_argument('name')

# 	# TODO build the list of choice from a class
# 	parser.add_argument('action', choices=(
# 								'compile','load','unload','is_loaded'
# 								) 
# 						)



class InstalledModule:

	# should be statique
	#KDIR=""
	# fullpath
	def __init__(self, bin):
		# self.name = name;
		# self.src  = src_dir
		# self.installed = 
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
		
