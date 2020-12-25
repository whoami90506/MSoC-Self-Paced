#!/bin/sh
lli=${LLVMINTERP-lli}
exec $lli \
    /home/team03-b05064/Vitis-Tutorials/Hardware_Accelerators/Design_Tutorials/02-bloom/build/my_opt/kernel_8/sw_emu/temp_dir/runOnfpga_sw_emu/runOnfpga/runOnfpga/solution/.autopilot/db/a.g.bc ${1+"$@"}
