# saved as greeting.py
# IMPORTANT launch naming service beforehand
# python3 -Wignore -m Pyro4.naming --host [your ip] --port [your port]
# 
# when closed incorrectly, socket keeps opened
# netstat -pn | grep CLOSE_WAIT
# or more thorough 
# netstat -tonp
# 
import Pyro4
import host
import subprocess

# why the object ?
# class GreetingMaker(object):
#     def get_fortune(self, name):
#         return "Hello, {0}. Here is your fortune message:\n" \
#                "Tomorrow's lucky number is 12345678.".format(name)

# greeting_maker=GreetingMaker()

remoteHost=host.Host("client.ini")

ip= Pyro4.socketutil.getIpAddress("localhost", workaround127=True, ipVersion=None)
# ip2= Pyro4.socketutil.getInterfaceAddress("eth0")
ip2="null"
print("Trying to bind daemon on ip ", ip, ip2 )
#Pyro4.config


# make a Pyro daemon, port=0 => random port
daemon=Pyro4.Daemon(host=ip, port=12345)                 
ns=Pyro4.locateNS()                   # find the name server
uri=daemon.register(remoteHost)   		  # register the greeting object as a Pyro object
ns.register("host", uri)  			  # register the object with a name in the name server

print ("Registered host:",uri)
print ("Ready.")
daemon.requestLoop()                  # start the event loop of the server to wait for calls