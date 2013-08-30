#!/usr/bin/python3
from __future__ import with_statement
#import unittest
import Pyro4.utils.flame
import Pyro4.utils.flameserver
import Pyro4.errors
#from testsupport import *

with Pyro4.core.Daemon() as d:
    #self.assertRaises(Pyro4.errors.SecurityError, Pyro4.utils.flame.start, d) # default should be disabled
    Pyro4.config.FLAME_ENABLED=True
    Pyro4.utils.flame.start(d)
    #Pyro4.config.FLAME_ENABLED=False
    #self.assertRaises(Pyro4.errors.SecurityError, Pyro4.utils.flame.start, d)


