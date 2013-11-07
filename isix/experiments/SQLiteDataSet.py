#!/usr/bin/python3
from . import manager as mgr
import sqlite3 as db
import logging
import argparse
import sys

logger = logging.getLogger()


# should be a minimum number of keys
# TODO add adapters
class SQLiteDataSet(mgr.FileDownloadData):

    def __init__(self, filename):
        self._conn = None
        self.load( filename )

    def __del__(self):
        if self._conn:
            # logger.debug("Closing connection to database")
            self._conn.close()

    def addResult(self, fileSize, result):
        self._cur.execute("INSERT INTO results(filesize, duration) VALUES(?,?)", (fileSize, result) )
        self._conn.commit()

    def getStats(self):
        # results 
        self._cur.execute( "SELECT filesize,count(*) FROM results GROUP BY filesize " )
        results = [ (i[0],i[1]) for i in self._cur ]
        return dict( results )


    def getAvg(self, keys):
        
        # TODO display on how many items it was done 
        # fileSizes
        # select * from people where name_last=:who and age=:age", {"who": who, "age": age}

        # GROUP BY key AVG(duration), 
        # , (key,)
        self._cur.execute( "SELECT filesize,AVG(duration),min(duration),max(duration),count(*) FROM results GROUP BY filesize " )
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
        self._cur.executescript("""
            CREATE TABLE IF NOT EXISTS results(
                filesize INTEGER,
                duration REAL,
                id INTEGER PRIMARY KEY AUTOINCREMENT
                );

            CREATE TABLE IF NOT EXISTS tcp_stats(
                min_rtt REAL DEFAULT 0,
                max_rtt REAL DEFAULT 0,
                avg_rtt REAL DEFAULT 0,
                result_id INTEGER
                )


            """)
        self._conn.commit()
        
    def getMin(self,keys):
        pass
        # self._cur.execute( "SELECT AVG(duration) FROM results WHERE filesize=?", filesize)

    def getMax(self,keys):
        pass
        # self._cur.execute( "SELECT AVG(duration) FROM results WHERE filesize=?", filesize)



    def formatForPlotbox(self):
        """

        """

        keys = []
        durations = []
        rowcounts = []
        self._cur.execute( "SELECT filesize FROM results GROUP BY filesize " )
        # keys = self._cur.fetchall()
        # print("keys", keys)
        for i in self._cur:
            print("key", i[0] )
            keys.append( i[0])

        # where Id in 
        for key in keys:
            self._cur.execute( "SELECT duration FROM results WHERE filesize=?", (key,) )
            durationsPerKey = []
            for i in self._cur:
                
                print("duration(s) ?:", i[0] )
                if i[0] != None:
                # print("count", i[2] )
                
                    durationsPerKey.append( i[0] )
                # rowcounts.append( i[2] )

            durations.append( durationsPerKey )

        print("Durations", durations )
        return keys, durations

    def formatForHistogram(self):
        """

        """
        keys = []
        minima = []
        maxima = []
        avg = []
        rowcounts = []

        self._cur.execute( "SELECT filesize,AVG(duration),min(duration),max(duration),count(*) FROM results GROUP BY filesize " )
        
        # TODO replace by self._cur.fetchall()  ?

        for i in self._cur:
            # print("keys")
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
    # keys = [ '512', '1024']
    # print( "Avg", ds.getAvg(keys) )
    # print( "Min", ds.getMin(keys) )
    stats = ds.getStats ()
    # print( "Statistics" , stats[512] )