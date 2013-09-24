

class Interface:

	def __init__(self, name, ip, netmask, gw ):
		self._name = name
		self.ip = ip
		self.netmask = netmask
		self.gw = gw


	def __repr__(self):
		return "%s %r (ip=%r/netmask=%r, gw=%r, )" % (
			self.__class__.__name__, self._name, self.ip , self.netmask, self.gw)


