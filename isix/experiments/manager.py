
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

    cur.executescript("""


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

# should be able to detect failed tests,
# propose the user to resume it or other options whenfacing a failure 
# sthg like try again or give up
class XPManager:

	def __init__(self, config, tests):
		self._tests = tests
		# TODO load config
		self._config = config

	def run_tests():
        
