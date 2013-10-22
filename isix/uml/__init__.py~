import logging,sys
import sys
 
# print ("dir ", logging.__file__)

__version__ = "0.1a"
__author__ = "Matthieu Coudron"
__date__ = "2012-Sep-04"


__all__ = ["module", "network"]
# sys.path +=__path__
# TODO
#name, defaults=None, disable_existing_loggers=True
# logging.fileConfig("isix")

# setup isix logger
isixLogger = logging.getLogger("isix")

ch = logging.StreamHandler()

formatter = logging.Formatter( '${levelname} (${name}): ${message}', style='$' )
ch.setFormatter ( formatter )
isixLogger.addHandler(ch)
