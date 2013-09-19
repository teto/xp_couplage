import logging
import threading
import os


#isix.logging.
def build_from_ini( name ):
	# logger= logging.getLogger(name)
	# logger
	pass






# A mettre dans un Process donc bof
class StreamToLogger(object):
	"""
	Fake file-like stream object that redirects writes to a logger instance.
	"""
	def __init__(self, logger, log_level=logging.INFO):
		self.logger = logger
		self.log_level = log_level
		self.linebuf = ''

	def write(self, buf):
		for line in buf.rstrip().splitlines():
			self.logger.log(self.log_level, line.rstrip())


class LogPipe(threading.Thread):

	def __init__(self, level):
		"""Setup the object with a logger and a loglevel
		and start the thread
		"""
		threading.Thread.__init__(self)
		self.daemon = False
		self.level = level
		self.fdRead, self.fdWrite = os.pipe()
		self.pipeReader = os.fdopen(self.fdRead)
		self.start()

	def fileno(self):
		"""Return the write file descriptor of the pipe
		"""
		return self.fdWrite

	# si j'utilise des select ici , ca permettrait d'éviter une race condition
	def run(self):
		"""Run the thread, logging everything.
		"""
		print("local logger:",logger)
		print("self.daemon:", self.daemon)
		logger.setLevel( logging.DEBUG)
		for line in iter(self.pipeReader.readline, ''):
			logger.log(self.level, line.strip('\n'))
			# print("test")

		self.pipeReader.close()

	def close(self):
		"""Close the write end of the pipe.
		"""
		os.close(self.fdWrite)
		

# logging.basicConfig(
#    level=logging.DEBUG,
#    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
#    filename="out.log",
#    filemode='a'
# )



# 
# class MultiProcessingLogListener(logging.handlers.QueueListener):
	
# 	def __init__(self):
# 		pass




# # This is a handler
# # http://stackoverflow.com/questions/641420/how-should-i-log-while-using-multiprocessing-in-python/894284#894284
# class MultiProcessingLogHandler(logging.Handler.QueueHandler):
	
# 	# Expects a 
# 	def __init__(self, handler, queue):
# 		logging.Handler.__init__(self)

# 		self._handler = handler
# 		self.queue = queue


		# we only want one of the loggers to be pulling from the queue.
		# If there is a way to do this without needing to be passed this
		# information, that would be great!
		# if child == False:
		# 	self.shutdown = False
		# 	self.polltime = 1
		# 	t = threading.Thread(target=self.receive)
		# 	t.daemon = True
		# 	t.start()

	# def setFormatter(self, fmt):
	# 	logging.Handler.setFormatter(self, fmt)
	# 	self._handler.setFormatter(fmt)

	# def receive(self):
	# 	#print "receive on"
	# 	while (self.shutdown == False) or (self.queue.empty() == False):
	# 		# so we block for a short period of time so that we can
	# 		# check for the shutdown cases.
	# 		try:
	# 			record = self.queue.get(True, self.polltime)
	# 			self._handler.emit(record)
	# 		except Queue.Empty, e:
	# 			pass

	# def send(self, s):
	# 	# send just puts it in the queue for the server to retrieve
	# 	self.queue.put(s)

	# def _format_record(self, record):
	# 	ei = record.exc_info
	# 	if ei:
	# 		dummy = self.format(record) # just to get traceback text into record.exc_text
	# 		record.exc_info = None  # to avoid Unpickleable error

	# 	return record

	# def emit(self, record):
	# 	try:
	# 		s = self._format_record(record)
	# 		self.send(s)
	# 	except (KeyboardInterrupt, SystemExit):
	# 		raise
	# 	except:
	# 		self.handleError(record)

	# def close(self):
	# 	time.sleep(self.polltime+1) # give some time for messages to enter the queue.
	# 	self.shutdown = True
	# 	time.sleep(self.polltime+1) # give some time for the server to time out and see the shutdown

	# def __del__(self):
	# 	self.close() # hopefully this aids in orderly shutdown when things are going poorly.
