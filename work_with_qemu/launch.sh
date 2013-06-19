#!/bin/bash
# boot -c => boot from HDD
#qemu -hda ubuntuimage -m 1G -net tap,ifname=tap0,script=no -boot c
#-no-acpi 

debuggingPort="8888"

echo "USE: $O {gdb|nographic}"
echo "Debugging Port to use with GDB: $debuggingPort"

default="drive network virtualFS externalKernel "
#drive file,boot=on
#externalKernel="-kernel /home/teto/mptcp_src/arch/x86_64/boot/bzImage -append \"root=/dev/sda1 rw rootfstype=ext4\"" # kgdboc=ttyS0,115200\""  #  
externalKernel="-kernel /home/teto/mptcp_src/arch/x86_64/boot/bzImage -append \"root=/dev/sda1 kgdboc=ttyS0,115200\""
drive="-hda /home/teto/mptcp/ubuntuimage"
network="-net nic,model=e1000 -net tap,ifname=tap0,script=no,downscript=no"
nographic="-nographic"
#gdb="-gdb tcp::$debuggingPort -serial \"stdio\" -serial \"pty\" "
gdb="-s " # listen on tcp :1234
virtualFS="-virtfs fsdriver=local,id=fsdev0,path=/home/teto,security_model=passthrough,mount_tag=test"


#graphics=""
cmd="qemu -m 1G" 
#cmd="$cmd $networkConfig $virtualFS $graphics"  

#if [ $# -eq 1 ]; then 

#	echo "Virtual filesystem enabled:"
#	echo $virtualFS;
#fi


# -z => if string empty 
params="$@ $default"
for param in $params; do

    if [ -z "${!param}" ];then
	echo "Wrong parameter";
	continue;
    fi;
	echo -e "Enabling $param:\t${!param}"
	cmd="$cmd ${!param}"
done



echo -e "Launching command :\nsudo $cmd"
#$($cmd)

#qemu -m 1G -hda $driveFilename $loadKernel -append "root=/dev/sda1 rw rootfstype=ext4 kgdboc=ttyS0,115200" \
 #   $networkConfig $virtualFS $graphics 
    #-gdb tcp::8888
    #



