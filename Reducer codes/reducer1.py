#!/usr/bin/env python
import sys



dictionary =  {}

for line in sys.stdin:
    line = line.strip()
    line = line.split('\t')
    if len(line)==2: 
        key = line[0]
        value = line[1]
        dictionary.setdefault(key,{})
    

    	filename,count = value.split(',')
    	count = int(count)
    	dictionary[key].setdefault(filename,0)
    	dictionary[key][filename] += count

for r in dictionary:
    sys.stdout.write("{0}\t{1}\n".format(r,dictionary[r]))




