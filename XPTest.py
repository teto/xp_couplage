#!/usr/bin/python3

# import linux
# import tempfile
# import mptcp
# import lispmob
import argparse
import sys
import logging
import inspect
# import host
# import nat
import configparser
import os
import subprocess
import Pyro4
# import math
import datetime
import csv
import numpy as np
import isix.host as host
import isix.experiments.SQLiteDataSet as sqlite_ds
import sqlite3 as db
import itertools
import time

# timeout before locateNS failure 
Pyro4.config.COMMTIMEOUT = 3

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

MainDir = os.path.realpath( os.path.dirname( __file__ ))


# TODO replace with external libraries such as Fabric or paramiko or spur etc...
# ServerAliveInterval X sends information every X sec to keep the connection alive
# ServerAliveCountMax X tells the client to kill the connection after X timeouts
# port might be optional ? , port
# host can be 127.0.0.1
def do_ssh(host, cmd):
	# TODO retrieve return value
    #return os.system("ssh -/o ServerAliveInterval=10 -o ServerAliveCountMax=2 -p "+port+" root@127.0.0.1 \""+cmd+"\"")
    output = subprocess.check_output("ssh -o ServerAliveInterval=10 root@"+host+" \""+cmd+"\"; echo $?")
    return output 

def do_ssh_back(host, cmd):
    #return os.system("ssh -o ServerAliveInterval=10 -o ServerAliveCountMax=2 -p "+port+" root@127.0.0.1 "+cmd)
    return os.system("ssh -o ServerAliveInterval=10 -o ServerAliveCountMax=2 root@"+host+" "+cmd +" echo $?")


# used to download files
def do_scp(host, rem, loc):
	return os.system("scp root@"+host+":"+rem+" "+loc)



def check_for_folder(dirname):
	# check if folder exists
	# dirname = "./results"
	
	if os.path.exists( dirname ):
		if os.path.isdir(dirname) :
			return True;
		else:
			return False
	# 	logging.error("Directory {0} already exists", dirname )
	# makedirs is recursive, contrary to mkdir
	elif not os.makedirs( dirname ,exist_ok=True):
		logger.error("Could not create directory '%s'"% dirname )
		return False;

	return True


# TODO we could use a pyro uri here
# to launch a naming server
#python3 -Wignore -m Pyro4.naming --host 192.168.1.102 --port 4243 --nathost=82.121.111.63 --natport 4243

#	echo "iperf -c mptcp.info.ucl.ac.be -t 20"
#	echo "$HOME/xp_couplage/wget_test.sh 153.16.49.120:8000/xpfiles temp 3"
# should also create remote and local hosts
# TODO should be able to accept a file (unifnished test) as an argument
# 
class XPTest:
	#name = property()
	
	# hosts should be instances of RemoteHost
	# **kwargs
	# for key in kwargs
	def __init__(self, name, cfg, localhost, remotehost, enable_lisp, enable_mptcp):
		
		self._name = name

		self._config = cfg
		self._localhost = localhost
		self._remotehost = remotehost

		# range start/stop/step
	
		
		# max_repeat = self.config.getint("xp","repeat")

		self._blockSize= self._config.getint("xp","blockSize")
		self._maxSize	 = self._config.getint("xp","maxFileSize")

		# replace by enable (True/False) ?
		print("enable lisp", enable_lisp)
		if enable_lisp:
			# logger.info("Please enable lispmob on both machines")
			input("Please enable lispmob on both machines")
		else:
			input("Please disable lispmob on both machines")


		# TODO check routes are ok 
		self._localhost.mptcp_set_state(enable_mptcp);
		self._remotehost.mptcp_set_state(enable_mptcp);

		# db connection
		self._db = None

	def __del__(self):
		pass
		# if self._db_con:
		# 	logger.debug("Closing connection to database")
		# 	self._db_con.close()


	# computes the filename where to register results
	def getResultsFilename(self):
		# TODO need to open the file where to register results
		now = datetime.datetime.now()
		#%Y for year , %H for hour (24h), %M for padded minute
		# rename into numpy format ?
		resultFilename = now.strftime(MainDir+"/results/"+self._name+"_%d%b_%Hh%Mm.sqlite")

		return resultFilename


	# def download_file():
	def check_connectivity(self):
		# TODO localhost.check_connectivity( remotehost )
		remotehost = self._remotehost.getEID()
		logger.info("Checking connectivity with [%s]"%remotehost)
		#os.system("wget  --timeout 3 -O -  "+ self.remotehost.address +" > /dev/null")
		return self._localhost.ping( remotehost )
		#return subprocess.call("ping ") ;


	# pass a callback , fn ?
	def generateTestFileSizes(self):
		

		# blockSize= self._config.getint("xp","blockSize")
		# maxSize	 = self._config.getint("xp","maxFileSize")
		# max_repeat = self.config.getint("xp","repeat")

		return range(blockSize, self._maxSize, self._blockSize )




	def generateTestFiles(self):
		filesFolder = self._config["xp"]["files_folder"]

		if not check_for_folder(filesFolder):
			return False

		logger.info("generating files to download for XP into %s"%filesFolder )
		# what happens if files already exist ?
		

		# maxSize	 = self.config.getint("xp","maxFileSize")
		# max_repeat = self.config.getint("xp","repeat")
		temp = self.generateTestFileSizes()
		print ("temp", temp)
		print ("block size ", self._blockSize)
		for size in temp:
			res = subprocess.call(["dd",
						"if=/dev/urandom" ,
						"of={folder}/{fileSize}.bin".format(folder=filesFolder, fileSize=size),
						# "bs=\"%dk\""%blockSize,
						"bs=%dk"%self._blockSize,
						"count=%d"%(size/self._blockSize)
						],
						# stdout=subprocess.STDOUT,
						# stderr=subprocess.STDOUT
						);
			if res:
				print("error while creating test file");
				return False

		return True






	# should be called from each child 
	# before launching tests
	def prepare(self, objectives, resume_from_results):

		# check if folder exists
		# dirname = self._config["results"]["folder"]
		# if not check_for_folder(dirname):
		# 	return False

		db_filename = self.getResultsFilename()
		if resume_from_results:
		# and os.path.isfile(resume_from_results):
			db_filename=resume_from_results

		self._db = sqlite_ds.SQLiteDataSet(db_filename)

		# TODO compare objectives with already existing results
		# 
		fileSizes = {}
		self._fileSizes = {}
		existing = self._db.getStats()
		for fileSize, count in objectives.items():
			fileSizes[ fileSize ] = count - existing.get(fileSize, 0 )

		self._fileSizes = fileSizes


		# db_connection
		# self._db_con = db.connect( db_filename )
		# self._db_con.row_factory = db.Row                # accès facile aux colonnes

		# cur = self._db_con.cursor()                             # obtention d'un curseur
		
		# # if new set of results table
		# if resume_from_results:
		# 	stats = ds.getResultStats ()

		# else:

		# 	#experiment INTEGER,
		#     cur.executescript("""
		#     CREATE TABLE IF NOT EXISTS results(
		#         filesize INTEGER,
		#         duration REAL,
		#         id INTEGER PRIMARY KEY AUTOINCREMENT
		#         );

		#     CREATE TABLE IF NOT EXISTS tcp_stats(
		#         min_rtt REAL DEFAULT 0,
		#         max_rtt REAL DEFAULT 0,
		#         avg_rtt REAL DEFAULT 0,
		#         result_id INTEGER
		#         )


		#     """)
		# if self.check_connectivity() != 0:
		# 	return False
		# self._db_con.commit()

		# return self.generateTestFiles()
		return True


	# return elapsed time
	def run_unit_test(self, fileToDownload):

		logger.info("Downloading file [%s]", fileToDownload)
		
		addressToBindTo=self._localhost.getEID()

		MAX_ATTEMPT=3
		for attempt in range(1,MAX_ATTEMPT):
			try:
				logger.info("Attempt %d out of %d possible..."%( attempt, MAX_ATTEMPT) )
				# will produce sthg like
				#/usr/bin/time -f '%e' wget -q -O /dev/null http://192.168.1.102:8000/xpfiles/1920.bin
				# be careful
				# time utility sends its output on stderr by default
				# TODO afficher la commande en mode debug
				# via string puis split[] ?
				logger.debug("Command [%s]"%"wget TODO")
				elapsedTime = subprocess.check_output(
					["/usr/bin/time", 
					"-f", # to specify format
					"%e" , # elapsed time
					"wget",
					"--bind-address=%s"%addressToBindTo,
					"--tries",
					"1",
					"--timeout",
					"1",
					 "-q",
					 "-O",
					 "/dev/null",
					 # " - ",
					 fileToDownload
					#, shell=True
					],
					stderr=subprocess.STDOUT
					);
				# append exection time.decode()
				elapsedTime = elapsedTime.decode().rstrip()
				logger.info("Result %s"% elapsedTime )
				
				return ( elapsedTime )
				# it worked so we go to next test 
				break;

			except subprocess.CalledProcessError as e:
				logger.error("Error on attempt [%d]. Error Code [%d].\nCommand [%s]\n returned [%s]\n . "%(attempt,e.returncode,e.cmd,e.output) );
				if attempt < MAX_ATTEMPT:
					logger.info("Sleep for 2 seconds")
					time.sleep(5)
					continue;
				else:
					return False


	def saveResult(self, result):
		# self._db_con
		pass


	# blockSize min/max/avg/all the results
	def launch(self):

		resultFilename = self.getResultsFilename()

		logger.info("Opening file %s"%resultFilename)



		

		# cur = self._db_con.cursor()
		for fileSize, count in self._fileSizes.items():
			
			# TODO selon lisp activé ou non, on prend l'EID ou l'IP 
			fileToDownload= ""+ self._remotehost.getWebfsUrl() +"/xpfiles/"+str(fileSize)+".bin";

			print( "[%d] iterations needed to complete results for the size [%d]"%(count, fileSize ) )
			for iteration in range(1,count+1):
				logger.info("Running unit test (%d ouf of %d) ..."%( iteration, count) )
				# fileSize = (index[1]+1) * blockSize
				# http://"+ self.remotehost.getIp()+ self.config["xp"]["files"]
				result = self.run_unit_test(fileToDownload)
				# TODO save result into DB
				# cur.execute("INSERT INTO results(filesize, duration) VALUES(?,?)", (fileSize, result) )

				self._db.addResult( fileSize, result )


		print("Results saved in [%s]"% resultFilename)
		return True;


	#it should trace a graph at least
	# def process_results(self):
	# 	pass





class TCPWithLISP(XPTest):
	def __init__(self,  cfg_file, localhost,remotehost):
		super( ).__init__( "tcpwithlisp", cfg_file,localhost, remotehost, True, False )
		





class TCPWithoutLISP(XPTest):
	def __init__(self, cfg_file,localhost,remotehost ):
		super().__init__( "tcpwithoutlisp",cfg_file,localhost, remotehost, False, False )
		


class MPTCPWithLisp(XPTest):
	
	def __init__(self,cfg_file, localhost,remotehost):
		super().__init__( "mptcpwithlisp",cfg_file,localhost, remotehost, True, True )
		



class MPTCPWithoutLISP(XPTest):
	
	def __init__(self,cfg_file, localhost,remotehost):
		super().__init__( "mptcpwithoutlisp",cfg_file,localhost, remotehost, False, True )
		



# TODO move that to isis manager
# logging facility
# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logging.warning('Protocol problem: %s', 'connection reset', extra=d)
def run_test(test_name, settings_file, localhostname, remotehostname, remoteport, simulation, resume_from_results, *extraargs, **kwargs):

	# check test exists
	logging.info("Launching test")
	# instantiate a test 
	#sys.modules["XPTest"]



	members = inspect.getmembers( sys.modules[__name__] , inspect.isclass)
	# remove second item of tupe (name,class)
	members = [ x[0] for x in members]
	# print ("members:", members)
	if not test_name in members:
		logger.error("Invalid test %s" % test_name)
		# print()
		return


	config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )

	# use nat ?
	# set variable MainDir in config file
	config.set( "DEFAULT", "MainDir", MainDir )
	config.set( "DEFAULT", "XPName", test_name )
	config.set( "DEFAULT", "hostname", remotehostname )

	# with open()
	# first need to compile module
	config.read_file(settings_file)

	# now we are sure the test name exists
	# tries to connect to pyro server
	# uri = 

	# no need for extraargs till now
	# globals()

	# TODO needs to create objects now
	# we should

	localhost = host.Host( "client.yaml" ) 
	# localhost = host.Host( "client.ini" ) 

	uri=None
	# ns = None
	if config.getboolean("pyro","use_nameserver"):
		
		ns_port = config.getint("pyro","ns_port");
		# TODO check it works
		logger.info("locating nameserver at %s %s"%(remotehostname, ns_port) )
		try:
			ns = Pyro4.locateNS( host=remotehostname, port= ns_port )
			uri = ns.lookup("host")
		except Pyro4.errors.NamingError as e:
			logger.warning("locateNS error: %s"%e)

	if not uri:	
		uri = input("Enter remote host uri:\n")

	logger.info("Using uri %s"%uri )

	# TODO handle that error case
	remotehost = Pyro4.Proxy(uri)


	#########################################################
	### Compute wanted results
	#########################################################
	blockSize= config.getint("xp","blockSize")
	maxSize	 = config.getint("xp","maxFileSize")
	repeat	 = config.getint("xp","repeat")

	# TODO generate number of keys
	# range( , maxSiz)		
	fileSizes = range(blockSize, maxSize, blockSize )
	# fileSizes = dict( itertools.zip_longest( fileSizes, fillvalue=repeat ) )
	temp = {}
	for size in fileSizes:
		temp[size] = repeat
	print("filesize", temp )
	# fileSizes = dict( list(zip( fileSizes, list(map( lambda x: repeat, fileSizes) ) ) ) )



	# instanciate test class XPTest
	# settings_file
	test = getattr( sys.modules[__name__], test_name)( config, localhost,remotehost );
	logger.info ("Prelaunching operations");
	if not test.prepare( temp, resume_from_results):
		logger.error ( "failed preparing test '"+ test.name + "' ")
		return False

	# rename to run

	
	for attempt in config["xp"]["repeat"]:

		if not test.launch():
			logger.error ( "failed running test '"+ test.name + "' ")
			break;
	# test.process_results()

	# TODO
	# do_ssh()

# TODO we should have a test to check Lispmob load balancing behavior
# move it elsewhere ?
# def run_tests(settings_file, remote_ip, args):

# 	#if args.run_tests:
# 	print("Using settings from ", settings_file, )
# 	print("TEsts run with remote host :", remote_ip )





# Avoir une queue par XP

if __name__ == '__main__':

	logger.setLevel(logging.DEBUG)
	# run tests
	parser = argparse.ArgumentParser(
	    #description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
	    description='Will run tests you precise'
	    )

	# parser.add_argument('localhost', action="store",help="local ip or hostname")
	parser.add_argument('config_file', type=argparse.FileType("r"), help="Describe experiment settings")
	parser.add_argument('remotehost', action="store",help="remote ip or hostname")
	# define it into config file for now
	# parser.add_argument('remoteport', action="store",type=int,nargs="?", help="ssh port ? in order to launch server")
	# FileType
	
	parser.add_argument('--simulate', action="store_true", help="Describe experiment settings")

	# parser.add_argument('remote_ip', help="IP of the other host of the experiment")

	# nargs="+"
	parser.add_argument('tests', choices=["TCPWithoutLISP","TCPWithLISP","MPTCPWithLISP","MPTCPWithoutLISP"], nargs=1, help='list of tests, their ')
	parser.add_argument('existing_results', nargs="?", help='Gives a previous file result you want to resume ')
	# tests_parser.set_defaults(func=run_tests)


	# parse arguments
	args = parser.parse_args( sys.argv[1:] )

	# args.config_file
	# run_tests(  )
	print("args", args)
	resumeFile = args.existing_results if args.existing_results else None

	for test_name in args.tests:
		print("test:", test_name)
		#args.remoteport,
		#def run_test(test_name, settings_file, localhostname, remotehostname, remoteport, extraargs):

		run_test( test_name, args.config_file, "localhost", args.remotehost, 0, simulation=args.simulate, resume_from_results=resumeFile)