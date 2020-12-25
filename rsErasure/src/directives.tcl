############################################################
## This file is generated automatically by Vivado HLS.
## Please DO NOT edit it.
## Copyright (C) 1986-2019 Xilinx, Inc. All Rights Reserved.
############################################################
set_directive_array_partition -type complete -dim 1 "rs_erasure" c
set_directive_array_partition -type complete -dim 1 "rs_erasure" d
set_directive_interface -mode s_axilite -depth 12 "rs_erasure" d
set_directive_interface -mode s_axilite "rs_erasure" codeidx
set_directive_pipeline -II 1 "rs_erasure"
set_directive_interface -mode s_axilite "rs_erasure" survival_pattern
set_directive_interface -mode s_axilite -depth 4 "rs_erasure" c
set_directive_interface -mode s_axilite "rs_erasure"
