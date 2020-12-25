############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2019 Xilinx, Inc. All Rights Reserved.
############################################################


open_project hls_matrixmultiplication -reset
add_file matrixmultiplication.c
add_file -tb matrixmultiplication-top.c
set_top matrixmul
open_solution solution1 -reset
set_part xc7z020-clg484-1
create_clock -period 5
source "./directives.tcl"
csim_design
csynth_design
cosim_design
export_design -rtl verilog -format ip_catalog

