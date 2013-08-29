#!/usr/bin/python


#import pyroute2
import SocketServer
import sys
#import pyroute2.netlink.generic
import netlink.core as netlink
import netlink.core as netlink


global LIG_FAMILY_NAME

# TODO we should be able to create a parser
# 

if len(sys.argv) > 1:


LIG_FAMILY_NAME="LIG_FAMILY"
print("Starting LIG DAEMON\n");
#print ("Hello world")


sock = netlink.Socket()
#returns itself
sock.connect(netlink.NETLINK_GENERIC)



# 2nd parameter refers to family name defined in gnl_family.name
family_id = genl_ctrl_resolve (sock, LIG_FAMILY_NAME);
if family_id < 0 :
    print("could not find family id");
    exit



print ("Family id ", family_id);


# group_id = genl_ctrl_resolve_grp (sk, LIG_FAMILY_NAME, LIG_GROUP_NAME);
# if(group_id  < 0 )
# {
#     printf("could not find group id \n");
#     goto failure;
# }

# printf("Group id:\t%d\n",group_id);


# ret = nl_socket_add_membership(sk, group_id);
# if(ret != 0)
# {
#     printf("could not register to group %d\n",group_id);
#     goto failure;
# }
# else
#     printf("successfully registered to group id:\t%d\n",group_id);
# genl_ctrl_resolve( )

# class MyTCPHandler(SocketServer.BaseRequestHandler):
#     """
#     The RequestHandler class for our server.

#     It is instantiated once per connection to the server, and must
#     override the handle() method to implement communication to the
#     client.
#     """

#     def handle(self):
#         # self.request is the TCP socket connected to the client
#         self.data = self.request.recv(1024).strip()
#         print "{} wrote:".format(self.client_address[0])
#         print self.data
#         # just send back the same data, but upper-cased
#         self.request.sendall(self.data.upper())

# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999

#     # Create the server, binding to localhost on port 9999
#     server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

#     # Activate the server; this will keep running until you
#     # interrupt the program with Ctrl-C
#     server.serve_forever()