#! /usr/bin/env python

import numpy as np

with open('day6_input.txt') as fh:
	coord_list = fh.read().split('\n')

# Convert to numpy
clist2 = {}
maxx = 0
maxy = 0
for coord in range(len(coord_list)):
    pair = coord_list[coord].split(',')
    x = int(pair[0])
    y = int(pair[1])
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y
    clist2[coord] = [x,y]

# print clist2

grid = np.zeros([maxx, maxy])
print grid.shape

keylist = clist2.keys()
for each in range(len(keylist)):
    key = keylist[each]
    x, y = clist2[key]
    