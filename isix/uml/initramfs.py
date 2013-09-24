

#
# be able to embed modules
class Initramfs(object):
	pass



# More info on
# https://www.kernel.org/doc/Documentation/filesystems/ramfs-rootfs-initramfs.txt
# easy way is to use an utilty such a "mkinitramfs"
def build_initramfs(output_filename):
	print "========================================================================"
	generator = g_kernel_bin+"/usr/gen_init_cpio"
	print("Building initramfs. Run "+generator+" for help");
	print "========================================================================"

	# one should check that the kernel supports initramfs
	#CONFIG_BLK_DEV_INITRD
	#if not os.path.exists(directory):
		#print "ERROR: Your path: "+directory+" does not exist!!!"
		#exit()
	#os.chdir(directory)
	#os.system("mkdir -p bin sbin etc proc sys mnt");
	# gen_init_cpio expands vars in ${}	
	cpio_list= """
		  dir /dev 755 0 0
		  nod /dev/console 644 0 0 c 5 1
		  nod /dev/loop0 644 0 0 b 7 0
		  dir /bin 755 1000 1000
		  slink /bin/sh busybox 777 0 0
		  file /bin/busybox initramfs/busybox 755 0 0
		  dir /proc 755 0 0
		  dir /sys 755 0 0
		  dir /mnt 755 0 0
		  file /init initramfs/init.sh 755 0 0
		"""

	cpio_list = g_cwd+ "/cpio_list.txt"
	print cpio_list
	# check file exits ( <=> kernel built)
	if not os.path.isfile( generator ):
		print "Build kernel first to generate initramfs generator '"+generator+"'"
		exit()

	# try without compressing it
	#| gzip 
	os.system( generator + " "+ cpio_list + ">" + output_filename +""  )
	print "========================================================================"
	print "Initramfs should be available in " + output_filename 
	print "========================================================================"

	#Mount things needed by this script
	# put it into init file
	#os.system("mount -t proc proc /proc")
	#os.system("mount -t sysfs sysfs /sys")
	#os.system("find . | cpio -H newc -o > ../initramfs.cpio");
	#os.system("cpio");

def uncompress_initramfs():
	
	# if compressed you should uncompress first
	#cpio -i -d -H newc -F initramfs_mptcp --no-absolute-filenames
	return False 