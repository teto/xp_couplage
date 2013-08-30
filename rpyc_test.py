#!/usr/bin/python3
# launch on server  /usr/local/bin/rpyc_classic
import rpyc
conn = rpyc.classic.connect('localhost')
print conn.modules.os.uname()