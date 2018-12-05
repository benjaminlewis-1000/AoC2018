#! /usr/bin/env python

import re
import numpy as np

with open('day3_input.txt') as fh:
    patterns = fh.read()

# Part 1
def process_pattern(raw_pattern):
    data = re.match('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', raw_pattern)
    ID = data.group(1)
    leftedge = int(data.group(2))
    rightedge = int(leftedge) + int(data.group(4))
    topedge = int(data.group(3))
    bottomedge = int(topedge) + int(data.group(5))

    return (ID, [leftedge, rightedge, topedge, bottomedge])

patterns = patterns.split('\n')
readable_patterns = {}
leftmost = 1e9
rightmost = 0
topmost = 1e9
bottommost = 0

for i in patterns:
    ID, boundaries = process_pattern(i)
    readable_patterns[ID] = boundaries
    if boundaries[0] < leftmost:
        leftmost = boundaries[0]
    if boundaries[1] > rightmost:
        rightmost = boundaries[1]
    if boundaries[2] < topmost:
        topmost = boundaries[2]
    if boundaries[3] > bottommost:
        bottommost = boundaries[3]

print "right edge is {}, bottom edge is {}".format(rightmost, bottommost)

fabric = np.zeros([rightmost, bottommost])
for key in readable_patterns.keys():
    b = readable_patterns[key]
    fabric[b[0]:b[1], b[2]:b[3]] += 1

print "There are {} square inches claimed by more than one elf.".format( len( fabric[ np.where( fabric > 1 ) ] ) )

# Part 2 
# Find the claim that doesn't overlap

for key in readable_patterns.keys():
    b = readable_patterns[key]
    area = (b[1] - b[0]) * (b[3] - b[2])
    fabric_sum_claims = fabric[b[0]:b[1], b[2]:b[3]].sum()
    if area == fabric_sum_claims:
        print "ID # {} is a good claim!".format(key)


