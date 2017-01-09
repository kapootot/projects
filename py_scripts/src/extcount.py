#!/usr/bin/python
import os
import sys
import collections

path = sys.argv[1]
list = os.listdir(path)
ext_list = []

for item in list:
    if os.path.isfile(path + item):
         ext_list.append((item.split('.'))[1])
cnt = collections.Counter(ext_list)

for i in cnt:
    print(i, cnt[i])
       
