#!/bin/bash

# Concat the two time files
paste send.log receive.log | awk '{print $2,$4}' > calc.txt

# Calc the differences
awk '{print $2-$1}' calc.txt
