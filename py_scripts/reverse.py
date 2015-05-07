#!/usr/bin/python
import sys
filename = sys.argv[1]
#num_lines = len(open(filename).readlines())
a = open(filename).readlines()

for line in reversed(a):
    print line 
