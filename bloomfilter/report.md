# Bloom Filter
<p align='right'>Team03 B05901064 林承德</p>

[Github Url](https://github.com/whoami90506/MSoC-Self-Paced/tree/master/bloomfilter)

## System level bring-up
I use Vitis platform to implement the design on U50. The data and parameter use the same ports to send. First I need to send the parameter first with a parameter flag true, and the data will be sent later. 

## Improvement
### Debug
* Some of the I/O integers are not assigned interfaces and resulted in compile error. Therefore I assigned the I/O integer the AXI Lite interface.
* The server has no header `CL/cl2.hpp`, therefore I download the [file](https://github.com/ARM-software/ComputeLibrary/blob/master/include/CL/cl2.hpp) and put it into the library.

### Array Partition
There is a global 2D array in this design as followed:
```c++
#define PARALLELISATION 8  
#define bloom_size 14

static unsigned int bloom_filter_local[PARALLELISATION][bloom_filter_size];
```
The original design only seperate first dimention, yet the second dimention is also short enough to be partitioned. Therefore I would like to try to seperate all dimentions.
```c++
// original
static unsigned int bloom_filter_local[PARALLELISATION][bloom_filter_size];
#pragma HLS ARRAY_PARTITION variable=bloom_filter_local complete dim=1

// optimize
static unsigned int bloom_filter_local[PARALLELISATION][bloom_filter_size];
#pragma HLS ARRAY_PARTITION variable=bloom_filter_local complete dim=0
```

However, the synthesis tool does not support array complete partition with size over 1024. I can not try to seperate all elements in arrays.


## HLS screenshot

### Csim
#### Origin
![](https://github.com/whoami90506/MSoC-Self-Paced/raw/master/bloomfilter/image/csim_ori.jpg)

#### Optimize
![](https://github.com/whoami90506/MSoC-Self-Paced/raw/master/bloomfilter/image/csim_opt.jpg)

### Synthesis
![](https://github.com/whoami90506/MSoC-Self-Paced/raw/master/bloomfilter/image/syn.jpg)

### Cosim
![](https://github.com/whoami90506/MSoC-Self-Paced/raw/master/bloomfilter/image/cosim.jpg)


