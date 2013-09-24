#!/usr/bin/python3
# import csv
# import numpy as np
import subprocess
import os
import sys
import logging
import logging.config
# import isix.logging.core as logix
import multiprocessing 
#as smp
# from multiprocessing import Process
import time
import threading
import shlex 
import sys
import yaml
import isix.service.program as prog
import isix.network.interface 
import isix.linux.kernel as kern
import isix.config.yaml_ as loader



# lisp.add_target("all", "${make} -C ${src}")
# print(lisp )
# print(lisp.list_targets() )

logger = logging.getLogger("root.test")


# class Monster(yaml.YAMLObject):
# 	 yaml_tag = u'!Monster'
# 	 def __init__(self, name, hp, ac, attacks):
# 		 self.name = name
# 		 self.hp = hp
# 		 self.ac = ac
# 		 self.attacks = attacks
# 	 def __repr__(self):
# 		 return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
# 			 self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)


if __name__ == "__main__":
	print("hello world")

	with open("vm0.yaml","r" ) as f:
		vms= loader.load_umlvms( f )

		print("%d vm loaded"%len(vms) )

		for vm in vms:
			print("VM description %r\n"%vm)

		vm = vms[0]

		print("Generated command", vm.generateCommand() )

	# with open("client.yaml","r" ) as f:
	# 	mods,config = loader.loadYamlFile(f)
		
	# 	lispmob = mods["lispmob"]
	# 	print("targets", lispmob.list_targets())
	# 	lispmob.start(stdoutLogger=logger,stderrLogger=logger)
