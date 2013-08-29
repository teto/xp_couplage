#!/usr/bin/python3

import subprocess
import os


#
# Allow control over lispmob
# 
class LISPmob:


	def __init__(self, src_dir,config_file):
		if not os.path.is_dir(src_dir):
			raise Exception( src_dir + "is not a directory");

		self.src = src_dir
		self.config = config_file
		# check binary present, otherwise build
		if not os.path.is_file( src_dir +"/lispd/lispd"):
			build()

	def build(self):
		print("Building LISPmob")
		subprocess.check_call("make platform=router");

#config_file
	def launch(self):
		# 
		subprocess.check_call( "sudo "+ self.src + "/lispd/lispd -f "+ self.config)
