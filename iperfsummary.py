#!/usr/bin/python
 
# date,sender-ip,sender-port,receiver-ip,receiver-port,id,interval,transfer,bandwidth
# 20111212103043,10.120.15.8,45020,10.120.13.120,5001,5,0.0-21.4,2490368,931080
# 20111212103109,10.120.15.8,5001,10.120.13.120,57022,4,0.0-24.2,2228224,736145
 
FILENAME = 'client-iperf.log'
 
RUNS = 1
 
MAX_BANDWIDTH_SENT = 0
MAX_BANDWIDTH_SENT_DATE = 0
MAX_BANDWIDTH_RECEIVED = 0
MAX_BANDWIDTH_RECEIVED_DATE = 0
 
TOTAL_BANDWIDTH_SENT = 0
TOTAL_BANDWIDTH_RECEIVED = 0
 
TOTAL_SENT = 0
TOTAL_RECEIVED = 0
 
def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size
 
f = open(FILENAME)
l1 = f.readline().strip().split(',')
l2 = f.readline().strip().split(',')
while l2 and l2[0] != '':
    if RUNS == 1:
        START = l1[0]
 
    BW_SENT = int(l1[8])
    BW_RECEIVED = int(l2[8])
 
    TOTAL_SENT = TOTAL_SENT + int(l1[7])
    TOTAL_RECEIVED = TOTAL_RECEIVED + int(l2[7])
 
    TOTAL_BANDWIDTH_SENT = TOTAL_BANDWIDTH_SENT + int(l1[8])
    TOTAL_BANDWIDTH_RECEIVED = TOTAL_BANDWIDTH_RECEIVED + int(l2[8])
 
    if BW_SENT > MAX_BANDWIDTH_SENT:
        MAX_BANDWIDTH_SENT = BW_SENT
        MAX_BANDWIDTH_SENT_DATE = l1[0]
 
    if BW_RECEIVED > MAX_BANDWIDTH_RECEIVED:
        MAX_BANDWIDTH_RECEIVED = BW_RECEIVED
        MAX_BANDWIDTH_RECEIVED_DATE = l2[0]
 
    END = l2[0]
    RUNS = RUNS + 1
    l1 = f.readline().strip().split(',')
    l2 = f.readline().strip().split(',')
 
f.close()
 
print "------------------------------------"
print "   --   IPERF CSV Summariser   --   "
print "-- Cooper Lees <me@cooperlees.com --"
print "------------------------------------"
print "-- SUMMARY --"
print "- %s to %s" % ( START, END )
print "- %d runs of IPERF" % RUNS
print "- Averages:"
print "-\tAverage Sent\t\t\t= %s" % convert_bytes((TOTAL_SENT / RUNS))
print "-\tAverage Received\t\t= %s" % convert_bytes((TOTAL_RECEIVED / RUNS))
print "-\tAverage Send Bandwidth\t\t= %s" % convert_bytes((TOTAL_BANDWIDTH_SENT / RUNS))
print "-\tAverage Receive Bandwidth\t= %s" % convert_bytes((TOTAL_BANDWIDTH_RECEIVED / RUNS))
print "-\tMax Send Bandwidth\t\t= %s (at %s)" % (convert_bytes((MAX_BANDWIDTH_SENT)), MAX_BANDWIDTH_SENT_DATE)
print "-\tMax Receive Bandwidth\t\t= %s (at %s)" % (convert_bytes((MAX_BANDWIDTH_RECEIVED)), MAX_BANDWIDTH_RECEIVED_DATE)
print "------------------------------------"
