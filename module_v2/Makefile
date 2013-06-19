#obj-y += lig_module.o
obj-m += lig_module.o

all:
    $(MAKE) -C $(KDIR) SUBDIRS=$(PWD) modules

install:
    $(MAKE) -C $(KDIR) M=$(PWD) modules_install

cleanall: clean
clean:
    $(MAKE) -C $(KDIR) M=$(PWD) clean
