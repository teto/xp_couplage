#!/usr/bin/python3
import mptcp
import lispmob

import configparser
import argparse
import sys
import os
# import inspect
import subprocess
import linux
import Pyro4


class Interface:
    def __init__(self):
        pass

# en fait pourl'instant cette commande on s'en moque
# we should be able to add ability to the host 
# every ability should be self documented 
class Host:
    #, port
    def __init__(self, configFile):
        # self.address = address
        self.config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )

        # set variable MainDir in config file
        self.config.set("DEFAULT", "MainDir", os.path.realpath( os.path.dirname(__file__) ))

        # first need to compile module
        self.config.read(configFile)


        self.router = lispmob.LISPmob( self.config['lispmob']['src'], self.config['lispmob']['bin'], self.config['lispmob']['config'])

        self.mod = linux.InstalledModule( self.config['module']['name'] )

        self.lisp_daemon = lispmob.LISPdaemon( self.config['daemon']['src'], self.config['daemon']['bin'])
        #self.port 

    def getEID(self):
        return self.config["network"]["eid"]

    def getIp(self):
        return Pyro4.socketutil.getIpAddress("localhost", workaround127=True, ipVersion=None)

    # TODO should use pyroute2 
    # or libnl python wrapper 
    def getInterfaces(self):
        pass


    """ ping timeouts after 3 sec"""
    def ping(self, remotehost):
        return (os.system("ping -w 3 "+ remotehost ) == 0)

    """ for testing purposes """
    def echo(self,msg):
        print(msg)


    def mptcp_set_state(self,state):
        return mptcp.MPTCP.set_global_state(state)

    # should check if it's in its abilities
    # def __call__():

    def lispmob(self,action):
        return getattr(self.router,action)();

    def daemon(self,action):
        print ("daemon subparser:", action );
        #daemon = lispmob.Program();
        # special usecase
        if action == "compile":
            cmd = "{1}/build.sh {2} {1} {0}".format(
                        self.config['daemon']['bin'],
                        self.config['daemon']['src'],
                        self.config['kernel']['src']) 
            return subprocess.check_call( cmd ,shell=True)
        else:
            return getattr(self.lisp_daemon,action)();



        #     
            
        # elif action == "load":
        #     return subprocess.check_call("sudo "+ self.config['daemon']['bin'])
        # else:
        #     #
        #     return os.system("sudo killall -r lig_daemon*)")

    def module(self,action):

        print("Handling module with action:" + action);

        
        if action == "compile":
            kernel = linux.KernelSource( self.config['kernel']['src']);
        
            kernel.compile_module( self.config['module']['src'])
            kernel.install_module( self.config['module']['src'])
        elif action == "load":
            self.mod.load()
        else:
            self.mod.unload()

        print ("Module loaded ", self.mod.is_loaded())



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
    daemon_parser.add_argument('action', choices=('compile','start','stop'), action="store")
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
    # lispmob_parser.set_defaults(func=handle_lispmob)


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