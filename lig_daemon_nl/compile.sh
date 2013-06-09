#!/bin/bash
daemonFolder="/home/teto/lig_daemon"

gcc -Wall  -g    -I/usr/include/libnl3 -I/home/teto/mptcp_src/include  -c /home/teto/lig_daemon_nl/lig_daemon.c -o obj/Debug/lig_daemon.o

g++  -o $daemonFolder/lig_daemon_d $daemonFolder/obj/Debug/lig_daemon.o   -lnl-3 -lnl-genl-3 
#-lexplain  
