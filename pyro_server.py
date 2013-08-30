# saved as greeting.py
import Pyro4
import host

# why the object ?
# class GreetingMaker(object):
#     def get_fortune(self, name):
#         return "Hello, {0}. Here is your fortune message:\n" \
#                "Tomorrow's lucky number is 12345678.".format(name)

# greeting_maker=GreetingMaker()

host=Host("server.ini")

daemon=Pyro4.Daemon()                 # make a Pyro daemon
ns=Pyro4.locateNS()                   # find the name server
uri=daemon.register(host)   		  # register the greeting object as a Pyro object
ns.register("host", uri)  			  # register the object with a name in the name server

print ("Ready.")
daemon.requestLoop()                  # start the event loop of the server to wait for calls