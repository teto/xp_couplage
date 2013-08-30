#!/bin/bash
kernelSrc=$1
daemonSrc=$2
daemonBin=$3

set -x 

# hope to replace that via a python daemon or a makefile${daemonSrc}
gcc -Wall  -g    -I/usr/include/libnl3 -I${kernelSrc}/include  -c ${daemonSrc}/lig_daemon.c -o ${daemonSrc}/lig_daemon.o
g++  -o ${daemonBin} ${daemonSrc}/lig_daemon.o   -lnl-3 -lnl-genl-3 -lexplain  
