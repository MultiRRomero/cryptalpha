#!/bin/bash

plainword=$1
cipherword=`echo $plainword | ./cryptalpha.py | cut -d= -f2`
cat alpharainbow | grep "\=$cipherword\$" | cut -d= -f1
