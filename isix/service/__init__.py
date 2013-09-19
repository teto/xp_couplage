import logging, logging.handlers
import multiprocessing

from isix.log import core

logger = logging.getLogger("isix.daemon")


# to dispatch al messages to subhandlers
logger.setLevel( logging.DEBUG )
logger.propagate = False

# main queue
q = multiprocessing.Queue()


# queueHandler = core.MultiProcessingLogHandler(q)
queueHandler = logging.handlers.QueueHandler(q)


# setup the queue listener which will dispatch messages to
# its handlers
consoleHandler = logging.StreamHandler()
fileHandler = logging.FileHandler('isix.daemon.log')



consoleHandler.setLevel( logging.DEBUG )
fileHandler.setLevel( logging.DEBUG)

formatter  = logging.Formatter('${levelname} (Process: ${processName}) ${message}' , style='$')
consoleHandler.setFormatter ( formatter )
#
# we can passa list to it
queueListener = logging.handlers.QueueListener(q, consoleHandler, fileHandler  )



# logger.addHandler( consoleHandler )
# logger.addHandler( fileHandler )
logger.addHandler( queueHandler )


queueListener.start()

# print("isix.daemon is available", logger)
# queueListener.join()