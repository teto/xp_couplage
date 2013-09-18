import logging
# import sys
 
__version__ = "0.1"
__author__ = "Matthieu Coudron"
__date__ = "2012-Sep-04"
 
# sys.path +=__path__


# setup isix logger
isixLogger = logging.getLogger("isix")

ch = logging.StreamHandler()
isixLogger.addHandler(ch)