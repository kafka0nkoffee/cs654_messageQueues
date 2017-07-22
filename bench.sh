#!/bin/bash

#Perform timings of device reads for benchmark and comparison purposes.  For meaning‐
#ful  results,  this  operation should be repeated 2-3 times on an otherwise inactive
#system (no other active processes) with at least a couple of megabytes of free  mem‐
#ory.   This displays the speed of reading through the buffer cache to the disk with‐
#out any prior caching of data.  This measurement is an indication of  how  fast  the
#drive  can  sustain  sequential data reads under Linux, without any filesystem over‐
#head.  To ensure accurate measurements, the buffer cache is flushed during the  pro‐
#cessing of -t using the BLKFLSBUF ioctl.

# Gen filesize 64bytes
dd if=/dev/zero of=output_64.dat  bs=64  count=1000000

# Gen file 1kb
dd if=/dev/zero of=output_1000.dat  bs=1000  count=1000000
