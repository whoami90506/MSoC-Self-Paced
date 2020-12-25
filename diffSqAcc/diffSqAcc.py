
# coding: utf-8

# In[ ]:


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

    ol = Overlay("/home/xilinx/IPBitFile/diffSqAcc_allLite.bit")
    ipFIRN11 = ol.diff_sq_acc_0

    # fiSamples = open("samples_triangular_wave.txt", "r+")
    inA = allocate(shape=(10,), dtype=np.int32)
    inB = allocate(shape=(10,), dtype=np.int32)
    # out = allocate(shape=(10,), dtype=np.int64)
    ans = 0
    for i in range(10):
        inA[i] = random.randint(0,1023)
        inB[i] = random.randint(0,1023)
        ans += (inA[i] - inB[i]) ** 2

    timeKernelStart = time()
    print("setting hwh")
    for i in range(10):
        ipFIRN11.write(0x20 + i * 4, int(inA[i]))
        ipFIRN11.write(0x40 + i * 4, int(inB[i]))
    ipFIRN11.write(0x00, 0x01)
    print("start kernel")
    while (ipFIRN11.read(0x00) & 0x4) == 0x0:   # idle = 1
        continue
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    
    Res = ipFIRN11.read(0x60)
    print('ans =', str(Res))
    print('\npass')
    # plt.title("FIR Response")
    # plt.xlabel("Sample Point") 
    # plt.ylabel("Magnitude")
    # xSeq = range(len(inBuffer0))
    # if n32DCGain == 0:
    #     plt.plot(xSeq, inBuffer0, 'b.', xSeq, outBuffer0, 'r.')
    # else:
    #     plt.plot(xSeq, inBuffer0, 'b.', xSeq, outBuffer0 / n32DCGain, 'r.')
    # plt.grid(True)
    # plt.show() # In Jupyter, press Tab + Shift keys to show plot then redo run
    print("============================")
    print("Exit process")

