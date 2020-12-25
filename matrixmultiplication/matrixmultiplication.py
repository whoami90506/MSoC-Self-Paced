
# coding: utf-8

# In[ ]:


from __future__ import print_function

import sys
import numpy as np
from time import time
import matplotlib.pyplot as plt 

sys.path.append('/home/xilinx')
from pynq import Overlay
from pynq import allocate

if __name__ == "__main__":
    print("Entry:", sys.argv[0])
    print("System argument(s):", len(sys.argv))

    print("Start of \"" + sys.argv[0] + "\"")

    ol = Overlay("/home/xilinx/IPBitFile/matrixmultiplication.bit")
    ipFIRN11 = ol.matrixmul_0

    # fiSamples = open("samples_triangular_wave.txt", "r+")
    inA = allocate(shape=(32,32), dtype=np.int32)
    inB = allocate(shape=(32,32), dtype=np.int32)
    ansAB = allocate(shape=(32,32), dtype=np.int32)
    outAB = allocate(shape=(32,32), dtype=np.int32)

    timeKernelStart = time()
    print("setting hwh")
    offset = 0
    for i in range(32):
        for j in range(32):
            inA[i][j] = i + j
            ipFIRN11.write(0x1000 + offset, i + j)
            inB[i][j] = i + j
            ipFIRN11.write(0x2000 + offset, i + j)
            offset += 4

    # numTaps = 16
    # n32Taps = [1, 2, 0, -3, 0, 4, -5, 0, 1, -2, 0, -3, 0, 4, -5, 0]
    # for i in range(numTaps):
    #     ipFIRN11.write(0x40 + i * 4, n32Taps[i])

    # ipFIRN11.write(0x80, len(inBuffer0) * 4)
    # ipFIRN11.write(0x10, inBuffer0.device_address)
    # ipFIRN11.write(0x18, outBuffer0.device_address)
    ipFIRN11.write(0x00, 0x01)
    print("start kernel")
    while (ipFIRN11.read(0x00) & 0x4) == 0x0:   # idle = 1
        continue
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    
    offset = 0
    for i in range(32):
        print()
        print(i, end='    ')
        for j in range(32):
            Res = ipFIRN11.read(0x3000 + offset)
            print(str(Res), end=' ')
            offset += 4

    print("\n\npass")
    print("============================")
    print("Exit process")

