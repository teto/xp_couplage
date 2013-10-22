
import sqlite3 as db


def create_db(filename):

    # check it does not exist

    # 
    # Create tables experiment/result/tcpstat
        # mptcp INTEGER, 
        # lisp INTEGER, 
        # status INTEGER DEFAULT -1,
    """
    CREATE TABLE experiments (
        name VARCHAR(50),
        date INTEGER,
        
        id INTEGER PRIMARY KEY AUTOINCREMENT
        );"""
        # Ajouter les hotes

    # cur.executescript(
    """


    CREATE TABLE results(
        filesize INTEGER,
        duration REAL,
        experiment INTEGER,
        id INTEGER PRIMARY KEY AUTOINCREMENT
        );

    CREATE TABLE tcp_stats(
        min_rtt REAL DEFAULT 0,
        max_rtt REAL DEFAULT 0,
        avg_rtt REAL DEFAULT 0,
        result_id INTEGER
        )


    """


def convertSQLiteToNumpyDataSet(sqliteDataset):
    return None



class FileDownloadData:
    
    def getAverageTransferTime(self, item):
        raise NotImplementedError();
    def getMinTransferTime(self, item):
        raise NotImplementedError();
    def getMaxTransferTime(self, item):
        raise NotImplementedError();

    def save(self, item):
        raise NotImplementedError();

    def load(self, item):
        raise NotImplementedError();



# class NumpyDataSet(FileDownloadData):
# class NumpyExperiment
#     def saveResults(self,resultFilename,results):
#         np.savetxt( resultFilename, results, fmt="%.3f",delimiter="," )


#         # creates a 2-dimensional array 
#         results = np.empty( (max_repeat +1, len(fileSizes) ) );
#         results.fill( np.NAN )
#         results[0,] = fileSizes
#         # print("results", results )

#                         logger.info("Attempt %d out of %d..."%( attempt, MAX_ATTEMPT) )
#                     elapsedTime = self.run_unit_test(fileToDownload)
#                     # results[iteration, no] = elapsedTime
#                     results[ index[0],index[1] ] = elapsedTime
#                     # value = elapsedTime
#                     # save intermediate results
#                     self.saveResults( resultFilename, results )


# should be able to detect failed tests,
# propose the user to resume it or other options whenfacing a failure 
# sthg like try again or give up
class XPManager:

    def __init__(self, config, tests):
        self._tests = tests
        # TODO load config
        self._config = config

    def run_tests():
        pass

    def post_process():
        # preprocess data & draw graphs
        pass
