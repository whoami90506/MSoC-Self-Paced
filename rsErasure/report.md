# RsErasure
<p align='right'>Team03 B05901064 林承德</p>

[Github Url](https://github.com/whoami90506/MSoC-Self-Paced/tree/master/rsErasure)

## System level bring-up
I use PYNQ to implement the design. All of the interface is AXI Lite.

## Improvement
Since the lengths of input vectors are only 4, I use `array_partition` to change to 4 individual registers. Remove the memory protocol can largely reduce the latency from 1994 cycles to 25 cycles.

## HLS screenshot

### Synthesis
#### Origin
![](https://github.com/whoami90506/MSoC-Self-Paced/raw/master/rsErasure/image/summary_origin.png)

#### Optimize
![](https://github.com/whoami90506/MSoC-Self-Paced/raw/master/rsErasure/image/summary_opt.png)

### Simulation
![](https://github.com/whoami90506/MSoC-Self-Paced/raw/master/rsErasure/image/cosim.png)

### Result
![](https://github.com/whoami90506/MSoC-Self-Paced/raw/master/rsErasure/image/result.png)
