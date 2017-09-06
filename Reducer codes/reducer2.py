#!/usr/bin/env python
import sys

dictionary =  {}

for line in sys.stdin:
	author,words = line.split('\t')
	dictionary.setdefault(author,{})
	key,value = words.split(':')
	value = int(value)
	dictionary[author].setdefault(key,0)
	dictionary[author][key] += value

for key in dictionary:
	sys.stdout.write("{0}\t{1}\n".format(key,dictionary[key]))

