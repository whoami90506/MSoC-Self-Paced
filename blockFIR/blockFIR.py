
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

    ol = Overlay("/home/xilinx/IPBitFile/blockFIR.bit")
    ipFIRN11 = ol.block_fir_0

    # fiSamples = open("samples_triangular_wave.txt", "r+")
    inBuffer0 = allocate(shape=(256,), dtype=np.int32)
    outBuffer0 = allocate(shape=(256,), dtype=np.int32)
    for i in range(256):
        inBuffer0[i] = i

    numTaps = 16
    n32Taps = [1, 2, 0, -3, 0, 4, -5, 0, 1, -2, 0, -3, 0, 4, -5, 0]
    n32DCGain = 0
    timeKernelStart = time()
    print("setting hwh")
    for i in range(numTaps):
        # n32DCGain = n32DCGain + n32Taps[i]
        ipFIRN11.write(0x40 + i * 4, n32Taps[i])
    # if n32DCGain < 0:
    #     n32DCGain = 0 - n32DCGain
    ipFIRN11.write(0x80, len(inBuffer0) * 4)
    ipFIRN11.write(0x10, inBuffer0.device_address)
    ipFIRN11.write(0x18, outBuffer0.device_address)
    ipFIRN11.write(0x00, 0x01)
    print("start kernel")
    while (ipFIRN11.read(0x00) & 0x4) == 0x0:   # idle = 1
        continue
    timeKernelEnd = time()
    print("Kernel execution time: " + str(timeKernelEnd - timeKernelStart) + " s")
    
    for i in range(256):
        print("iter %d: result = %d\n" % (i, outBuffer0[i]))
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
    # if(outBuffer0[255]==)
    print("============================")
    print("Exit process")

