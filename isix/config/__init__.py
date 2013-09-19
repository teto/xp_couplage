import logging


logger = logging.getLogger("isix.loader")

# logger.basicConfig
ch = logging.StreamHandler()


# formatter = logging.Formatter( '${levelname} (Loader):  ${message}', style='$')
# ch.setFormatter (   formatter ) 

logger.addHandler( ch )