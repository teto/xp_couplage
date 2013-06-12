#!/bin/bash
echo "USAGE: $0 [load|install|compile] as many times as you want "

KDIR="/home/teto/mptcp_src"
moduleFolder="/home/teto/lig_module"
cmd="$1"

#make -C /lib/modules/`uname -r`/build M=$PWD


#if [ $# -le 0 ]; then

for cmd in $@; do
#    if [ $1 == "load" ]; then

case "$cmd" in
     "remove") 
        echo "remove module"
        rmmod lig_module 2>&1
	;;

    "compile") echo "compiling module"
        # -C => change to that dir before doing anything
        make -C $KDIR M=$moduleFolder

	res=$?
	echo "Result of compilation : $res"
	if [ $res -ne 0 ]; then
		echo "compilation failed"
		exit 1
	fi
        ;;
    

    "load") echo "Loading module "
            insmod $moduleFolder/lig_module.ko 2>&1
        ;;
     "install") echo "Installing module"
        make -C /lib/modules/`uname -r`/build M=$moduleFolder modules_install
	echo "Result of compilation : $?"
	if [ $? -ne 0 ]; then
		echo "compilation failed"
		exit 1
	fi

        modprobe lig_module
	;;
esac;

done;
