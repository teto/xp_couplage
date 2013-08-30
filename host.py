#!/usr/bin/python3
import mptcp
import lispmob

import configparser
import argparse
import sys
import os
import inspect
import linux
# faire des do_ssh
# can be local or remote
# class LocalHost:


# class RemoteHost:


# commands= {
# 'enable_mptcp'
# }







#
# en fait pourl'instant cette commande on s'en moque
# we should be able to add ability to the host 
# every ability should be self documented 
class Host:
    #, port
    def __init__(self, configFile):
        # self.address = address
        self.config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )

        # set variable MainDir in config file       
        self.config.set("DEFAULT", "MainDir", os.path.realpath( os.path.dirname(__file__))  )

        # first need to compile module
        self.config.read(configFile)


        self.router = lispmob.LISPmob( self.config['lispmob']['src'], self.config['lispmob']['bin'], self.config['lispmob']['config'])

        self.mod = linux.InstalledModule( self.config['module']['name'] )

        self.lisp_daemon = lispmob.LISPmob( self.config['daemon']['src'], self.config['daemon']['bin'])
        #self.port 

    def lispmob(self,action):
        return getattr(self.router,action)();

    def daemon(self,action):
        print ("daemon subparser:", action );
        #daemon = lispmob.Program();

        if action == "compile":
            return subprocess.check_call( self.config['daemon']['src'] + "/build.sh",shell=True)
        elif action == "load":
            return subprocess.check_call("sudo "+ self.config['daemon']['bin'] + "&")
        else:
            #
            return os.system("sudo killall -r lig_daemon*)")

    def module(self,action):

        print("Handling module with action:" + action);

        
        if action == "compile":
            kernel = linux.KernelSource( config['kernel']['src']);
        
            kernel.compile_module( config['module']['src'])
            kernel.install_module( config['module']['src'])
        elif action == "load":
            self.mod.load()
        else:
            self.mod.unload()

        print ("Module loaded ", self.mod.is_loaded())

 #    def run(self,cmd):
 #        #raise Exception("Not implemented yet")
 #        # setup.py must be in path
 #        #do_ssh( self.address, "setup.py " + cmd)
 #        pass

 #    def start_lispmob(self):
 #        self.run("lispmob load")

 #    def stop_lispmob(self):
 #        self.run("lispmob unload")

 #    def load_module(self):
 #        print("Loading module")
 #        self.run("module load")

 #    def unload_module():
 #        print("Unloading module")
 #        self.run("module unload")

 #    def set_mptcp_state(self,state):
 #        self.run("mptcp enable")

	# def load_daemon(self):
 #        self.run("daemon load")


	# def unload_daemon(self):
	# 	self.run("daemon unload")



	# def set_mptcp_state(self,state):
	# 	self.command("mptcp")



# class LocalHost(Host):
# 	def __init__(self):
# 		Host.__init__(self, 127.0.0.1)
# 	#def 

# class RemoteHost(Host):
# 	def __init__(self, address, port):
# 		self.address = address
# 		self.port 

#	def command(self,cmd):
		#do_ssh(cmd)


# def handle_daemon( args):
#     print ("daemon subparser:", args.action );
#     #daemon = lispmob.Program();

#     if args.action == "compile":
#         return subprocess.check_call(config['daemon']['src'] + "/build.sh",shell=True)
#     elif args.action == "load":
#         return subprocess.check_call("sudo "+ config['daemon']['bin'] + "&")
#     else:
#         #
#         return os.system("sudo killall -r lig_daemon*)")



# def handle_module( args ):

#     print("Handling module with action:" + args.action);

#     module = linux.InstalledModule( config['module']['name'])
#     if args.action == "compile":
#         kernel = linux.KernelSource( config['kernel']['src']);
    
#         kernel.compile_module( config['module']['src'])
#         kernel.install_module( config['module']['src'])
#     elif args.action == "load":
#         module.load()
#     else:
#         module.unload()

#     print ("Module loaded ", module.is_loaded())


# def handle_lispmob(args):

#     print("Lispmob action:", args.action)
#     # src dir / config file
#     router = lispmob.LISPmob( config['lispmob']['src'], config['lispmob']['config'])

#     if args.action == "compile":
#         router.build()
#     elif args.action == "load":
#         router.start()
#     else:
#         router.stop()


# raise NotImplementedError
# TODO move the parser here
# in case script is called directly
if __name__ == '__main__':
    
    # run tests
    parser = argparse.ArgumentParser(
        #description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
        description='Will run tests you precise'
        )

    #there must be at most one ?
    parser.add_argument('config_file', choices=(
                                  'server.ini',
                                  'client.ini',
                                  # 'tests',
                                  # 'daemon', 
                                  # 'module',
                                  # 'kernel'
                                  # 'mptcp'
                                  ), 
                      help="Choose")

    subparsers    = parser.add_subparsers(dest="mode", help='sub-command help')
    daemon_parser = subparsers.add_parser('daemon',help='daemon help')
    daemon_parser.add_argument('action', choices=('compile','load','unload'), action="store")
    # daemon_parser.set_defaults(func=handle_daemon)

    module_parser = subparsers.add_parser('module', help='module help')
    module_parser.add_argument('action', choices=('compile','load','unload') )
    # module_parser.set_defaults(func=handle_module)



    # all params get passed to mptcp.py ?
    # mptcp_parser  = subparsers.add_parser('mptcp', help='tests help')
    # mptcp_parser.add_argument('params',nargs="*")

    # generate choices from available methods
    #print ( "sys.module" ,sys.modules["lispmob"].__class__)
    # print ( "dir" ,dir (lispmob.lispmob) )
    # # print ( "test:",  lispmob.lispmob.__dir__() )
    # lisp_choices = members = inspect.getmembers( lispmob.lispmob, inspect.ismethod);
    # print( 'lisp_choices', lisp_choices )

    lispmob_parser  = subparsers.add_parser('lispmob', help='tests help')
    lispmob_parser.add_argument('action', 
        choices=('build','start','stop','is_running') 
        # choices=lisp_choices
        )
    lispmob_parser.set_defaults(func=handle_lispmob)


    # parse arguments
    args = parser.parse_args( sys.argv[1:] )



    # config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )

    # set variable MainDir in config file       
    # config.set("DEFAULT", "MainDir", os.path.realpath( os.path.dirname(__file__))  )

    # first need to compile module
    # config.read(args.config_file)
    host = Host( args.config_file )

    getattr(host, args.mode)( args.action)
    #