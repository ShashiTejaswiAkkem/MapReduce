#!/usr/bin/env python
import sys
import re

dictionary =  {}

for line in sys.stdin:
	line = line.strip()
	key = line.split('\t')[0]
        value = line.split('\t')[1]
	dictionary.setdefault(key,[])
	if value not in dictionary[key]:
	    dictionary[key].append(value)
for key in dictionary:
	sys.stdout.write("{0}\t{1}\n".format(key,dictionary[key]))

