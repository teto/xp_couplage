#!/usr/bin/python3
import argparse
import csv
import numpy as np
import matplotlib.pyplot as plt
import configparser
import argparse
import sys
import isix.experiments.SQLiteDataSet as ds

from collections import defaultdict


# TODO it 

# expects a plot script and data files





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



def drawPlot(dataFilename):

    # TODO need to get 
    print("Drawing plot for dataset ", dataFilename)

    # resultsFilename= "/home/teto/xp_couplage/results/tcpwithoutlisp_1509_2118.csv"
    # TODO use numpy to load data
    # np.array
    # names = True reads column names from data
    res = np.loadtxt( dataFilename, 
                    dtype=None, 
                    comments="#",
            #, names=True
                    delimiter=","
            )

    fileSizes = res[0,]
    print("file sizes:\n", fileSizes)

    res= res[1:,]
    # print("Loaded results:\n", res)

    # res.reshape( (3,3))
    mean = res.mean()

    # generate linear spaces
    # x= res[0,]



    avg = getAverageRowResults ( res)
    minValues = getLowestRowResults ( res)
    maxValues = getHighestRowResults ( res)

    print("mean", avg )
    print("min",  minValues )
    print("high", maxValues )

    # errors relative to data set
    yerr= maxValues- avg, avg-minValues
    print("Compute xerr, yerr",yerr)


    #x, y, yerr=None, xerr=None, fmt='-', ecolor=None, elinewidth=None, capsize=3, barsabove=False, lolims=False, uplims=False, xlolims=False, xuplims=False, errorevery=1, capthick=None, hold=None, **kwargs)
    p1 = plt.errorbar(
                fileSizes,
                # x, 
                y=avg, 
                yerr=yerr, 
                label = config[plotName]["legend"]
    #           xerr=None, 
    #           fmt='-', 
    #           ecolor=None, 
    #           elinewidth=None, 
    #           capsize=3, 
    #           barsabove=False, 
    #           lolims=False, 
    #           uplims=False, 
    #           xlolims=False, 
    #           xuplims=False, 
    #           errorevery=1, 
    #           capthick=None, 
    #           hold=None, 
    #           #**kwargs
                )
    return p1

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False)

# linewidth=2.0,names=("lol","plop")


print("names",plotNames)
plots = dict.fromkeys( plotNames)
plots = defaultdict(dict)
# for plot in plots:
#   plot = dict.fromkeys(["graph" ,"legend" ])


for plotName in plotNames:
    plots[plotName]["graph"]  = drawPlot( getattr(args,plotName) )
    # plots[plotName][0]  = drawPlot( getattr(args,plotName) )
    plots[plotName]["legend"] = config[plotName]["legend"]

# p1 = plt.plot(  res[0,] , "b") 
# #, legend="Hello world"
# p2 = plt.plot( res[1,],"r", label="red" )
# TODO use getkeys or getattributes 
# plt.legend([p1, p2], ["Sinus", "Cosinus"])


# plt.title("Mon titre")
plt.title(config["general"]["title"])
# plt.xticks( fileSizes)
# plt.yticks()
plt.xlabel("hello world")
plt.xlabel(config["general"]["xlabel"])
plt.ylabel(config["general"]["ylabel"])

plt.legend(loc='upper left')
plt.show()





