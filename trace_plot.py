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

args = parser.parse_args( [ sys.argv[1] ] )


# TODO draw with error bars

print("conf",args.config_file )

# config.set("DEFAULT", "MainDir", mainDir )

config.read_file( args.config_file )

# name plots to draw
plots= config["general"]["draw"].split(' ')
for plot in plots:
	# TODO check a section exists
	print("plot", plot )
	#argparse.FileType('r')
	parser.add_argument( plot,  type=str, help=config[plot]["legend"] )


args = parser.parse_args( sys.argv[1:] )

print("This program aims at creating a gnuplot script with embedded data")

# TODO need to get 

resultsFilename= "/home/teto/xp_couplage/results/tcpwithoutlisp_1509_2118.csv"
# TODO use numpy to load data
# np.array
# names = True reads column names from data
res = np.loadtxt( resultsFilename, dtype=None, comments="#"
		#, names=True
		, delimiter=","
		)

fileSizes = res[0,]
print("file sizes:\n", fileSizes)

res= res[1:,]
print("Loaded results:\n", res)

# res.reshape( (3,3))
mean = res.mean()



# 

# returns indices
# ligne/colonne
# arange(x) generate a flat array of x entries starting from 0 to x-1

def getHighestRowResults( arr):
	# temp = np.arange(3)
	# indices = res.argmax( axis=0)
	# print("max", indices, arr[indices, temp] )
	# return arr[ arr.argmax( axis=0), np.arange(3) ] 
	return arr.max(axis=0)


def getLowestRowResults( arr):
	# temp = 
	# indices = 
	# return arr[ arr.argmin( axis=0), np.arange(3) ] 
	return arr.min(axis=0)

def getAverageRowResults( arr ):
	return arr.mean(  axis=0)


avg = getAverageRowResults ( res)
minValues = getLowestRowResults ( res)
maxValues = getHighestRowResults ( res)

print("mean", avg )
print("min",  minValues )
print("high", maxValues )

# errors relative to data set
yerr= maxValues- avg, avg-minValues
print("Compute xerr, yerr",yerr)



# generate linear spaces
x= res[0,]
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False)

# linewidth=2.0,names=("lol","plop")


#x, y, yerr=None, xerr=None, fmt='-', ecolor=None, elinewidth=None, capsize=3, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None, hold=None, **kwargs)
p1 = plt.errorbar(
			fileSizes,
			# x, 
			y=avg, 
			yerr=yerr, 
# 			xerr=None, 
# 			fmt='-', 
# 			ecolor=None, 
# 			elinewidth=None, 
# 			capsize=3, 
# 			barsabove=False, 
# 			lolims=False, 
# 			uplims=False, 
# 			xlolims=False, 
# 			xuplims=False, 
# 			errorevery=1, 
# 			capthick=None, 
# 			hold=None, 
# 			#**kwargs
			)

p1 = plt.plot(  res[0,] , "b") 
#, legend="Hello world"
p2 = plt.plot( res[1,],"r", label="red" )
plt.legend([p1, p2], ["Sinus", "Cosinus"])


plt.title("Mon titre")
plt.title(config["general"]["title"])
plt.xticks( fileSizes)
# plt.yticks()
plt.xlabel("hello world")
# plot.xlabel(config["general"]["xlabel"])
# plot.ylabel(config["general"]["ylabel"])

plt.legend(loc='upper left')
plt.show()

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
