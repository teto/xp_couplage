#!/usr/bin/python3
from . import manager as mgr
import sqlite3 as db
import logging
import argparse

logger = logging.getLogger()


# should be a minimum number of keys
class SQLiteDataSet(mgr.FileDownloadData):

    def __init__(self, filename):
        self._conn = None
        self.load( filename )

    def __del__(self):
        if self._conn:
            # logger.debug("Closing connection to database")
            self._conn.close()

    def getAvg(self, keys):
        
        # TODO display on how many items it was done 
        # fileSizes
        # select * from people where name_last=:who and age=:age", {"who": who, "age": age}

        # GROUP BY key AVG(duration), 
        # , (key,)
        self._cur.execute( "SELECT [t=filesize],AVG(duration),min(duration),max(duration),count(*) FROM results GROUP BY filesize " )
        # print( self._cur )
        # print( "row count", self._cur.rowcount)
        for i in self._cur:
            # i[2]
            print ("keys", i.keys() )
            print("result 0: ", i[0]  )
            print("result 1: ", i[1]  )
            print("result 1: ", i[2]  )
            print("rowcount: ", i[4]  )
        # return 

    def getMinTransferTime(self, item):
        raise NotImplementedError();

    def getMaxTransferTime(self, item):
        raise NotImplementedError();

    def save(self, item):
        self._conn.close()
        raise NotImplementedError();

    def load(self, filename):
        
        if self._conn:
            self._conn.close()

        self._conn = db.connect(filename)
        self._conn.row_factory = db.Row                # accès facile aux colonnes

        self._cur = self._conn.cursor()                             # obtention d'un curseur
        
    def getMin(self,keys):
        pass
        # self._cur.execute( "SELECT AVG(duration) FROM results WHERE filesize=?", filesize)

    def getMax(self,keys):
        pass
        # self._cur.execute( "SELECT AVG(duration) FROM results WHERE filesize=?", filesize)


    def formatForHistogram(self):
        keys = []
        minima = []
        maxima = []
        avg = []
        rowcounts = []

        self._cur.execute( "SELECT filesize,AVG(duration),min(duration),max(duration),count(*) FROM results GROUP BY filesize " )
        
        for i in self._cur:
            print("keys")
            keys.append( i[0])
            avg.append( i[1])
            minima.append( i[2])
            maxima.append( i[3])
            rowcounts.append( i[4])

        return keys,minima,maxima,avg,rowcounts
        

if __name__ == '__main__':




    parser = argparse.ArgumentParser(
        #description='Handle mptcp kernel module in charge of converting kernel requests into netlink requests '
        description='This program generates plots for different experiences'
        )

    #there must be at most one ?
    #argparse.FileType('r')
    parser.add_argument('results', type=str ,
              help="Choose filename")

    args = parser.parse_args( )


    ds = SQLiteDataSet(args.results)
    keys = [ '512', '1024']
    print( "Avg", ds.getAvg(keys) )
    print( "Min", ds.getMin(keys) )