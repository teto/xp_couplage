import os 


def shell_call(cmd,root=False):
	cmd = "sudo "+cmd if root else cmd
	os.system(cmd)