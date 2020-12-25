
# coding: utf-8
from __future__ import print_function

import sys
import numpy as np
import random
from time import time
import matplotlib.pyplot as plt 

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFile/rsErasure.bit")
    ipFIRN11 = ol.rs_erasure_0

    # fiSamples = open("samples_triangular_wave.txt", "r+")
    outC = allocate(shape=(4,), dtype=np.int8)
    inD = allocate(shape=(12,), dtype=np.int8)
    survival_pattern = allocate(shape=(1,), dtype=np.int16)
    codeid = allocate(shape=(1,), dtype=np.int8)
    
    # errcnt = 0
    linecnt = 0
    # suberrcnt = [0, 0, 0, 0]
    sublincnt = [0, 0, 0, 0]

    with open('./tv_rs_erasure_in.txt', 'r') as f_in:
        for line in f_in:
            timeKernelStart = time()
            line = line.split('\n')[0].split()
            print("setting %dth hwh" % linecnt)
            codeid = line[0] & 3
            ipFIRN11.write(0x98, int(codeid))
            survival_pattern = line[1] & ( (1<<16) - 1 )
            ipFIRN11.write(0x90, int(survival_pattern))
            for i in range(12):
                inD[i] = line[i+2] & ( (1<<8) - 1 )
                ipFIRN11.write(0x30 + i*8, int(inD[i]))
            print("start %dth kernel" % linecnt)
            ipFIRN11.write(0x00, 0x01)
            while (ipFIRN11.read(0x00) & 0x4) == 0x0:   # idle = 1
                continue
            timeKernelEnd = time()
            print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
            sublincnt[codeid] += 1
            for i in range(4):
                outC[i] = ipFIRN11.read(0x10 + i*8)
                print(outC[i], end=' ')
            print()

    print('\npass')
    print("============================")
    print("Exit process")

