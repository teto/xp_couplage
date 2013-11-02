#obj-y += lig_module.o
obj-m += mptcp_netlink.ko
mptcp_netlink-objs := mptcp_netlink.o mptcp_mesh.o

all:
    $(MAKE) -C $(KDIR) SUBDIRS=$(PWD) modules

install:
    sudo $(MAKE) -C $(KDIR) M=$(PWD) modules_install

cleanall: clean
clean:
    $(MAKE) -C $(KDIR) M=$(PWD) clean
