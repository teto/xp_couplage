#!/bin/bash

tap="tap0"
#tap="lispTun0"
bridge="virbr0"
#ifconfig_cmd="ifconfig"
#export good folders
echo "============================================="
echo -e "\nChecking if bridge interface is presented"
echo "============================================="

res=`ifconfig -a | grep br | cut -d " " -f1`
if [ -z "$res" ]; then
       echo "No bridge interface was found"
#	exit 1
#       echo -e "Checking if package 'bridge-utils' is installed"
 #      if [ `rpm -qa | grep bridge-utils` ]; then
#	  echo -e "Package 'bridge-utils' is installed, nothing to do"
 #      else
#	  echo -e "No package 'bridge-utils' was found, trying to install it"
#	  sudo yum install bridge-utils -y
 #      fi
       sudo  brctl addbr $bridge
#       bridge=virbr0
       echo -e "Interface $bridge was created"
else
       echo "Interface $bridge is presented, nothing to do"
fi
sudo ifconfig $bridge up


echo -e "\nChecking if a virtual tap interface \"$tap\" is presented"
res=`ifconfig -a | grep $tap | cut -d " " -f1`
if [ -z "$res" ]; then
      echo "No tap interface was found"
      echo "Checking if 'tunctl' package is installed"
      if [ ! -z `which tunctl` ]; then
	echo "Package 'tunctl' is installed, nothing to do"
      else
	echo "No package 'tunctl' was found, install it"
	exit 1
#        sudo yum install tunctl -y
      fi
      echo -e "Checking if module 'tun' is loaded in kernel"
      check=`lsmod | grep tun | cut -d " " -f1`
	if [ "$check"  == "" ]; then
	  echo "Module 'tun' is not loaded, trying to load it"
	  sudo modprobe tun
	else 
        echo "Module 'tun' is loaded, nothing to do"
      fi
      sudo tunctl -u $(whoami) -t $tap
      echo "Interface $tap was created"
else
	echo "Interface $tap is presented, nothing to do"
fi
sudo ifconfig $tap up
echo  "Checking if $tap is presented in the bridge $bridge"
check=`brctl show $bridge | grep $tap`
if [ "$check" == "" ]; then
      sudo brctl addif $bridge $tap
      echo "Interface $tap was added to $bridge"
      else
	echo "Interface $tap is presented in $bridge, nothing to do"
      fi


echo -e "\nChecking if Ethernet interface is presented"
#interface_list=`ip addr show label eth* | cut -d ":" -f2`
#if [ "$interface_list" != "" ]; then
 #     echo -e "\nThe following Ethernet interfaces were found" 
  #    echo -e "\n$interface_list"
      a=0
      while [ $a == 0 ]; do
	echo -n -e "\nPlease, enter the interface name and press [ENTER]: "
	# remove redirection if u want another interface
	read interface 
#< "eth0"
	#b=`echo $interface_list | grep $interface` 
	b=`ip addr show dev $interface`
	if [ "$b" == "" ]; then
	  echo "Interface $interface cannot be found, try again"
	else 
	  a=1
	fi
      done
      
      echo -e "\nChecking if interface $interface is presented in $bridge"
      check=`brctl show $bridge | grep $interface`
      if [ "$check" == "" ]; then
	sudo brctl addif $bridge $interface
        echo "Interface $interface was added to $bridge"
      else
	echo "Interface $interface is presented in $bridge, nothing to do" 
      fi   
    


echo -e "\nSwitching off Ethernet filtering"
for file in /proc/sys/net/bridge/bridge* 
do
  echo 0 | sudo tee $file > /dev/null
done
echo "Ethernet filtering was switched off"

echo -e "\nTrying to restore your network connectivity"
ip=`ip addr show $interface | grep -w inet | cut -d "t" -f2 | cut -d "b" -f1`
default=`ip route | grep default | cut -d " " -f3`

if [ "$ip"  == "" ]; then
    echo "No valid IP address is configured on interface $interface"
    echo "Sorry, your network connection cannot be restored"
    exit
fi

sudo ifconfig $bridge $ip up
sudo ifconfig $interface promisc 0.0.0.0 up  
sudo route add default gw $default

echo -e "\nNote:" 
echo "IP address $ip was configured on interface $bridge"
echo "IP address 0.0.0.0 was configured on interface $interface"
echo "Default gateway address $default was restored"

