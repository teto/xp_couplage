#!/usr/bin/python3
import mptcp
import lispmob


# faire des do_ssh
# can be local or remote
# class LocalHost:


# class RemoteHost:

# commands= {
# 'enable_mptcp'


# }

def do_ssh(host, cmd):
        if kvm:
                if host == "comp1":
                        port = "8021"
                if host == "comp2":
                        port = "8022"
                if host == "comp3":
                        port = "8023"
                return os.system("ssh -o ServerAliveInterval=10 -o ServerAliveCountMax=2 -p "+port+" root@127.0.0.1 \""+cmd+"\"")
        return os.system("ssh -o ServerAliveInterval=10 root@"+host+" \""+cmd+"\"")

def do_ssh_back(host, cmd):
        if kvm:
                if host == "comp1":
                        port = "8021"
                if host == "comp2":
                        port = "8022"
                if host == "comp3":
                        port = "8023"
                return os.system("ssh -o ServerAliveInterval=10 -o ServerAliveCountMax=2 -p "+port+" root@127.0.0.1 "+cmd)
        return os.system("ssh -o ServerAliveInterval=10 root@"+host+" "+cmd)

def do_scp(host, rem, loc):
        if kvm:
                if host == "comp1":
                    return os.system("scp -P 8021 root@127.0.0.1:"+rem+" "+loc)
                if host == "comp2":
                    return os.system("scp -P 8022 root@127.0.0.1:"+rem+" "+loc)
                if host == "comp3":
                    return os.system("scp -P 8023 root@127.0.0.1:"+rem+" "+loc)
        return os.system("scp root@"+host+":"+rem+" "+loc)


class Host:
	def run(self,cmd):
		raise Exception("Not implemented yet")

	def load_module(self):
		print("Loading module")
		self.run("module load")

	def unload_module():
		print("Unloading module")
		self.run("module unload")

	def set_mptcp_state(self,state):
		self.command("mptcp")

	def load_daemon(self):
		pass


	def unload_daemon(self):
		pass


	# def set_mptcp_state(self,state):
	# 	self.command("mptcp")



class LocalHost(Host):
	def __init__():
		pass
	def 

class RemoteHost(Host):
	def __init__(self, address, port):
		self.address = address
		self.port 

	def command(self,cmd):
		#do_ssh(cmd)

