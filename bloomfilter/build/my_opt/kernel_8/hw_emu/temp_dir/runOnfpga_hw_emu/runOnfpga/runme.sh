#!/bin/sh

# 
# v++(TM)
# runme.sh: a v++-generated Runs Script for UNIX
# Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
# 

if [ -z "$PATH" ]; then
  PATH=/opt/Xilinx/Vivado/2019.2/bin:/opt/Xilinx/Vitis/2019.2/bin:/opt/Xilinx/Vitis/2019.2/bin
else
  PATH=/opt/Xilinx/Vivado/2019.2/bin:/opt/Xilinx/Vitis/2019.2/bin:/opt/Xilinx/Vitis/2019.2/bin:$PATH
fi
export PATH

if [ -z "$LD_LIBRARY_PATH" ]; then
  LD_LIBRARY_PATH=
else
  LD_LIBRARY_PATH=:$LD_LIBRARY_PATH
fi
export LD_LIBRARY_PATH

HD_PWD='/home/team03-b05064/Vitis-Tutorials/Hardware_Accelerators/Design_Tutorials/02-bloom/build/my_opt/kernel_8/hw_emu/temp_dir/runOnfpga_hw_emu/runOnfpga'
cd "$HD_PWD"

HD_LOG=runme.log
/bin/touch $HD_LOG

ISEStep="./ISEWrap.sh"
EAStep()
{
     $ISEStep $HD_LOG "$@" >> $HD_LOG 2>&1
     if [ $? -ne 0 ]
     then
         exit
     fi
}

EAStep vivado_hls -f runOnfpga.tcl -messageDb vivado_hls.pb
