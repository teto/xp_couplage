#!/usr/bin/python3

import subprocess
import os
import logging
import logging.config
from multiprocessing import Process, Queue, Event, current_process
import random
import time
import shlex

logger = logging.getLogger( __name__ )
logger.setLevel(logging.DEBUG)


class MyHandler(object):
	"""
	A simple handler for logging events. It runs in the listener process and
	dispatches events to loggers based on the name in the received record,
	which then get dispatched, by the logging system, to the handlers
	configured for those loggers.
	"""
	def handle(self, record):
		print("MyHandler called")
		logger = logging.getLogger(record.name)
		# The process name is transformed just to show that it's the listener
		# doing the logging to files and console
		record.processName = '%s (for %s)' % (current_process().name, record.processName)
		logger.handle(record)

def listener_process(q, stop_event, configp):
	"""
	This could be done in the main process, but is just done in a separate
	process for illustrative purposes.
	This initialises logging according to the specified configuration,
	starts the listener and waits for the main process to signal completion
	via the event. The listener is then stopped, and the process exits.
	"""
	print("listener called")
	logging.config.dictConfig(configp)
	# only needs an object with an handle function
	listener = logging.handlers.QueueListener(q, MyHandler())
	listener.start()
	if os.name == 'posix':
	# On POSIX, the setup logger will have been configured in the
	# parent process, but should have been disabled following the
	# dictConfig call.
	# On Windows, since fork isn't used, the setup logger won't
	# exist in the child, so it would be created and the message
	# would appear - hence the "if posix" clause.
		logger = logging.getLogger('setup')
		logger.critical('Should not appear, because of disabled logger ...')

	stop_event.wait()
	listener.stop()



 # The listener process configuration shows that the full flexibility of
# logging configuration is available to dispatch events to handlers however
# you want.
# We disable existing loggers to disable the "setup" logger used in the
# parent process. This is needed on POSIX because the logger will
# be there in the child following a fork().
config_listener = {
'version': 1,
'disable_existing_loggers': True,
'formatters': {
'detailed': {
'class': 'logging.Formatter',
'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
},
'simple': {
'class': 'logging.Formatter',
'format': '%(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
}
},
'handlers': {
'console': {
'class': 'logging.StreamHandler',
'level': 'INFO',
'formatter': 'simple',
},
'file': {
'class': 'logging.FileHandler',
'filename': 'mplog.log',
'mode': 'w',
'formatter': 'detailed',
},
'foofile': {
'class': 'logging.FileHandler',
'filename': 'mplog-foo.log',
'mode': 'w',
'formatter': 'detailed',
},
'errors': {
'class': 'logging.FileHandler',
'filename': 'mplog-errors.log',
'mode': 'w',
'level': 'ERROR',
'formatter': 'detailed',
},
},
'loggers': {
'foo': {
'handlers' : ['foofile']
}
},
'root': {
'level': 'DEBUG',
'handlers': ['console', 'file', 'errors']
},
}


# TODO use Process method
# represents an instance of a program, is associated to its pid
# TODO need to provide full path or  env $PATH as an argument ?
class Program:
	# absolute 
	def __init__(self, binary, need_root):
		
		
		self.sudo = "/usr/bin/sudo " if need_root else ""
		
			

		# self.src = src_dir
		self.bin = binary
		self.process = None;

		# logger should be passed by construction ?
		# create one by default
		# logging.config.dictConfig(config)
		# should be a QueueHandler
		# config of the logger
		# config_worker = {
		# 'version': 1,
		# 'disable_existing_loggers': True,
		# 'handlers': {
		# 'queue': {
		# 'class': 'logging.handlers.QueueHandler',
		# 'queue': q,
		# },
		# },
		# 'root': {
		# 'level': 'DEBUG',
		# 'handlers': ['queue']
		# },
		# }
		# self.logger  = logging.config.dictConfig(config_worker)
		#logging.getLogger( self.get_bin_name() )

	# in case there are additionnal commands
	# by default will launch programs in background
	def start(self, options="", background=True, *args, **kwargs):
		
		command_line = self.sudo + self.bin + options
		logger.info("Start function: %s"% command_line)
		#
		cli_args = shlex.split(command_line)
		# works only on windows ,startupinfos=subprocess.CREATE_NEW_CONSOLE

		self.process = subprocess.Popen( cli_args , **kwargs)
		
		if background:
			return self.process.poll()
			# subprocess.check_call( ,shell=True)
		else:
			# self.pid = subprocess.
			return self.process.wait( )

	def get_bin_name(self):
		return os.path.basename( self.bin);

	#
	def is_running(self):
		# check if process exists with registered PID ?
		if self.process:
			return self.process.poll()
		return False;

		# output = subprocess.check_output("ps -e", shell=True).decode();
		# result = self.get_bin_name() in  output
		# #print ('Is ', self.bin, " running ?",result )
		# return  result

	def get_pid(self):
		if self.is_running():
			return self.process.pid
		else:
			return False;

	#
	def stop(self):
		# we don't care if it fails
		if self.is_running():
			return self.process.kill()
			#os.kill(pid, sig)
		else:
			logger.info ("Program '"+ self.bin +"'' not running")
		return True
		# if not self.is_running():
		# 	
		# 	return True

		# return subprocess.check_call( self.sudo + "killall -9 "+ self.get_bin_name() ,shell=True)



# need to pass srcd_ir
# class BuildableProgram(Program):
#

# TODO pass targets associated with install, make etc...
# class BuildableViaMake(BuildableProgram):



#
# Allow control over lispmob
# 
class LISPdaemon(Program):


	def __init__(self, src_dir, binary ):
		super().__init__(binary, False)
		if not os.path.isdir(src_dir):
			raise Exception( src_dir + "is not a directory");

		self.src = src_dir
		

	def build(self):
		logging.info("Building daemon")
		# subprocess.check_call("make -C "+ self.src +" all platform=router",shell=True);
		subprocess.check_call( self.src +"/build.sh", shell=True);

#config_file
	# def start(self):
	# 	# 
	# 	return super.start( "-D -f "+ self.config)
		#subprocess.check_call( "sudo "+ self.src + "/lispd/lispd -D -f "+ self.config,shell=True)

	# def is_running(self):
	# 	output = subprocess.check_output("ps -e ", shell=True).decode();
	# 	return  os.path.basename ( "lispd") in  output

	# def stop(self):
	# 	# we don't care if it fails
	# 	if not self.is_running():
	# 		print ("Lispmob not running")
	# 		return True

	# 	subprocess.check_call( "sudo killall -9 lispd ",shell=True)


#
# Allow control over lispmob
# 
class LISPmob(Program):


	def __init__(self, src_dir, bin, config_file):
		# need root True
		super().__init__( bin, True )
		# Program.__init__
		if not os.path.isdir(src_dir):
			raise Exception( src_dir + "is not a directory");

		# self.bin = bin
		self.src = src_dir
		self.config = config_file

		# check binary present, otherwise build
		if not os.path.isfile( self.bin ):
			self.build()

	#
	# def __dir__():
	# 	return ('build', 'start' )
	def start(self):
		stdout_fd=open("/tmp/lispmob.log","w") 
		super().start(stdin=stdout_fd,stderr=stdout_fd)

	def build(self):
		print("Building LISPmob")
		subprocess.check_call("make -C "+ self.src +" all platform=router", shell=True);

#config_file
	# def start(self):
	# 	# -D to run in background
	# 	#subprocess.check_call( "sudo "+ self.src + "/lispd/lispd -D -f "+ self.config,shell=True)
	# 	return super().start( " -f "+ self.config)

	# def is_running(self):
	# 	output = subprocess.check_output("ps -e ", shell=True).decode();
	# 	return  os.path.basename ( "lispd") in  output

	# def stop(self):
	# 	# we don't care if it fails
	# 	if not self.is_running():
	# 		print ("Lispmob not running")
	# 		return True

	# 	subprocess.check_call( "sudo killall -9 lispd ",shell=True)








def worker_process(config):
	logging.config.dictConfig(config)
	levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
	logging.CRITICAL]
	loggers = ['foo', 'foo.bar', 'foo.bar.baz',
	'spam', 'spam.ham', 'spam.ham.eggs']
	if os.name == 'posix':
	# On POSIX, the setup logger will have been configured in the
	# parent process, but should have been disabled following the
	# dictConfig call.
	# On Windows, since fork isn't used, the setup logger won't
	# exist in the child, so it would be created and the message
	# would appear - hence the "if posix" clause.
		logger = logging.getLogger('setup')
		logger.critical('Should not appear, because of disabled logger ...')

	for i in range(100):
		lvl = random.choice(levels)
		logger = logging.getLogger(random.choice(loggers))
		logger.log(lvl, 'Message no. %d', i)
	time.sleep(0.01)




if __name__ == "__main__":
	q = Queue()
	stop_event = Event()
	workers = []
	print('main')


	 # The worker process configuration is just a QueueHandler attached to the
	# root logger, which allows all messages to be sent to the queue.
	# We disable existing loggers to disable the "setup" logger used in the
	# parent process. This is needed on POSIX because the logger will
	# be there in the child following a fork().
	config_worker = {
	'version': 1,
	'disable_existing_loggers': True,
	'handlers': {
	'queue': {
	'class': 'logging.handlers.QueueHandler',
	'queue': q,
	},
	},
	'root': {
	'level': 'DEBUG',
	'handlers': ['queue']
	},
	}

	 # The main process gets a simple configuration which prints to the console.
	config_initial = {
	'version': 1,
	'formatters': {
	'detailed': {
	'class': 'logging.Formatter',
	'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
	}
	},
	'handlers': {
	'console': {
	'class': 'logging.StreamHandler',
	'level': 'INFO',
	},
	},
	'root': {
	'level': 'DEBUG',
	'handlers': ['console']
	},
	}

	logging.config.dictConfig(config_initial)
	logger = logging.getLogger('setup')
	logger.info('About to create workers ...')

	lp = Process(target=listener_process, name='listener',
		args=(q, stop_event, config_listener))
	lp.start()
	logger.info('Started listener')

	# router = LISPmob("/home/teto/lispmob","/home/teto/lispmob/lispd/lispd","/home/teto/lisp.conf")

	for i in range(5):
		wp = Process(target=worker_process, name='worker %d' % (i + 1),
		args=(config_worker,))
		workers.append(wp)
		wp.start()
		logger.info('Started worker: %s', wp.name) 	


	for wp in workers:
			wp.join()
	logger.info('Telling listener to stop ...')
	stop_event.set()
	lp.join()
	logger.info('All done.')