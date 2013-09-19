#!/usr/bin/python3
import logging,subprocess
import shlex
import select
import multiprocessing 
import os
import fcntl
import time

from isix.log import core
from isix.linux import fd
# setup default logger used by any daemon

# def call_program

# by default logger should be getLogger("isix.daemon")

# readline/readlines are blocking
# readline expects at least one byte before returning
# readlines expect an EOF which only happens on program exit (for a pipe)
# subprocess.communicate also expects EOF

#





def listen_to_fds(logger, proc):
	print("Started running program with id", proc.pid )

	print("Inside poll", proc.poll( ) )
	# returns resultcode if finshed, None otherwise
	while proc.poll() is None:
		print("program still running", proc.returncode)
		# sys.stderr.read()
		data = proc.stdout.read()
		if data:
			print("Data", data)
		time.sleep(1)
		# self.logger.log(logging.INFO, lines)

	print("last check", proc.returncode )





def call_thread(cli,logger,**kwargs):

	cli_args = shlex.split(cli)

	proc = subprocess.Popen(
			cli_args
			# ,stdout=devnull
			,stdout=subprocess.PIPE 
			,stderr=subprocess.PIPE
			# ,universal_newlines=True
			# ,bufsize=0
			# ,close_fds=False
			)

	print("Proc poll", proc.poll( ) )
	# when I start this the pipes get closed ?
	fd.set_fd_as_nonblocking( proc.stdout )
	fd.set_fd_as_nonblocking( proc.stderr )

	# TODO could use select here 
	while proc.poll() is None:
		# print("program still running", proc.returncode)
		# sys.stderr.read()
		# returns a byte array
		data = proc.stdout.read()
		if data:
			# print("Data", data)
			logger.log(logging.INFO, data.decode().rstrip() )
		data = proc.stderr.read()
		if data:
			# print("Data", data)
			logger.error( data.decode().rstrip() )
		time.sleep(0.1)

	proc.wait()


# different version
def create_process(cli, stdoutlogger=None, stderrlogger=None ):
	
	logger = logging.getLogger("isix.daemon")

	pipe2 = multiprocessing.Process( 
		target=call_thread,
		#logger
		args=( cli , logger  )
		)

	# pipe2.daemon = True
	# pipe2.start()
	return pipe2


# TODO use mp.Value to 
# once start is called then there is a fork and values can vary
# between the 2 objects
class SelectBasedListener(multiprocessing.Process):

	def __init__(self,logger,proc):

		super().__init__(
			# target=self.run,args=()

			)

		self.proc = proc
		self.logger = logger
		print("Start Inside poll", self.proc.poll( ) )


	# I May have a flush to add somewhere !
	def run(self):
		print("Started running program with id", self.proc.pid )
		# print("From Process: proc fds", self.proc.stdout, " " , self.proc.stderr)
		proc = self.proc

		print("Inside poll", self.proc.poll( ) )
		# returns resultcode if finshed, None otherwise
		 # is None
		while proc.poll() is None:
			print("program still running", proc.returncode)
			# sys.stderr.read()
			data = proc.stdout.read()
			if data:
				print("Data", data)
			# time.sleep(1)
			# self.logger.log(logging.INFO, lines)

		print("last check", self.proc.returncode )

		# self.check_io() # check again to catch anything after the process exits
		# print("last check io finished. Waiting")
		

	# def run(self):
	# 	# If the process does not terminate after timeout seconds, a TimeoutExpired exception will be raised.
	# 	while True:
	# 		stdout, stderr = self.proc.communicate()







# def call(cli, stdoutlogger=None, stderrlogger=None ):

# 	# TODO even if we pass a logger name 
# 	# we should prepend isix.daemon
# 	logger = logging.getLogger("isix.daemon")
# 	cli_args = shlex.split(cli)


# 	# If close_fds is true, all file descriptors except 0, 1 and 2 will be closed before the child process is executed.
# 	proc = subprocess.Popen(
# 			cli_args
# 			# ,stdout=devnull
# 			,stdout=subprocess.PIPE 
# 			,stderr=subprocess.PIPE
# 			# ,universal_newlines=True
# 			# ,bufsize=0
# 			# ,close_fds=False
# 			)

# 	print("Proc pooll", proc.poll( ) )
# 	# when I start this the pipes get closed ?
# 	set_fd_as_nonblocking( proc.stdout )
# 	set_fd_as_nonblocking( proc.stderr )
# 	# print("Proc pooll", proc.poll( ) )
# 	# print("proc fds", proc.stdout, " " ,proc.stderr)
# 	# print("messages", proc.stdout.readline() )

# 	pipeListener = SelectBasedListener(logger,proc)

# 	pipe2 = multiprocessing.Process( 
# 		target=listen_to_fds,
# 		args=( logger, proc )
# 		)
# 	# print("Proc pooll", proc.poll( ) )
# 	# # to kill thread on program exit
# 	pipeListener.daemon = True
# 	pipeListener.start()
# 	# print("Proc pooll", proc.poll( ) )
# 	# # time.sleep(10)


# 	while proc.poll() is None:
# 		print("program still running", proc.returncode)
# 		# sys.stderr.read()
# 		data = proc.stdout.read()
# 		if data:
# 			print("Data", data)
# 		time.sleep(1)















	# return proc.wait()


		# def selectBasedListener():
	# 	# TODO should check pipe states

	# def check_io(self):
	# 	#
	# 	# 1st parameter is the sequence of files we wanna read from
	# 	# 2nd files we wanna write to
	# 	# 3rd is a special parameter
	# 	# last parameter is timeout
	# 	ready_to_read = select.select([self.proc.stdout, self.proc.stderr], [], [], 1000)[0]

	# 	print("logger used", self.logger)

	# 	for io in ready_to_read:
	# 		lines = io.readlines()
	# 		# TODO change level according to fd
	# 		self.logger.log(logging.INFO, lines)
			 
	