import .interface as ixnet
import isix.core.shell as ixsh
#
# derive from isix.module ?
class TuntapInterface(ixnet.Interface):
	def __init__(self,*args):

		super().__init__(*args)
		self._name = name


	# shell_cmd() #root=True/False
	def enable(self):
		# sudo ip tuntap add mode tap user teto
		ixsh.shell_call("ip tuntap ")

	def disable(self):