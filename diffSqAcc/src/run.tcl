############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2019 Xilinx, Inc. All Rights Reserved.
############################################################
open_project hls_diffSqAcc
set_top diff_sq_acc
add_files ./diff_sq_acc.cpp
add_files ./diff_sq_acc.h
add_files -tb ./diff_sq_acc_tb.cpp
open_solution "solution1"
set_part {xc7z020-clg484-1}
create_clock -period 5 -name default
# config_export -format ip_catalog -rtl verilog
source "./directives.tcl"
csim_design
csynth_design
cosim_design -trace_level all -tool xsim
export_design -rtl verilog -format ip_catalog
