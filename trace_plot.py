#!/usr/bin/python3
import argparse
import csv
import numpy as np
import matplotlib.pyplot as plt
import configparser
import argparse
import sys

# TODO it 

# expects a plot script and data files

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )



parser = argparse.ArgumentParser(
	#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
	description='Will run tests you precise'
	)

#there must be at most one ?
parser.add_argument('config_file', type=argparse.FileType('r') ,
	# choices=[
	# 		  "graph1.ini"
	# 		  # 'client.ini',
	# 		  ], 
		  help="Choose")

args = parser.parse_args( )


# TODO draw with error bars

print("conf",args.config_file )

# config.set("DEFAULT", "MainDir", mainDir )

config.read_file( args.config_file )

# name plots to draw
plots= config["general"]["draw"].split(' ')
for plot in plots:
	# TODO check a section exists
	print("plot", plot )
	parser.add_argument( plot, help=config[plot]["legend"] )


args = parser.parse_args( sys.argv[1:] )

print("This program aims at creating a gnuplot script with embedded data")

# TODO need to get 

resultsFilename= "/home/teto/xp_couplage/results/tcpwithoutlisp_1409_0059.data"
# TODO use numpy to load data
res = np.loadtxt( resultsFilename, comments="#", delimiter=" " )

print(res)


mean = np.mean( res, axis=0)
print("mean", mean)


# 
indices = res.argmax( axis=0)
# returns indices
# ligne/colonne
# arange(x) generate a flat array of x entries starting from 0 to x-1
temp = np.arange(3)
print("max", indices, res[indices, temp]   )

# generate linear spaces
x=np.linspace(-5,5,100)


# linewidth=2.0,names=("lol","plop")
plot.xlabel("File size")
plot.ylabel("Time")
p1 = plot.plot(  res[0,] , "b") 
#, legend="Hello world"
p2 = plot.plot( res[1,],"r", label="red" )
plot.legend([p1, p2], ["Sinus", "Cosinus"])
plot.title("Mon titre")
# plot.xticks()
# plot.yticks()
plot.legend(loc='upper left')
plot.show()

# with open( resultsFilename, 'r', newline='') as csvfile:

# 	print("creating CSV reader")
# 	# TODO use DictWriter instead
# 	resultReader = csv.reader(csvfile, delimiter=' ', quoting=csv.QUOTE_NONE)
# 	print("CSV reader created")
# 	for row in resultReader:
		# print("row",row)
	# resultWriter = csv.DictWriter(csvfile,fieldnames= fileSizes , delimiter=' ',
	# 	quotechar='|', quoting=csv.QUOTE_MINIMAL)


					# resultWriter.writerow(results)


	# TODO move that elsewhere, leave it to a script for instance
				# # sort it to make it easier
				# results.sort()
				# # append at the end the results
				# # add average/min/max at the end
				# computedValues.append( math.fsum(results)/ results.len() )
				# computedValues.append(  results.min() )
				# computedValues.append(  results.max() )
				# # prepend filesize
				# # result.insert(0, currentSize)
				# # TODO would be better to prepend
				# results.append( computedValues )
				# # result.insert(1,average)
				# # result.insert(2,minimum)
				# # result.insert(3,maximum)
