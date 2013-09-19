# deal with file descriptors
# TODO move it to linux
import os, fcntl


def check_fd_validity(fd):
	try:
		statinfo =  os.fstat( fd )
		print("Check file descriptors status:", statinfo)
	except OSError as e:
		print("ERROR", e)





""" expects a file descriptor
can be retrieved for instance by self.proc.stdout.fileno()
"""
def set_fd_as_nonblocking(fd):
	# retrieve current configuration of the file descriptor
	try:
		fl = fcntl.fcntl(fd, fcntl.F_GETFL)
		fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
	except OSError as e:
		print("OSError",e)



class FileDescriptor:

	def __init__(self, fd):
		self._fd = fd

	# true or false
	# def set_blocking(self,value):
	#	additionnalFlag = os.O_BLOCK if value == True else os.O_NONBLOCK