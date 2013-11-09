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
# import collections

from collections import defaultdict, OrderedDict


logger = logging.getLogger()
logger.setLevel( logging.DEBUG )


MINIMUM_SAMPLE_SIZE = 0
# expects a plot script and data files

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation() )


# plots = {
# }

class PlotParser(argparse.Action):

	# how to pass an option string
	def __call__(self,parser, namespace, values, option_string=None):
		# TODO selon la optional string, on associe une fct
		print("Valus: %r ",values)
		print("Optional string: %r ", option_string)
		args = plot_parser.parse_args(values)
		#values
		plots = getattr(namespace, self.dest)
		if not plots:
			plots= OrderedDict()

		plots[ args.graphName ] = dict.fromkeys( ["dataset"] );
		plots[ args.graphName ]["dataset"] = args.file
		setattr(namespace, self.dest, plots )




parser = argparse.ArgumentParser(
	#description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
	description='This program generates plots for different experiences'
	)

#there must be at most one ?
parser.add_argument('config_file', type=argparse.FileType('r') ,
		  help="Choose plot configuration file")

parser.add_argument('--plot', 
			type=str 
			, dest="plots"
			, nargs=2
			, action=PlotParser
		  	, help="Name of the plot. Might set many of them"
		  # const=
		  )
# parser.add_argument('args', nargs=argparse.REMAINDER, action="store")

parser.add_argument('--title', type=str,
		  help="Title of the plot"
		  )

# subparsers = parser.add_subparsers(help='commands')

plot_parser = argparse.ArgumentParser(description="add a plot")
plot_parser.add_argument('graphName'
			, type=str 
			# , choices=[ "tcp" ]
			#	, action="append", dest="plotNames"
		  	, help="Name of the plot. Might set many of them"
			)

plot_parser.add_argument('file'
			# TODO
			# , type=argparse.FileType("r")
			, type=str
		  	, help="Name of the plot. Might set many of them"
			)


if len(sys.argv) < 1:
	print("Choose a graph definition file as a parameter (graph1.ini for instance)")
	exit(1)

# [ sys.argv[1]]
args = parser.parse_args( )
# print("args", args.args)



# class ParsePlot:

# 	def __call__

# 	def __init__(self):
# 		pass

# TODO draw with error bars

print("Logging config file ", args.config_file )

# config.set("DEFAULT", "MainDir", mainDir )
# TODO be able to load config from YAML
config.read_file( args.config_file )

# config.sections()
# parser.add_argument('--plot', 
# 			type=str 
# 			, choices=[ x for x in config.sections() if x is not "general" ]
# 			, nargs=2
# 			, dest="plotNames"
# 			, action="append"
# 		  	, help="Name of the plot. Might set many of them"
# 		  # const=
# 		  )


# name plots to draw
# remove the general section


# plotNames = config["general"]["draw"].split(' ')
# for plotName in plotNames:
	# TODO check a section exists
	# print("plot name: ", plotName )
	#argparse.FileType('r')
	# parser.add_argument( plotName,  
	# 					type=str,
	# 					# type=argparse.FileType('r'), 
	# 					help=config[plotName]["legend"] 
	# 					)

#sys.argv[1:]
# args = parser.parse_args( args.args  )

# plotNames = args.plotNames

# if not plotNames:
# 	print("No plot to draw. Us --plot to add some plots to draw")
# 	exit(1)
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



# for plot in plots:
# 	plot = dict.fromkeys(["graph" ,"legend" ])
# hold on;
# TODO from these args, use a function  called loadDataSet
#getattr(args,plotName)
for plotName,conf in args.plots.items():
	print( config[plotName].get("type","error") )
	drawPlotCb = plotTypes[ config[plotName].get("type","error") ]
	conf["graph"]  = drawPlotCb( conf["dataset"] )
	# plots[plotName][0]  = drawPlot( getattr(args,plotName) )
	conf["legend"] = config[plotName]["legend"]



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
