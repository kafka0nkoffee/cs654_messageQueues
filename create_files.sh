#!/bin/bash

### Create 1GB file
if [ ! -f 1GB.zip ]; then
	wget http://ipv4.download.thinkbroadband.com/1GB.zip
fi

truncate -s 1000000000 1GB.zip


### Create 64MB file
if [ ! -f 100MB.zip ]; then
	wget http://ipv4.download.thinkbroadband.com/100MB.zip
fi

mv 100MB.zip 64MB.zip
truncate -s 64000000 64MB.zip


### Create 1kB file
cp 64MB.zip 1kB.zip
truncate -s 1000 1kB.zip


### Create 64B file
cp 1kB.zip 64B.zip
truncate -s 64 64B.zip
