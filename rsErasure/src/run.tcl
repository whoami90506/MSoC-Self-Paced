############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2019 Xilinx, Inc. All Rights Reserved.
############################################################
open_project hls_rsErasure
set_top rs_erasure
add_files ./rs_erasure.c
add_files ./rs_erasure.h
add_files -tb ./tb_rs_erasure.c
add_files -tb ./tv_rs_erasure_in.txt
add_files -tb ./tv_rs_erasure_mout.txt
open_solution "solution1"
set_part {xc7z020-clg484-1}
create_clock -period 5 -name default
# config_export -format ip_catalog -rtl verilog
source "./directives.tcl"
csim_design
csynth_design
cosim_design -trace_level all -tool xsim
export_design -rtl verilog -format ip_catalog
