#!/bin/sh

## Uncomment the following line to install packages if they're missing
###sudo apt-get install ntp; sudo apt-get install ntpdate;


# The -gq tells the ntp daemon to correct the time regardless of the offset (g) and exit immediately (q) after setting the time.
sudo service ntp stop
sudo ntpd -gq
sudo service ntp start
