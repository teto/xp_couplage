cmd_/home/teto/xp_couplage/module_v3/mptcp_nl_simple.o := gcc -Wp,-MD,/home/teto/xp_couplage/module_v3/.mptcp_nl_simple.o.d  -nostdinc -isystem /usr/lib/gcc/x86_64-linux-gnu/4.7/include -I/home/teto/mptcp88/arch/x86/include -Iarch/x86/include/generated  -I/home/teto/mptcp88/include -Iinclude -I/home/teto/mptcp88/arch/x86/include/uapi -Iarch/x86/include/generated/uapi -I/home/teto/mptcp88/include/uapi -Iinclude/generated/uapi -include /home/teto/mptcp88/include/linux/kconfig.h   -I/home/teto/xp_couplage/module_v3 -D__KERNEL__ -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Wno-format-security -fno-delete-null-pointer-checks -O2 -m64 -mno-sse -mpreferred-stack-boundary=3 -mtune=generic -mno-red-zone -mcmodel=kernel -funit-at-a-time -maccumulate-outgoing-args -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1 -DCONFIG_AS_FXSAVEQ=1 -DCONFIG_AS_AVX=1 -DCONFIG_AS_AVX2=1 -pipe -Wno-sign-compare -fno-asynchronous-unwind-tables -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -mno-avx -Wframe-larger-than=2048 -fno-stack-protector -Wno-unused-but-set-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -pg -mfentry -DCC_USING_FENTRY -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fconserve-stack -DCC_HAVE_ASM_GOTO  -DMODULE  -D"KBUILD_STR(s)=\#s" -D"KBUILD_BASENAME=KBUILD_STR(mptcp_nl_simple)"  -D"KBUILD_MODNAME=KBUILD_STR(mptcp_nl)" -c -o /home/teto/xp_couplage/module_v3/mptcp_nl_simple.o /home/teto/xp_couplage/module_v3/mptcp_nl_simple.c

source_/home/teto/xp_couplage/module_v3/mptcp_nl_simple.o := /home/teto/xp_couplage/module_v3/mptcp_nl_simple.c

deps_/home/teto/xp_couplage/module_v3/mptcp_nl_simple.o := \
    $(wildcard include/config/ipv6.h) \
  /home/teto/mptcp88/include/linux/module.h \
    $(wildcard include/config/sysfs.h) \
    $(wildcard include/config/modules.h) \
    $(wildcard include/config/unused/symbols.h) \
    $(wildcard include/config/module/sig.h) \
    $(wildcard include/config/generic/bug.h) \
    $(wildcard include/config/kallsyms.h) \
    $(wildcard include/config/smp.h) \
    $(wildcard include/config/tracepoints.h) \
    $(wildcard include/config/tracing.h) \
    $(wildcard include/config/event/tracing.h) \
    $(wildcard include/config/ftrace/mcount/record.h) \
    $(wildcard include/config/module/unload.h) \
    $(wildcard include/config/constructors.h) \
    $(wildcard include/config/debug/set/module/ronx.h) \
  /home/teto/mptcp88/include/linux/list.h \
    $(wildcard include/config/debug/list.h) \
  /home/teto/mptcp88/include/linux/types.h \
    $(wildcard include/config/uid16.h) \
    $(wildcard include/config/lbdaf.h) \
    $(wildcard include/config/arch/dma/addr/t/64bit.h) \
    $(wildcard include/config/phys/addr/t/64bit.h) \
    $(wildcard include/config/64bit.h) \
  /home/teto/mptcp88/include/uapi/linux/types.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/types.h \
  /home/teto/mptcp88/include/uapi/asm-generic/types.h \
  /home/teto/mptcp88/include/asm-generic/int-ll64.h \
  /home/teto/mptcp88/include/uapi/asm-generic/int-ll64.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/bitsperlong.h \
  /home/teto/mptcp88/include/asm-generic/bitsperlong.h \
  /home/teto/mptcp88/include/uapi/asm-generic/bitsperlong.h \
  /home/teto/mptcp88/include/uapi/linux/posix_types.h \
  /home/teto/mptcp88/include/linux/stddef.h \
  /home/teto/mptcp88/include/uapi/linux/stddef.h \
  /home/teto/mptcp88/include/linux/compiler.h \
    $(wildcard include/config/sparse/rcu/pointer.h) \
    $(wildcard include/config/trace/branch/profiling.h) \
    $(wildcard include/config/profile/all/branches.h) \
    $(wildcard include/config/enable/must/check.h) \
    $(wildcard include/config/enable/warn/deprecated.h) \
    $(wildcard include/config/kprobes.h) \
  /home/teto/mptcp88/include/linux/compiler-gcc.h \
    $(wildcard include/config/arch/supports/optimized/inlining.h) \
    $(wildcard include/config/optimize/inlining.h) \
  /home/teto/mptcp88/include/linux/compiler-gcc4.h \
    $(wildcard include/config/arch/use/builtin/bswap.h) \
  /home/teto/mptcp88/arch/x86/include/asm/posix_types.h \
    $(wildcard include/config/x86/32.h) \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/posix_types_64.h \
  /home/teto/mptcp88/include/uapi/asm-generic/posix_types.h \
  /home/teto/mptcp88/include/linux/poison.h \
    $(wildcard include/config/illegal/pointer/value.h) \
  /home/teto/mptcp88/include/uapi/linux/const.h \
  /home/teto/mptcp88/include/linux/stat.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/stat.h \
  /home/teto/mptcp88/include/uapi/linux/stat.h \
  /home/teto/mptcp88/include/linux/time.h \
    $(wildcard include/config/arch/uses/gettimeoffset.h) \
  /home/teto/mptcp88/include/linux/cache.h \
    $(wildcard include/config/arch/has/cache/line/size.h) \
  /home/teto/mptcp88/include/linux/kernel.h \
    $(wildcard include/config/preempt/voluntary.h) \
    $(wildcard include/config/debug/atomic/sleep.h) \
    $(wildcard include/config/prove/locking.h) \
    $(wildcard include/config/ring/buffer.h) \
  /usr/lib/gcc/x86_64-linux-gnu/4.7/include/stdarg.h \
  /home/teto/mptcp88/include/linux/linkage.h \
  /home/teto/mptcp88/include/linux/stringify.h \
  /home/teto/mptcp88/include/linux/export.h \
    $(wildcard include/config/have/underscore/symbol/prefix.h) \
    $(wildcard include/config/modversions.h) \
  /home/teto/mptcp88/arch/x86/include/asm/linkage.h \
    $(wildcard include/config/x86/64.h) \
    $(wildcard include/config/x86/alignment/16.h) \
  /home/teto/mptcp88/include/linux/bitops.h \
  /home/teto/mptcp88/arch/x86/include/asm/bitops.h \
    $(wildcard include/config/x86/cmov.h) \
  /home/teto/mptcp88/arch/x86/include/asm/alternative.h \
    $(wildcard include/config/paravirt.h) \
  /home/teto/mptcp88/arch/x86/include/asm/asm.h \
  /home/teto/mptcp88/arch/x86/include/asm/cpufeature.h \
    $(wildcard include/config/x86/debug/static/cpu/has.h) \
  /home/teto/mptcp88/arch/x86/include/asm/required-features.h \
    $(wildcard include/config/x86/minimum/cpu/family.h) \
    $(wildcard include/config/math/emulation.h) \
    $(wildcard include/config/x86/pae.h) \
    $(wildcard include/config/x86/cmpxchg64.h) \
    $(wildcard include/config/x86/use/3dnow.h) \
    $(wildcard include/config/x86/p6/nop.h) \
    $(wildcard include/config/matom.h) \
  /home/teto/mptcp88/include/asm-generic/bitops/find.h \
    $(wildcard include/config/generic/find/first/bit.h) \
  /home/teto/mptcp88/include/asm-generic/bitops/sched.h \
  /home/teto/mptcp88/arch/x86/include/asm/arch_hweight.h \
  /home/teto/mptcp88/include/asm-generic/bitops/const_hweight.h \
  /home/teto/mptcp88/include/asm-generic/bitops/le.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/byteorder.h \
  /home/teto/mptcp88/include/linux/byteorder/little_endian.h \
  /home/teto/mptcp88/include/uapi/linux/byteorder/little_endian.h \
  /home/teto/mptcp88/include/linux/swab.h \
  /home/teto/mptcp88/include/uapi/linux/swab.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/swab.h \
  /home/teto/mptcp88/include/linux/byteorder/generic.h \
  /home/teto/mptcp88/include/asm-generic/bitops/ext2-atomic-setbit.h \
  /home/teto/mptcp88/include/linux/log2.h \
    $(wildcard include/config/arch/has/ilog2/u32.h) \
    $(wildcard include/config/arch/has/ilog2/u64.h) \
  /home/teto/mptcp88/include/linux/typecheck.h \
  /home/teto/mptcp88/include/linux/printk.h \
    $(wildcard include/config/early/printk.h) \
    $(wildcard include/config/printk.h) \
    $(wildcard include/config/dynamic/debug.h) \
  /home/teto/mptcp88/include/linux/init.h \
    $(wildcard include/config/broken/rodata.h) \
  /home/teto/mptcp88/include/linux/kern_levels.h \
  /home/teto/mptcp88/include/linux/dynamic_debug.h \
  /home/teto/mptcp88/include/linux/string.h \
    $(wildcard include/config/binary/printf.h) \
  /home/teto/mptcp88/include/uapi/linux/string.h \
  /home/teto/mptcp88/arch/x86/include/asm/string.h \
  /home/teto/mptcp88/arch/x86/include/asm/string_64.h \
    $(wildcard include/config/kmemcheck.h) \
  /home/teto/mptcp88/include/linux/errno.h \
  /home/teto/mptcp88/include/uapi/linux/errno.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/errno.h \
  /home/teto/mptcp88/include/uapi/asm-generic/errno.h \
  /home/teto/mptcp88/include/uapi/asm-generic/errno-base.h \
  /home/teto/mptcp88/include/uapi/linux/kernel.h \
  /home/teto/mptcp88/include/uapi/linux/sysinfo.h \
  /home/teto/mptcp88/arch/x86/include/asm/cache.h \
    $(wildcard include/config/x86/l1/cache/shift.h) \
    $(wildcard include/config/x86/internode/cache/shift.h) \
    $(wildcard include/config/x86/vsmp.h) \
  /home/teto/mptcp88/include/linux/seqlock.h \
  /home/teto/mptcp88/include/linux/spinlock.h \
    $(wildcard include/config/debug/spinlock.h) \
    $(wildcard include/config/generic/lockbreak.h) \
    $(wildcard include/config/preempt.h) \
    $(wildcard include/config/debug/lock/alloc.h) \
  /home/teto/mptcp88/include/linux/preempt.h \
    $(wildcard include/config/debug/preempt.h) \
    $(wildcard include/config/preempt/tracer.h) \
    $(wildcard include/config/context/tracking.h) \
    $(wildcard include/config/preempt/count.h) \
    $(wildcard include/config/preempt/notifiers.h) \
  /home/teto/mptcp88/include/linux/thread_info.h \
    $(wildcard include/config/compat.h) \
    $(wildcard include/config/debug/stack/usage.h) \
  /home/teto/mptcp88/include/linux/bug.h \
  /home/teto/mptcp88/arch/x86/include/asm/bug.h \
    $(wildcard include/config/bug.h) \
    $(wildcard include/config/debug/bugverbose.h) \
  /home/teto/mptcp88/include/asm-generic/bug.h \
    $(wildcard include/config/generic/bug/relative/pointers.h) \
  /home/teto/mptcp88/arch/x86/include/asm/thread_info.h \
    $(wildcard include/config/ia32/emulation.h) \
  /home/teto/mptcp88/arch/x86/include/asm/page.h \
  /home/teto/mptcp88/arch/x86/include/asm/page_types.h \
  /home/teto/mptcp88/arch/x86/include/asm/page_64_types.h \
    $(wildcard include/config/physical/start.h) \
    $(wildcard include/config/physical/align.h) \
  /home/teto/mptcp88/arch/x86/include/asm/page_64.h \
    $(wildcard include/config/debug/virtual.h) \
    $(wildcard include/config/flatmem.h) \
  /home/teto/mptcp88/include/linux/range.h \
  /home/teto/mptcp88/include/asm-generic/memory_model.h \
    $(wildcard include/config/discontigmem.h) \
    $(wildcard include/config/sparsemem/vmemmap.h) \
    $(wildcard include/config/sparsemem.h) \
  /home/teto/mptcp88/include/asm-generic/getorder.h \
  /home/teto/mptcp88/arch/x86/include/asm/processor.h \
    $(wildcard include/config/cc/stackprotector.h) \
    $(wildcard include/config/m486.h) \
    $(wildcard include/config/x86/debugctlmsr.h) \
    $(wildcard include/config/xen.h) \
  /home/teto/mptcp88/arch/x86/include/asm/processor-flags.h \
    $(wildcard include/config/vm86.h) \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/processor-flags.h \
  /home/teto/mptcp88/arch/x86/include/asm/vm86.h \
  /home/teto/mptcp88/arch/x86/include/asm/ptrace.h \
  /home/teto/mptcp88/arch/x86/include/asm/segment.h \
    $(wildcard include/config/x86/32/lazy/gs.h) \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/ptrace.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/ptrace-abi.h \
  /home/teto/mptcp88/arch/x86/include/asm/paravirt_types.h \
    $(wildcard include/config/x86/local/apic.h) \
    $(wildcard include/config/paravirt/debug.h) \
  /home/teto/mptcp88/arch/x86/include/asm/desc_defs.h \
  /home/teto/mptcp88/arch/x86/include/asm/kmap_types.h \
    $(wildcard include/config/debug/highmem.h) \
  /home/teto/mptcp88/include/asm-generic/kmap_types.h \
  /home/teto/mptcp88/arch/x86/include/asm/pgtable_types.h \
    $(wildcard include/config/mem/soft/dirty.h) \
    $(wildcard include/config/compat/vdso.h) \
    $(wildcard include/config/proc/fs.h) \
  /home/teto/mptcp88/arch/x86/include/asm/pgtable_64_types.h \
  /home/teto/mptcp88/arch/x86/include/asm/sparsemem.h \
  /home/teto/mptcp88/include/asm-generic/ptrace.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/vm86.h \
  /home/teto/mptcp88/arch/x86/include/asm/math_emu.h \
  /home/teto/mptcp88/arch/x86/include/asm/sigcontext.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/sigcontext.h \
  /home/teto/mptcp88/arch/x86/include/asm/current.h \
  /home/teto/mptcp88/arch/x86/include/asm/percpu.h \
    $(wildcard include/config/x86/64/smp.h) \
  /home/teto/mptcp88/include/asm-generic/percpu.h \
    $(wildcard include/config/have/setup/per/cpu/area.h) \
  /home/teto/mptcp88/include/linux/threads.h \
    $(wildcard include/config/nr/cpus.h) \
    $(wildcard include/config/base/small.h) \
  /home/teto/mptcp88/include/linux/percpu-defs.h \
    $(wildcard include/config/debug/force/weak/per/cpu.h) \
  /home/teto/mptcp88/arch/x86/include/asm/msr.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/msr.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/msr-index.h \
  /home/teto/mptcp88/include/uapi/linux/ioctl.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/ioctl.h \
  /home/teto/mptcp88/include/asm-generic/ioctl.h \
  /home/teto/mptcp88/include/uapi/asm-generic/ioctl.h \
  /home/teto/mptcp88/arch/x86/include/asm/cpumask.h \
  /home/teto/mptcp88/include/linux/cpumask.h \
    $(wildcard include/config/cpumask/offstack.h) \
    $(wildcard include/config/hotplug/cpu.h) \
    $(wildcard include/config/debug/per/cpu/maps.h) \
    $(wildcard include/config/disable/obsolete/cpumask/functions.h) \
  /home/teto/mptcp88/include/linux/bitmap.h \
  /home/teto/mptcp88/arch/x86/include/asm/paravirt.h \
    $(wildcard include/config/paravirt/spinlocks.h) \
  /home/teto/mptcp88/arch/x86/include/asm/nops.h \
    $(wildcard include/config/mk7.h) \
  /home/teto/mptcp88/arch/x86/include/asm/special_insns.h \
  /home/teto/mptcp88/include/linux/personality.h \
  /home/teto/mptcp88/include/uapi/linux/personality.h \
  /home/teto/mptcp88/include/linux/math64.h \
  /home/teto/mptcp88/arch/x86/include/asm/div64.h \
  /home/teto/mptcp88/include/asm-generic/div64.h \
  /home/teto/mptcp88/include/linux/err.h \
  /home/teto/mptcp88/include/linux/irqflags.h \
    $(wildcard include/config/trace/irqflags.h) \
    $(wildcard include/config/irqsoff/tracer.h) \
    $(wildcard include/config/trace/irqflags/support.h) \
  /home/teto/mptcp88/arch/x86/include/asm/irqflags.h \
  /home/teto/mptcp88/include/linux/atomic.h \
    $(wildcard include/config/arch/has/atomic/or.h) \
    $(wildcard include/config/generic/atomic64.h) \
  /home/teto/mptcp88/arch/x86/include/asm/atomic.h \
  /home/teto/mptcp88/arch/x86/include/asm/cmpxchg.h \
  /home/teto/mptcp88/arch/x86/include/asm/cmpxchg_64.h \
  /home/teto/mptcp88/arch/x86/include/asm/atomic64_64.h \
  /home/teto/mptcp88/include/asm-generic/atomic-long.h \
  /home/teto/mptcp88/include/linux/bottom_half.h \
  /home/teto/mptcp88/arch/x86/include/asm/barrier.h \
    $(wildcard include/config/x86/ppro/fence.h) \
    $(wildcard include/config/x86/oostore.h) \
  /home/teto/mptcp88/include/linux/spinlock_types.h \
  /home/teto/mptcp88/arch/x86/include/asm/spinlock_types.h \
  /home/teto/mptcp88/arch/x86/include/asm/rwlock.h \
  /home/teto/mptcp88/include/linux/lockdep.h \
    $(wildcard include/config/lockdep.h) \
    $(wildcard include/config/lock/stat.h) \
    $(wildcard include/config/prove/rcu.h) \
  /home/teto/mptcp88/include/linux/rwlock_types.h \
  /home/teto/mptcp88/arch/x86/include/asm/spinlock.h \
  /home/teto/mptcp88/include/linux/rwlock.h \
  /home/teto/mptcp88/include/linux/spinlock_api_smp.h \
    $(wildcard include/config/inline/spin/lock.h) \
    $(wildcard include/config/inline/spin/lock/bh.h) \
    $(wildcard include/config/inline/spin/lock/irq.h) \
    $(wildcard include/config/inline/spin/lock/irqsave.h) \
    $(wildcard include/config/inline/spin/trylock.h) \
    $(wildcard include/config/inline/spin/trylock/bh.h) \
    $(wildcard include/config/uninline/spin/unlock.h) \
    $(wildcard include/config/inline/spin/unlock/bh.h) \
    $(wildcard include/config/inline/spin/unlock/irq.h) \
    $(wildcard include/config/inline/spin/unlock/irqrestore.h) \
  /home/teto/mptcp88/include/linux/rwlock_api_smp.h \
    $(wildcard include/config/inline/read/lock.h) \
    $(wildcard include/config/inline/write/lock.h) \
    $(wildcard include/config/inline/read/lock/bh.h) \
    $(wildcard include/config/inline/write/lock/bh.h) \
    $(wildcard include/config/inline/read/lock/irq.h) \
    $(wildcard include/config/inline/write/lock/irq.h) \
    $(wildcard include/config/inline/read/lock/irqsave.h) \
    $(wildcard include/config/inline/write/lock/irqsave.h) \
    $(wildcard include/config/inline/read/trylock.h) \
    $(wildcard include/config/inline/write/trylock.h) \
    $(wildcard include/config/inline/read/unlock.h) \
    $(wildcard include/config/inline/write/unlock.h) \
    $(wildcard include/config/inline/read/unlock/bh.h) \
    $(wildcard include/config/inline/write/unlock/bh.h) \
    $(wildcard include/config/inline/read/unlock/irq.h) \
    $(wildcard include/config/inline/write/unlock/irq.h) \
    $(wildcard include/config/inline/read/unlock/irqrestore.h) \
    $(wildcard include/config/inline/write/unlock/irqrestore.h) \
  /home/teto/mptcp88/include/uapi/linux/time.h \
  /home/teto/mptcp88/include/linux/uidgid.h \
    $(wildcard include/config/uidgid/strict/type/checks.h) \
    $(wildcard include/config/user/ns.h) \
  /home/teto/mptcp88/include/linux/highuid.h \
  /home/teto/mptcp88/include/linux/kmod.h \
  /home/teto/mptcp88/include/linux/gfp.h \
    $(wildcard include/config/numa.h) \
    $(wildcard include/config/highmem.h) \
    $(wildcard include/config/zone/dma.h) \
    $(wildcard include/config/zone/dma32.h) \
    $(wildcard include/config/pm/sleep.h) \
    $(wildcard include/config/cma.h) \
  /home/teto/mptcp88/include/linux/mmzone.h \
    $(wildcard include/config/force/max/zoneorder.h) \
    $(wildcard include/config/memory/isolation.h) \
    $(wildcard include/config/memcg.h) \
    $(wildcard include/config/compaction.h) \
    $(wildcard include/config/memory/hotplug.h) \
    $(wildcard include/config/have/memblock/node/map.h) \
    $(wildcard include/config/flat/node/mem/map.h) \
    $(wildcard include/config/no/bootmem.h) \
    $(wildcard include/config/numa/balancing.h) \
    $(wildcard include/config/have/memory/present.h) \
    $(wildcard include/config/have/memoryless/nodes.h) \
    $(wildcard include/config/need/node/memmap/size.h) \
    $(wildcard include/config/need/multiple/nodes.h) \
    $(wildcard include/config/have/arch/early/pfn/to/nid.h) \
    $(wildcard include/config/sparsemem/extreme.h) \
    $(wildcard include/config/have/arch/pfn/valid.h) \
    $(wildcard include/config/nodes/span/other/nodes.h) \
    $(wildcard include/config/holes/in/zone.h) \
    $(wildcard include/config/arch/has/holes/memorymodel.h) \
  /home/teto/mptcp88/include/linux/wait.h \
  /home/teto/mptcp88/include/uapi/linux/wait.h \
  /home/teto/mptcp88/include/linux/numa.h \
    $(wildcard include/config/nodes/shift.h) \
  /home/teto/mptcp88/include/linux/nodemask.h \
    $(wildcard include/config/movable/node.h) \
  /home/teto/mptcp88/include/linux/pageblock-flags.h \
    $(wildcard include/config/hugetlb/page.h) \
    $(wildcard include/config/hugetlb/page/size/variable.h) \
  /home/teto/mptcp88/include/linux/page-flags-layout.h \
  include/generated/bounds.h \
  /home/teto/mptcp88/include/linux/memory_hotplug.h \
    $(wildcard include/config/memory/hotremove.h) \
    $(wildcard include/config/have/arch/nodedata/extension.h) \
    $(wildcard include/config/have/bootmem/info/node.h) \
  /home/teto/mptcp88/include/linux/notifier.h \
  /home/teto/mptcp88/include/linux/mutex.h \
    $(wildcard include/config/debug/mutexes.h) \
    $(wildcard include/config/mutex/spin/on/owner.h) \
    $(wildcard include/config/have/arch/mutex/cpu/relax.h) \
  /home/teto/mptcp88/include/linux/rwsem.h \
    $(wildcard include/config/rwsem/generic/spinlock.h) \
  /home/teto/mptcp88/arch/x86/include/asm/rwsem.h \
  /home/teto/mptcp88/include/linux/srcu.h \
  /home/teto/mptcp88/include/linux/rcupdate.h \
    $(wildcard include/config/rcu/torture/test.h) \
    $(wildcard include/config/tree/rcu.h) \
    $(wildcard include/config/tree/preempt/rcu.h) \
    $(wildcard include/config/rcu/trace.h) \
    $(wildcard include/config/preempt/rcu.h) \
    $(wildcard include/config/rcu/user/qs.h) \
    $(wildcard include/config/tiny/rcu.h) \
    $(wildcard include/config/debug/objects/rcu/head.h) \
    $(wildcard include/config/rcu/nocb/cpu.h) \
  /home/teto/mptcp88/include/linux/completion.h \
  /home/teto/mptcp88/include/linux/debugobjects.h \
    $(wildcard include/config/debug/objects.h) \
    $(wildcard include/config/debug/objects/free.h) \
  /home/teto/mptcp88/include/linux/rcutree.h \
  /home/teto/mptcp88/include/linux/workqueue.h \
    $(wildcard include/config/debug/objects/work.h) \
    $(wildcard include/config/freezer.h) \
  /home/teto/mptcp88/include/linux/timer.h \
    $(wildcard include/config/timer/stats.h) \
    $(wildcard include/config/debug/objects/timers.h) \
  /home/teto/mptcp88/include/linux/ktime.h \
    $(wildcard include/config/ktime/scalar.h) \
  /home/teto/mptcp88/include/linux/jiffies.h \
  /home/teto/mptcp88/include/linux/timex.h \
  /home/teto/mptcp88/include/uapi/linux/timex.h \
  /home/teto/mptcp88/include/uapi/linux/param.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/param.h \
  /home/teto/mptcp88/include/asm-generic/param.h \
    $(wildcard include/config/hz.h) \
  /home/teto/mptcp88/include/uapi/asm-generic/param.h \
  /home/teto/mptcp88/arch/x86/include/asm/timex.h \
  /home/teto/mptcp88/arch/x86/include/asm/tsc.h \
    $(wildcard include/config/x86/tsc.h) \
  /home/teto/mptcp88/arch/x86/include/asm/mmzone.h \
  /home/teto/mptcp88/arch/x86/include/asm/mmzone_64.h \
  /home/teto/mptcp88/include/linux/mmdebug.h \
    $(wildcard include/config/debug/vm.h) \
  /home/teto/mptcp88/arch/x86/include/asm/smp.h \
    $(wildcard include/config/x86/io/apic.h) \
    $(wildcard include/config/x86/32/smp.h) \
    $(wildcard include/config/debug/nmi/selftest.h) \
  /home/teto/mptcp88/arch/x86/include/asm/mpspec.h \
    $(wildcard include/config/x86/numaq.h) \
    $(wildcard include/config/eisa.h) \
    $(wildcard include/config/x86/mpparse.h) \
    $(wildcard include/config/acpi.h) \
  /home/teto/mptcp88/arch/x86/include/asm/mpspec_def.h \
  /home/teto/mptcp88/arch/x86/include/asm/x86_init.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/bootparam.h \
  /home/teto/mptcp88/include/linux/screen_info.h \
  /home/teto/mptcp88/include/uapi/linux/screen_info.h \
  /home/teto/mptcp88/include/linux/apm_bios.h \
  /home/teto/mptcp88/include/uapi/linux/apm_bios.h \
  /home/teto/mptcp88/include/linux/edd.h \
  /home/teto/mptcp88/include/uapi/linux/edd.h \
  /home/teto/mptcp88/arch/x86/include/asm/e820.h \
    $(wildcard include/config/efi.h) \
    $(wildcard include/config/hibernation.h) \
    $(wildcard include/config/memtest.h) \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/e820.h \
    $(wildcard include/config/intel/txt.h) \
  /home/teto/mptcp88/include/linux/ioport.h \
  /home/teto/mptcp88/arch/x86/include/asm/ist.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/ist.h \
  /home/teto/mptcp88/include/video/edid.h \
    $(wildcard include/config/x86.h) \
  /home/teto/mptcp88/include/uapi/video/edid.h \
  /home/teto/mptcp88/arch/x86/include/asm/apicdef.h \
  /home/teto/mptcp88/arch/x86/include/asm/apic.h \
    $(wildcard include/config/x86/x2apic.h) \
  /home/teto/mptcp88/include/linux/pm.h \
    $(wildcard include/config/vt/console/sleep.h) \
    $(wildcard include/config/pm.h) \
    $(wildcard include/config/pm/runtime.h) \
    $(wildcard include/config/pm/clk.h) \
    $(wildcard include/config/pm/generic/domains.h) \
  /home/teto/mptcp88/arch/x86/include/asm/fixmap.h \
    $(wildcard include/config/paravirt/clock.h) \
    $(wildcard include/config/provide/ohci1394/dma/init.h) \
    $(wildcard include/config/x86/visws/apic.h) \
    $(wildcard include/config/pci/mmconfig.h) \
    $(wildcard include/config/x86/intel/mid.h) \
  /home/teto/mptcp88/arch/x86/include/asm/acpi.h \
    $(wildcard include/config/acpi/numa.h) \
  /home/teto/mptcp88/include/acpi/pdc_intel.h \
  /home/teto/mptcp88/arch/x86/include/asm/numa.h \
    $(wildcard include/config/numa/emu.h) \
  /home/teto/mptcp88/arch/x86/include/asm/topology.h \
    $(wildcard include/config/x86/ht.h) \
  /home/teto/mptcp88/include/asm-generic/topology.h \
  /home/teto/mptcp88/arch/x86/include/asm/mmu.h \
  /home/teto/mptcp88/arch/x86/include/asm/realmode.h \
    $(wildcard include/config/acpi/sleep.h) \
  /home/teto/mptcp88/arch/x86/include/asm/io.h \
    $(wildcard include/config/mtrr.h) \
  /home/teto/mptcp88/include/asm-generic/iomap.h \
    $(wildcard include/config/has/ioport.h) \
    $(wildcard include/config/pci.h) \
    $(wildcard include/config/generic/iomap.h) \
  /home/teto/mptcp88/include/asm-generic/pci_iomap.h \
    $(wildcard include/config/no/generic/pci/ioport/map.h) \
    $(wildcard include/config/generic/pci/iomap.h) \
  /home/teto/mptcp88/include/linux/vmalloc.h \
    $(wildcard include/config/mmu.h) \
  /home/teto/mptcp88/include/linux/rbtree.h \
  /home/teto/mptcp88/arch/x86/include/asm/pvclock.h \
  /home/teto/mptcp88/include/linux/clocksource.h \
    $(wildcard include/config/arch/clocksource/data.h) \
    $(wildcard include/config/clocksource/watchdog.h) \
    $(wildcard include/config/clksrc/of.h) \
  /home/teto/mptcp88/arch/x86/include/asm/clocksource.h \
  /home/teto/mptcp88/arch/x86/include/asm/pvclock-abi.h \
  /home/teto/mptcp88/arch/x86/include/asm/vsyscall.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/vsyscall.h \
  /home/teto/mptcp88/arch/x86/include/asm/vvar.h \
  /home/teto/mptcp88/arch/x86/include/asm/idle.h \
  /home/teto/mptcp88/arch/x86/include/asm/io_apic.h \
  /home/teto/mptcp88/arch/x86/include/asm/irq_vectors.h \
    $(wildcard include/config/have/kvm.h) \
  /home/teto/mptcp88/include/linux/topology.h \
    $(wildcard include/config/sched/smt.h) \
    $(wildcard include/config/sched/mc.h) \
    $(wildcard include/config/sched/book.h) \
    $(wildcard include/config/use/percpu/numa/node/id.h) \
  /home/teto/mptcp88/include/linux/smp.h \
    $(wildcard include/config/use/generic/smp/helpers.h) \
  /home/teto/mptcp88/include/linux/percpu.h \
    $(wildcard include/config/need/per/cpu/embed/first/chunk.h) \
    $(wildcard include/config/need/per/cpu/page/first/chunk.h) \
  /home/teto/mptcp88/include/linux/pfn.h \
  /home/teto/mptcp88/include/linux/sysctl.h \
    $(wildcard include/config/sysctl.h) \
  /home/teto/mptcp88/include/uapi/linux/sysctl.h \
  /home/teto/mptcp88/include/linux/elf.h \
  /home/teto/mptcp88/arch/x86/include/asm/elf.h \
  /home/teto/mptcp88/arch/x86/include/asm/user.h \
  /home/teto/mptcp88/arch/x86/include/asm/user_64.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/auxvec.h \
  /home/teto/mptcp88/arch/x86/include/asm/vdso.h \
  /home/teto/mptcp88/include/uapi/linux/elf.h \
  /home/teto/mptcp88/include/uapi/linux/elf-em.h \
  /home/teto/mptcp88/include/linux/kobject.h \
  /home/teto/mptcp88/include/linux/sysfs.h \
  /home/teto/mptcp88/include/linux/kobject_ns.h \
  /home/teto/mptcp88/include/linux/kref.h \
  /home/teto/mptcp88/include/linux/moduleparam.h \
    $(wildcard include/config/alpha.h) \
    $(wildcard include/config/ia64.h) \
    $(wildcard include/config/ppc64.h) \
  /home/teto/mptcp88/include/linux/tracepoint.h \
  /home/teto/mptcp88/include/linux/static_key.h \
  /home/teto/mptcp88/include/linux/jump_label.h \
    $(wildcard include/config/jump/label.h) \
  /home/teto/mptcp88/arch/x86/include/asm/module.h \
    $(wildcard include/config/m586.h) \
    $(wildcard include/config/m586tsc.h) \
    $(wildcard include/config/m586mmx.h) \
    $(wildcard include/config/mcore2.h) \
    $(wildcard include/config/m686.h) \
    $(wildcard include/config/mpentiumii.h) \
    $(wildcard include/config/mpentiumiii.h) \
    $(wildcard include/config/mpentiumm.h) \
    $(wildcard include/config/mpentium4.h) \
    $(wildcard include/config/mk6.h) \
    $(wildcard include/config/mk8.h) \
    $(wildcard include/config/melan.h) \
    $(wildcard include/config/mcrusoe.h) \
    $(wildcard include/config/mefficeon.h) \
    $(wildcard include/config/mwinchipc6.h) \
    $(wildcard include/config/mwinchip3d.h) \
    $(wildcard include/config/mcyrixiii.h) \
    $(wildcard include/config/mviac3/2.h) \
    $(wildcard include/config/mviac7.h) \
    $(wildcard include/config/mgeodegx1.h) \
    $(wildcard include/config/mgeode/lx.h) \
  /home/teto/mptcp88/include/asm-generic/module.h \
    $(wildcard include/config/have/mod/arch/specific.h) \
    $(wildcard include/config/modules/use/elf/rel.h) \
    $(wildcard include/config/modules/use/elf/rela.h) \
  /home/teto/mptcp88/include/net/mptcp.h \
    $(wildcard include/config/mptcp.h) \
  /home/teto/mptcp88/include/linux/inetdevice.h \
  /home/teto/mptcp88/include/uapi/linux/if.h \
  /home/teto/mptcp88/include/linux/socket.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/socket.h \
  /home/teto/mptcp88/include/uapi/asm-generic/socket.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/sockios.h \
  /home/teto/mptcp88/include/uapi/asm-generic/sockios.h \
  /home/teto/mptcp88/include/uapi/linux/sockios.h \
  /home/teto/mptcp88/include/linux/uio.h \
  /home/teto/mptcp88/include/uapi/linux/uio.h \
  /home/teto/mptcp88/include/uapi/linux/socket.h \
  /home/teto/mptcp88/include/uapi/linux/hdlc/ioctl.h \
  /home/teto/mptcp88/include/linux/ip.h \
  /home/teto/mptcp88/include/linux/skbuff.h \
    $(wildcard include/config/nf/conntrack.h) \
    $(wildcard include/config/bridge/netfilter.h) \
    $(wildcard include/config/nf/defrag/ipv4.h) \
    $(wildcard include/config/nf/defrag/ipv6.h) \
    $(wildcard include/config/xfrm.h) \
    $(wildcard include/config/net/sched.h) \
    $(wildcard include/config/net/cls/act.h) \
    $(wildcard include/config/ipv6/ndisc/nodetype.h) \
    $(wildcard include/config/net/dma.h) \
    $(wildcard include/config/net/rx/busy/poll.h) \
    $(wildcard include/config/network/secmark.h) \
    $(wildcard include/config/network/phy/timestamping.h) \
    $(wildcard include/config/netfilter/xt/target/trace.h) \
  /home/teto/mptcp88/include/linux/kmemcheck.h \
  /home/teto/mptcp88/include/linux/mm_types.h \
    $(wildcard include/config/split/ptlock/cpus.h) \
    $(wildcard include/config/have/cmpxchg/double.h) \
    $(wildcard include/config/have/aligned/struct/page.h) \
    $(wildcard include/config/want/page/debug/flags.h) \
    $(wildcard include/config/aio.h) \
    $(wildcard include/config/mm/owner.h) \
    $(wildcard include/config/mmu/notifier.h) \
    $(wildcard include/config/transparent/hugepage.h) \
  /home/teto/mptcp88/include/linux/auxvec.h \
  /home/teto/mptcp88/include/uapi/linux/auxvec.h \
  /home/teto/mptcp88/include/linux/page-debug-flags.h \
    $(wildcard include/config/page/poisoning.h) \
    $(wildcard include/config/page/guard.h) \
    $(wildcard include/config/page/debug/something/else.h) \
  /home/teto/mptcp88/include/linux/uprobes.h \
    $(wildcard include/config/arch/supports/uprobes.h) \
    $(wildcard include/config/uprobes.h) \
  /home/teto/mptcp88/arch/x86/include/asm/uprobes.h \
  /home/teto/mptcp88/include/linux/net.h \
  /home/teto/mptcp88/include/linux/random.h \
    $(wildcard include/config/arch/random.h) \
  /home/teto/mptcp88/include/uapi/linux/random.h \
  /home/teto/mptcp88/include/linux/irqnr.h \
    $(wildcard include/config/generic/hardirqs.h) \
  /home/teto/mptcp88/include/uapi/linux/irqnr.h \
  /home/teto/mptcp88/arch/x86/include/asm/archrandom.h \
  /home/teto/mptcp88/include/linux/fcntl.h \
  /home/teto/mptcp88/include/uapi/linux/fcntl.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/fcntl.h \
  /home/teto/mptcp88/include/uapi/asm-generic/fcntl.h \
  /home/teto/mptcp88/include/uapi/linux/net.h \
  /home/teto/mptcp88/include/linux/textsearch.h \
  /home/teto/mptcp88/include/linux/slab.h \
    $(wildcard include/config/slab/debug.h) \
    $(wildcard include/config/failslab.h) \
    $(wildcard include/config/slob.h) \
    $(wildcard include/config/slab.h) \
    $(wildcard include/config/slub.h) \
    $(wildcard include/config/debug/slab.h) \
  /home/teto/mptcp88/include/linux/slub_def.h \
    $(wildcard include/config/slub/stats.h) \
    $(wildcard include/config/memcg/kmem.h) \
    $(wildcard include/config/slub/debug.h) \
  /home/teto/mptcp88/include/linux/kmemleak.h \
    $(wildcard include/config/debug/kmemleak.h) \
  /home/teto/mptcp88/include/net/checksum.h \
  /home/teto/mptcp88/arch/x86/include/asm/uaccess.h \
    $(wildcard include/config/x86/intel/usercopy.h) \
  /home/teto/mptcp88/arch/x86/include/asm/smap.h \
    $(wildcard include/config/x86/smap.h) \
  /home/teto/mptcp88/arch/x86/include/asm/uaccess_64.h \
  /home/teto/mptcp88/arch/x86/include/asm/checksum.h \
  /home/teto/mptcp88/arch/x86/include/asm/checksum_64.h \
  /home/teto/mptcp88/include/linux/dmaengine.h \
    $(wildcard include/config/async/tx/enable/channel/switch.h) \
    $(wildcard include/config/rapidio/dma/engine.h) \
    $(wildcard include/config/dma/engine.h) \
    $(wildcard include/config/async/tx/dma.h) \
  /home/teto/mptcp88/include/linux/device.h \
    $(wildcard include/config/debug/devres.h) \
    $(wildcard include/config/pinctrl.h) \
    $(wildcard include/config/devtmpfs.h) \
    $(wildcard include/config/sysfs/deprecated.h) \
  /home/teto/mptcp88/include/linux/klist.h \
  /home/teto/mptcp88/include/linux/pinctrl/devinfo.h \
  /home/teto/mptcp88/include/linux/ratelimit.h \
  /home/teto/mptcp88/arch/x86/include/asm/device.h \
    $(wildcard include/config/x86/dev/dma/ops.h) \
    $(wildcard include/config/intel/iommu.h) \
    $(wildcard include/config/amd/iommu.h) \
  /home/teto/mptcp88/include/linux/pm_wakeup.h \
  /home/teto/mptcp88/include/linux/scatterlist.h \
    $(wildcard include/config/debug/sg.h) \
  /home/teto/mptcp88/include/linux/mm.h \
    $(wildcard include/config/ppc.h) \
    $(wildcard include/config/parisc.h) \
    $(wildcard include/config/metag.h) \
    $(wildcard include/config/stack/growsup.h) \
    $(wildcard include/config/ksm.h) \
    $(wildcard include/config/debug/vm/rb.h) \
    $(wildcard include/config/arch/uses/numa/prot/none.h) \
    $(wildcard include/config/debug/pagealloc.h) \
    $(wildcard include/config/hugetlbfs.h) \
  /home/teto/mptcp88/include/linux/debug_locks.h \
    $(wildcard include/config/debug/locking/api/selftests.h) \
  /home/teto/mptcp88/include/linux/bit_spinlock.h \
  /home/teto/mptcp88/include/linux/shrinker.h \
  /home/teto/mptcp88/arch/x86/include/asm/pgtable.h \
  /home/teto/mptcp88/arch/x86/include/asm/pgtable_64.h \
  /home/teto/mptcp88/include/asm-generic/pgtable.h \
    $(wildcard include/config/have/arch/soft/dirty.h) \
  /home/teto/mptcp88/include/linux/page-flags.h \
    $(wildcard include/config/pageflags/extended.h) \
    $(wildcard include/config/arch/uses/pg/uncached.h) \
    $(wildcard include/config/memory/failure.h) \
    $(wildcard include/config/swap.h) \
  /home/teto/mptcp88/include/linux/huge_mm.h \
  /home/teto/mptcp88/include/linux/vmstat.h \
    $(wildcard include/config/vm/event/counters.h) \
  /home/teto/mptcp88/include/linux/vm_event_item.h \
    $(wildcard include/config/migration.h) \
  /home/teto/mptcp88/arch/x86/include/asm/scatterlist.h \
  /home/teto/mptcp88/include/asm-generic/scatterlist.h \
    $(wildcard include/config/need/sg/dma/length.h) \
  /home/teto/mptcp88/include/linux/hrtimer.h \
    $(wildcard include/config/high/res/timers.h) \
    $(wildcard include/config/timerfd.h) \
  /home/teto/mptcp88/include/linux/timerqueue.h \
  /home/teto/mptcp88/include/linux/dma-mapping.h \
    $(wildcard include/config/has/dma.h) \
    $(wildcard include/config/arch/has/dma/set/coherent/mask.h) \
    $(wildcard include/config/have/dma/attrs.h) \
    $(wildcard include/config/need/dma/map/state.h) \
  /home/teto/mptcp88/include/linux/dma-attrs.h \
  /home/teto/mptcp88/include/linux/dma-direction.h \
  /home/teto/mptcp88/arch/x86/include/asm/dma-mapping.h \
    $(wildcard include/config/isa.h) \
    $(wildcard include/config/x86/dma/remap.h) \
  /home/teto/mptcp88/include/linux/dma-debug.h \
    $(wildcard include/config/dma/api/debug.h) \
  /home/teto/mptcp88/arch/x86/include/asm/swiotlb.h \
    $(wildcard include/config/swiotlb.h) \
  /home/teto/mptcp88/include/linux/swiotlb.h \
  /home/teto/mptcp88/include/asm-generic/dma-coherent.h \
    $(wildcard include/config/have/generic/dma/coherent.h) \
  /home/teto/mptcp88/include/linux/dma-contiguous.h \
    $(wildcard include/config/cma/areas.h) \
  /home/teto/mptcp88/include/asm-generic/dma-mapping-common.h \
  /home/teto/mptcp88/include/linux/netdev_features.h \
  /home/teto/mptcp88/include/net/flow_keys.h \
  /home/teto/mptcp88/include/uapi/linux/ip.h \
  /home/teto/mptcp88/include/linux/netdevice.h \
    $(wildcard include/config/dcb.h) \
    $(wildcard include/config/wlan.h) \
    $(wildcard include/config/ax25.h) \
    $(wildcard include/config/mac80211/mesh.h) \
    $(wildcard include/config/net/ipip.h) \
    $(wildcard include/config/net/ipgre.h) \
    $(wildcard include/config/ipv6/sit.h) \
    $(wildcard include/config/ipv6/tunnel.h) \
    $(wildcard include/config/rps.h) \
    $(wildcard include/config/netpoll.h) \
    $(wildcard include/config/xps.h) \
    $(wildcard include/config/bql.h) \
    $(wildcard include/config/rfs/accel.h) \
    $(wildcard include/config/fcoe.h) \
    $(wildcard include/config/net/poll/controller.h) \
    $(wildcard include/config/libfcoe.h) \
    $(wildcard include/config/wireless/ext.h) \
    $(wildcard include/config/vlan/8021q.h) \
    $(wildcard include/config/net/dsa.h) \
    $(wildcard include/config/net/ns.h) \
    $(wildcard include/config/netprio/cgroup.h) \
    $(wildcard include/config/net/dsa/tag/dsa.h) \
    $(wildcard include/config/net/dsa/tag/trailer.h) \
    $(wildcard include/config/netpoll/trap.h) \
    $(wildcard include/config/net/flow/limit.h) \
  /home/teto/mptcp88/include/linux/pm_qos.h \
  /home/teto/mptcp88/include/linux/plist.h \
    $(wildcard include/config/debug/pi/list.h) \
  /home/teto/mptcp88/include/linux/miscdevice.h \
  /home/teto/mptcp88/include/uapi/linux/major.h \
  /home/teto/mptcp88/include/linux/delay.h \
  /home/teto/mptcp88/arch/x86/include/asm/delay.h \
  /home/teto/mptcp88/include/asm-generic/delay.h \
  /home/teto/mptcp88/include/linux/rculist.h \
  /home/teto/mptcp88/include/linux/dynamic_queue_limits.h \
  /home/teto/mptcp88/include/linux/ethtool.h \
  /home/teto/mptcp88/include/linux/compat.h \
    $(wildcard include/config/compat/old/sigaction.h) \
    $(wildcard include/config/odd/rt/sigaction.h) \
  /home/teto/mptcp88/include/linux/sem.h \
    $(wildcard include/config/sysvipc.h) \
  /home/teto/mptcp88/include/uapi/linux/sem.h \
  /home/teto/mptcp88/include/linux/ipc.h \
  /home/teto/mptcp88/include/uapi/linux/ipc.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/ipcbuf.h \
  /home/teto/mptcp88/include/uapi/asm-generic/ipcbuf.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/sembuf.h \
  /home/teto/mptcp88/include/linux/fs.h \
    $(wildcard include/config/fs/posix/acl.h) \
    $(wildcard include/config/security.h) \
    $(wildcard include/config/quota.h) \
    $(wildcard include/config/fsnotify.h) \
    $(wildcard include/config/ima.h) \
    $(wildcard include/config/epoll.h) \
    $(wildcard include/config/debug/writecount.h) \
    $(wildcard include/config/file/locking.h) \
    $(wildcard include/config/auditsyscall.h) \
    $(wildcard include/config/block.h) \
    $(wildcard include/config/fs/xip.h) \
  /home/teto/mptcp88/include/linux/kdev_t.h \
  /home/teto/mptcp88/include/uapi/linux/kdev_t.h \
  /home/teto/mptcp88/include/linux/dcache.h \
  /home/teto/mptcp88/include/linux/rculist_bl.h \
  /home/teto/mptcp88/include/linux/list_bl.h \
  /home/teto/mptcp88/include/linux/lockref.h \
  /home/teto/mptcp88/include/linux/path.h \
  /home/teto/mptcp88/include/linux/llist.h \
    $(wildcard include/config/arch/have/nmi/safe/cmpxchg.h) \
  /home/teto/mptcp88/include/linux/radix-tree.h \
  /home/teto/mptcp88/include/linux/pid.h \
  /home/teto/mptcp88/include/linux/capability.h \
  /home/teto/mptcp88/include/uapi/linux/capability.h \
  /home/teto/mptcp88/include/linux/semaphore.h \
  /home/teto/mptcp88/include/uapi/linux/fiemap.h \
  /home/teto/mptcp88/include/linux/migrate_mode.h \
  /home/teto/mptcp88/include/linux/percpu-rwsem.h \
  /home/teto/mptcp88/include/linux/blk_types.h \
    $(wildcard include/config/blk/cgroup.h) \
    $(wildcard include/config/blk/dev/integrity.h) \
  /home/teto/mptcp88/include/uapi/linux/fs.h \
  /home/teto/mptcp88/include/uapi/linux/limits.h \
  /home/teto/mptcp88/include/linux/quota.h \
    $(wildcard include/config/quota/netlink/interface.h) \
  /home/teto/mptcp88/include/linux/percpu_counter.h \
  /home/teto/mptcp88/include/uapi/linux/dqblk_xfs.h \
  /home/teto/mptcp88/include/linux/dqblk_v1.h \
  /home/teto/mptcp88/include/linux/dqblk_v2.h \
  /home/teto/mptcp88/include/linux/dqblk_qtree.h \
  /home/teto/mptcp88/include/linux/projid.h \
  /home/teto/mptcp88/include/uapi/linux/quota.h \
  /home/teto/mptcp88/include/linux/nfs_fs_i.h \
  /home/teto/mptcp88/include/uapi/linux/aio_abi.h \
  /home/teto/mptcp88/arch/x86/include/asm/compat.h \
    $(wildcard include/config/x86/x32/abi.h) \
  /home/teto/mptcp88/include/linux/sched.h \
    $(wildcard include/config/sched/debug.h) \
    $(wildcard include/config/no/hz/common.h) \
    $(wildcard include/config/lockup/detector.h) \
    $(wildcard include/config/core/dump/default/elf/headers.h) \
    $(wildcard include/config/sched/autogroup.h) \
    $(wildcard include/config/virt/cpu/accounting/native.h) \
    $(wildcard include/config/bsd/process/acct.h) \
    $(wildcard include/config/taskstats.h) \
    $(wildcard include/config/audit.h) \
    $(wildcard include/config/cgroups.h) \
    $(wildcard include/config/inotify/user.h) \
    $(wildcard include/config/fanotify.h) \
    $(wildcard include/config/posix/mqueue.h) \
    $(wildcard include/config/keys.h) \
    $(wildcard include/config/perf/events.h) \
    $(wildcard include/config/schedstats.h) \
    $(wildcard include/config/task/delay/acct.h) \
    $(wildcard include/config/fair/group/sched.h) \
    $(wildcard include/config/rt/group/sched.h) \
    $(wildcard include/config/cgroup/sched.h) \
    $(wildcard include/config/blk/dev/io/trace.h) \
    $(wildcard include/config/rcu/boost.h) \
    $(wildcard include/config/compat/brk.h) \
    $(wildcard include/config/virt/cpu/accounting/gen.h) \
    $(wildcard include/config/detect/hung/task.h) \
    $(wildcard include/config/rt/mutexes.h) \
    $(wildcard include/config/task/xacct.h) \
    $(wildcard include/config/cpusets.h) \
    $(wildcard include/config/futex.h) \
    $(wildcard include/config/fault/injection.h) \
    $(wildcard include/config/latencytop.h) \
    $(wildcard include/config/function/graph/tracer.h) \
    $(wildcard include/config/bcache.h) \
    $(wildcard include/config/have/unstable/sched/clock.h) \
    $(wildcard include/config/irq/time/accounting.h) \
    $(wildcard include/config/no/hz/full.h) \
  /home/teto/mptcp88/include/uapi/linux/sched.h \
  /home/teto/mptcp88/arch/x86/include/asm/cputime.h \
  /home/teto/mptcp88/include/asm-generic/cputime.h \
    $(wildcard include/config/virt/cpu/accounting.h) \
  /home/teto/mptcp88/include/asm-generic/cputime_jiffies.h \
  /home/teto/mptcp88/include/linux/signal.h \
    $(wildcard include/config/old/sigaction.h) \
  /home/teto/mptcp88/include/uapi/linux/signal.h \
  /home/teto/mptcp88/arch/x86/include/asm/signal.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/signal.h \
  /home/teto/mptcp88/include/uapi/asm-generic/signal-defs.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/siginfo.h \
  /home/teto/mptcp88/include/asm-generic/siginfo.h \
  /home/teto/mptcp88/include/uapi/asm-generic/siginfo.h \
  /home/teto/mptcp88/include/linux/proportions.h \
  /home/teto/mptcp88/include/linux/seccomp.h \
    $(wildcard include/config/seccomp.h) \
    $(wildcard include/config/seccomp/filter.h) \
  /home/teto/mptcp88/include/uapi/linux/seccomp.h \
  /home/teto/mptcp88/arch/x86/include/asm/seccomp.h \
  /home/teto/mptcp88/arch/x86/include/asm/seccomp_64.h \
  /home/teto/mptcp88/include/uapi/linux/unistd.h \
  /home/teto/mptcp88/arch/x86/include/asm/unistd.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/unistd.h \
  arch/x86/include/generated/uapi/asm/unistd_64.h \
  arch/x86/include/generated/asm/unistd_64_x32.h \
  /home/teto/mptcp88/arch/x86/include/asm/ia32_unistd.h \
  arch/x86/include/generated/asm/unistd_32_ia32.h \
  /home/teto/mptcp88/include/linux/rtmutex.h \
    $(wildcard include/config/debug/rt/mutexes.h) \
  /home/teto/mptcp88/include/linux/resource.h \
  /home/teto/mptcp88/include/uapi/linux/resource.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/resource.h \
  /home/teto/mptcp88/include/asm-generic/resource.h \
  /home/teto/mptcp88/include/uapi/asm-generic/resource.h \
  /home/teto/mptcp88/include/linux/task_io_accounting.h \
    $(wildcard include/config/task/io/accounting.h) \
  /home/teto/mptcp88/include/linux/latencytop.h \
  /home/teto/mptcp88/include/linux/cred.h \
    $(wildcard include/config/debug/credentials.h) \
  /home/teto/mptcp88/include/linux/key.h \
  /home/teto/mptcp88/include/linux/selinux.h \
    $(wildcard include/config/security/selinux.h) \
  /home/teto/mptcp88/arch/x86/include/asm/user32.h \
  /home/teto/mptcp88/include/uapi/linux/ethtool.h \
  /home/teto/mptcp88/include/linux/if_ether.h \
  /home/teto/mptcp88/include/uapi/linux/if_ether.h \
  /home/teto/mptcp88/include/net/net_namespace.h \
    $(wildcard include/config/ip/sctp.h) \
    $(wildcard include/config/ip/dccp.h) \
    $(wildcard include/config/netfilter.h) \
    $(wildcard include/config/wext/core.h) \
    $(wildcard include/config/ip/vs.h) \
  /home/teto/mptcp88/include/net/netns/core.h \
  /home/teto/mptcp88/include/net/netns/mib.h \
    $(wildcard include/config/xfrm/statistics.h) \
  /home/teto/mptcp88/include/net/snmp.h \
  /home/teto/mptcp88/include/uapi/linux/snmp.h \
  /home/teto/mptcp88/include/linux/u64_stats_sync.h \
  /home/teto/mptcp88/include/net/netns/unix.h \
  /home/teto/mptcp88/include/net/netns/packet.h \
  /home/teto/mptcp88/include/net/netns/ipv4.h \
    $(wildcard include/config/ip/multiple/tables.h) \
    $(wildcard include/config/ip/route/classid.h) \
    $(wildcard include/config/ip/mroute.h) \
    $(wildcard include/config/ip/mroute/multiple/tables.h) \
  /home/teto/mptcp88/include/net/inet_frag.h \
  /home/teto/mptcp88/include/net/netns/ipv6.h \
    $(wildcard include/config/ipv6/multiple/tables.h) \
    $(wildcard include/config/ipv6/mroute.h) \
    $(wildcard include/config/ipv6/mroute/multiple/tables.h) \
  /home/teto/mptcp88/include/net/dst_ops.h \
  /home/teto/mptcp88/include/net/netns/mptcp.h \
  /home/teto/mptcp88/include/net/netns/sctp.h \
  /home/teto/mptcp88/include/net/netns/dccp.h \
  /home/teto/mptcp88/include/net/netns/netfilter.h \
  /home/teto/mptcp88/include/linux/proc_fs.h \
  /home/teto/mptcp88/include/linux/netfilter.h \
    $(wildcard include/config/nf/nat/needed.h) \
  /home/teto/mptcp88/include/linux/in.h \
  /home/teto/mptcp88/include/uapi/linux/in.h \
  /home/teto/mptcp88/include/linux/in6.h \
  /home/teto/mptcp88/include/uapi/linux/in6.h \
  /home/teto/mptcp88/include/uapi/linux/netfilter.h \
  /home/teto/mptcp88/include/net/flow.h \
  /home/teto/mptcp88/include/net/netns/x_tables.h \
    $(wildcard include/config/bridge/nf/ebtables.h) \
    $(wildcard include/config/ip/nf/target/ulog.h) \
    $(wildcard include/config/bridge/ebt/ulog.h) \
  /home/teto/mptcp88/include/net/netns/conntrack.h \
    $(wildcard include/config/nf/conntrack/proc/compat.h) \
    $(wildcard include/config/nf/conntrack/labels.h) \
  /home/teto/mptcp88/include/linux/list_nulls.h \
  /home/teto/mptcp88/include/linux/netfilter/nf_conntrack_tcp.h \
  /home/teto/mptcp88/include/uapi/linux/netfilter/nf_conntrack_tcp.h \
  /home/teto/mptcp88/include/net/netns/xfrm.h \
  /home/teto/mptcp88/include/uapi/linux/xfrm.h \
  /home/teto/mptcp88/include/linux/seq_file_net.h \
  /home/teto/mptcp88/include/linux/seq_file.h \
  /home/teto/mptcp88/include/net/dsa.h \
  /home/teto/mptcp88/include/net/netprio_cgroup.h \
  /home/teto/mptcp88/include/linux/cgroup.h \
  /home/teto/mptcp88/include/uapi/linux/cgroupstats.h \
  /home/teto/mptcp88/include/uapi/linux/taskstats.h \
  /home/teto/mptcp88/include/linux/prio_heap.h \
  /home/teto/mptcp88/include/linux/idr.h \
  /home/teto/mptcp88/include/linux/xattr.h \
  /home/teto/mptcp88/include/uapi/linux/xattr.h \
  /home/teto/mptcp88/include/linux/percpu-refcount.h \
  /home/teto/mptcp88/include/linux/cgroup_subsys.h \
    $(wildcard include/config/cgroup/debug.h) \
    $(wildcard include/config/cgroup/cpuacct.h) \
    $(wildcard include/config/cgroup/device.h) \
    $(wildcard include/config/cgroup/freezer.h) \
    $(wildcard include/config/net/cls/cgroup.h) \
    $(wildcard include/config/cgroup/perf.h) \
    $(wildcard include/config/cgroup/hugetlb.h) \
  /home/teto/mptcp88/include/linux/hardirq.h \
  /home/teto/mptcp88/include/linux/ftrace_irq.h \
    $(wildcard include/config/ftrace/nmi/enter.h) \
  /home/teto/mptcp88/include/linux/vtime.h \
  /home/teto/mptcp88/arch/x86/include/asm/hardirq.h \
    $(wildcard include/config/x86/thermal/vector.h) \
    $(wildcard include/config/x86/mce/threshold.h) \
  /home/teto/mptcp88/include/linux/irq.h \
    $(wildcard include/config/generic/pending/irq.h) \
    $(wildcard include/config/hardirqs/sw/resend.h) \
  /home/teto/mptcp88/include/linux/irqreturn.h \
  /home/teto/mptcp88/arch/x86/include/asm/irq.h \
  /home/teto/mptcp88/arch/x86/include/asm/irq_regs.h \
  /home/teto/mptcp88/include/linux/irqdesc.h \
    $(wildcard include/config/irq/preflow/fasteoi.h) \
    $(wildcard include/config/sparse/irq.h) \
  /home/teto/mptcp88/arch/x86/include/asm/hw_irq.h \
    $(wildcard include/config/irq/remap.h) \
  /home/teto/mptcp88/include/linux/profile.h \
    $(wildcard include/config/profiling.h) \
  /home/teto/mptcp88/arch/x86/include/asm/sections.h \
    $(wildcard include/config/debug/rodata.h) \
  /home/teto/mptcp88/include/asm-generic/sections.h \
  /home/teto/mptcp88/include/uapi/linux/neighbour.h \
  /home/teto/mptcp88/include/linux/netlink.h \
  /home/teto/mptcp88/include/net/scm.h \
    $(wildcard include/config/security/network.h) \
  /home/teto/mptcp88/include/linux/security.h \
    $(wildcard include/config/security/path.h) \
    $(wildcard include/config/security/network/xfrm.h) \
    $(wildcard include/config/securityfs.h) \
    $(wildcard include/config/security/yama.h) \
  /home/teto/mptcp88/include/linux/nsproxy.h \
  /home/teto/mptcp88/include/uapi/linux/netlink.h \
  /home/teto/mptcp88/include/uapi/linux/netdevice.h \
  /home/teto/mptcp88/include/uapi/linux/if_packet.h \
  /home/teto/mptcp88/include/linux/if_link.h \
  /home/teto/mptcp88/include/uapi/linux/if_link.h \
  /home/teto/mptcp88/include/linux/rtnetlink.h \
  /home/teto/mptcp88/include/uapi/linux/rtnetlink.h \
  /home/teto/mptcp88/include/uapi/linux/if_addr.h \
  /home/teto/mptcp88/include/linux/ipv6.h \
    $(wildcard include/config/ipv6/privacy.h) \
    $(wildcard include/config/ipv6/router/pref.h) \
    $(wildcard include/config/ipv6/route/info.h) \
    $(wildcard include/config/ipv6/optimistic/dad.h) \
    $(wildcard include/config/ipv6/mip6.h) \
    $(wildcard include/config/ipv6/subtrees.h) \
  /home/teto/mptcp88/include/uapi/linux/ipv6.h \
  /home/teto/mptcp88/include/linux/icmpv6.h \
  /home/teto/mptcp88/include/uapi/linux/icmpv6.h \
  /home/teto/mptcp88/include/linux/tcp.h \
    $(wildcard include/config/tcp/md5sig.h) \
  /home/teto/mptcp88/include/net/sock.h \
    $(wildcard include/config/net.h) \
  /home/teto/mptcp88/include/linux/uaccess.h \
  /home/teto/mptcp88/include/linux/memcontrol.h \
    $(wildcard include/config/memcg/swap.h) \
    $(wildcard include/config/inet.h) \
  /home/teto/mptcp88/include/linux/res_counter.h \
  /home/teto/mptcp88/include/linux/aio.h \
  /home/teto/mptcp88/include/linux/filter.h \
    $(wildcard include/config/bpf/jit.h) \
  /home/teto/mptcp88/include/uapi/linux/filter.h \
  /home/teto/mptcp88/include/linux/rculist_nulls.h \
  /home/teto/mptcp88/include/linux/poll.h \
  /home/teto/mptcp88/include/uapi/linux/poll.h \
  /home/teto/mptcp88/arch/x86/include/uapi/asm/poll.h \
  /home/teto/mptcp88/include/uapi/asm-generic/poll.h \
  /home/teto/mptcp88/include/net/dst.h \
  /home/teto/mptcp88/include/net/neighbour.h \
  /home/teto/mptcp88/include/net/rtnetlink.h \
  /home/teto/mptcp88/include/net/netlink.h \
  /home/teto/mptcp88/include/net/inet_connection_sock.h \
  /home/teto/mptcp88/include/net/inet_sock.h \
  /home/teto/mptcp88/include/linux/jhash.h \
  /home/teto/mptcp88/include/linux/unaligned/packed_struct.h \
  /home/teto/mptcp88/include/net/request_sock.h \
  /home/teto/mptcp88/include/net/netns/hash.h \
  /home/teto/mptcp88/include/net/inet_timewait_sock.h \
  /home/teto/mptcp88/include/net/tcp_states.h \
  /home/teto/mptcp88/include/net/timewait_sock.h \
  /home/teto/mptcp88/include/uapi/linux/tcp.h \
  /home/teto/mptcp88/include/linux/udp.h \
  /home/teto/mptcp88/include/uapi/linux/udp.h \
  /home/teto/mptcp88/include/linux/netpoll.h \
  /home/teto/mptcp88/include/linux/interrupt.h \
    $(wildcard include/config/irq/forced/threading.h) \
    $(wildcard include/config/generic/irq/probe.h) \
  /home/teto/mptcp88/arch/x86/include/asm/unaligned.h \
  /home/teto/mptcp88/include/linux/unaligned/access_ok.h \
  /home/teto/mptcp88/include/linux/unaligned/generic.h \
  /home/teto/mptcp88/include/crypto/hash.h \
  /home/teto/mptcp88/include/linux/crypto.h \
  /home/teto/mptcp88/include/net/tcp.h \
    $(wildcard include/config/syn/cookies.h) \
  /home/teto/mptcp88/include/linux/cryptohash.h \
  /home/teto/mptcp88/include/net/inet_hashtables.h \
  /home/teto/mptcp88/include/net/route.h \
  /home/teto/mptcp88/include/net/inetpeer.h \
  /home/teto/mptcp88/include/net/ipv6.h \
    $(wildcard include/config/have/efficient/unaligned/access.h) \
  /home/teto/mptcp88/include/net/if_inet6.h \
  /home/teto/mptcp88/include/net/ndisc.h \
  /home/teto/mptcp88/include/linux/if_arp.h \
    $(wildcard include/config/firewire/net.h) \
  /home/teto/mptcp88/include/uapi/linux/if_arp.h \
  /home/teto/mptcp88/include/linux/hash.h \
  /home/teto/mptcp88/include/uapi/linux/in_route.h \
  /home/teto/mptcp88/include/uapi/linux/route.h \
  /home/teto/mptcp88/include/net/ip.h \
  /home/teto/mptcp88/include/net/inet_ecn.h \
  /home/teto/mptcp88/include/net/dsfield.h \
  /home/teto/mptcp88/include/net/mptcp_v4.h \
  /home/teto/mptcp88/include/linux/genetlink.h \
  /home/teto/mptcp88/include/uapi/linux/genetlink.h \
  /home/teto/mptcp88/include/linux/inet.h \
  /home/teto/mptcp88/include/net/genetlink.h \
  /home/teto/xp_couplage/module_v3/mptcp_netlink.h \

/home/teto/xp_couplage/module_v3/mptcp_nl_simple.o: $(deps_/home/teto/xp_couplage/module_v3/mptcp_nl_simple.o)

$(deps_/home/teto/xp_couplage/module_v3/mptcp_nl_simple.o):
