#!/usr/bin/python3
import argparse
import csv
import numpy as np
import matplotlib.pyplot as plt
import configparser
import argparse
import sys
import isix.experiments.SQLiteDataSet as ds
import logging

from collections import defaultdict


logger = logging.getLogger()
logger.setLevel( logging.DEBUG )


# TODO it 
MINIMUM_SAMPLE_SIZE=0
# expects a plot script and data files

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )



parser = argparse.ArgumentParser(
	#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
	description='This program generates plots for different experiences'
	)

#there must be at most one ?
parser.add_argument('config_file', type=argparse.FileType('r') ,
		  help="Choose plot configuration file")


if len(sys.argv) < 1:
	print("Choose a graph definition file as a parameter (graph1.ini for instance)")
	exit(1)

args = parser.parse_args( [ sys.argv[1] ]  )


# TODO draw with error bars

print("Logging config file ",args.config_file )

# config.set("DEFAULT", "MainDir", mainDir )

config.read_file( args.config_file )

# name plots to draw
plotNames = config["general"]["draw"].split(' ')
for plotName in plotNames:
	# TODO check a section exists
	print("plot name: ", plotName )
	#argparse.FileType('r')
	parser.add_argument( plotName,  
						type=str,
						# type=argparse.FileType('r'), 
						help=config[plotName]["legend"] 
						)


args = parser.parse_args( sys.argv[1:] )


# def drawErrorPlot( dataFilename ):
# 	pass



def drawBoxPlot(dataFilename):

	logger.info("Drawing error plot for dataset ", dataFilename)

	res = ds.SQLiteDataSet(dataFilename) 

	keys,durations =  res.formatForPlotbox()

	locs, labels = plt.xticks() 
	# concatenate
	p1 = plt.boxplot(
		durations
		# ,notch=True
		#,positions=keys
		)

	# plt.xticks(keys)
	# plt.xticks(locs)

	return p1


def drawErrorPlot(dataFilename):

	# TODO need to get 
	logger.info("Drawing error plot for dataset ", dataFilename)

	res = ds.SQLiteDataSet(dataFilename) 

	keys,minValues,maxValues,avg,rowcounts =  res.formatForHistogram()
	
	
	yerr = list(map( (lambda x, y: x-y ), maxValues, avg) )

	limit = 5
	for index, nb in enumerate(rowcounts):
		if nb < MINIMUM_SAMPLE_SIZE:
			print('Results are too few: ', nb , ' results for key ', keys[index] )

	# print("mean", avg )
	# print("min",  minValues )
	# print("high", maxValues )
	# print("Compute xerr, yerr",yerr)

	#x, y, yerr=None, xerr=None, fmt='-', ecolor=None, elinewidth=None, capsize=3, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None, hold=None, **kwargs)
	format=config[plotName].get("format",'o')
	print("format:", format)
	p1 = plt.errorbar(
				keys,	# cles
				y=avg, 
				yerr=yerr, 
				label = config[plotName]["legend"],
				linewidth=config[plotName].get("linewidth",3), 
				linestyle= config[plotName].get("linestyle","--"),
				fmt=format,
				markersize= config[plotName].getfloat("ms",6.)
				,capthick=config[plotName].getint("capthick",1)
				
	# 			xerr=None, 
				# fmt='-', 
	# 			ecolor=None, 
				
	# 			capsize=3, 
	# 			barsabove=False, 
	# 			lolims=False, 
	# 			uplims=False, 
	# 			xlolims=False, 
	# 			xuplims=False, 
	# 			errorevery=1, 
	# 			capthick=None, 
				,hold=True 
	# 			#**kwargs
				)
	# plt.draw()
	return p1



plotTypes = {
"error" : drawErrorPlot,
"box" : drawBoxPlot

}

# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False)

# linewidth=2.0,names=("lol","plop")


print("names",plotNames)
print("types ",plotTypes)
plots = dict.fromkeys( plotNames)
plots = defaultdict(dict)
# for plot in plots:
# 	plot = dict.fromkeys(["graph" ,"legend" ])
# hold on;
# TODO from these args, use a function  called loadDataSet
for plotName in plotNames:
	print( config[plotName].get("type","error") )
	plots[plotName]["graph"]  = plotTypes[ config[plotName].get("type","error") ]( getattr(args,plotName) )
	# plots[plotName][0]  = drawPlot( getattr(args,plotName) )
	plots[plotName]["legend"] = config[plotName]["legend"]

# p1 = plt.plot(  res[0,] , "b") 
# #, legend="Hello world"
# p2 = plt.plot( res[1,],"r", label="red" )
# TODO use getkeys or getattributes 
# plt.legend([p1, p2], ["Sinus", "Cosinus"])


# plt.title("Mon titre")
# plt.title(config["general"]["title"], fontsize=30)
plt.xticks( fontsize=26)
plt.yticks(fontsize=26)
plt.xlabel(config["general"]["xlabel"], fontsize=28)
plt.ylabel(config["general"]["ylabel"], fontsize=28)

plt.legend(loc='upper left', fontsize=28)
# ax1.figure.show()
# plt.tight_layout()
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
