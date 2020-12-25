
open_project fir.proj -reset
add_file block_fir.c
add_file -tb block_fir-top.c

set_top block_fir

open_solution solution -reset

set_part xc7z020-clg484-1

create_clock -period 5

csynth_design
cosim_design
export_design -format ip_catalog