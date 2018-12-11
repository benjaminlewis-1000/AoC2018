#! /usr/bin/env python

import numpy as np
import re
from time import sleep

with open('day10_input.txt') as fh:
	values = fh.read().split('\n')

positions = np.array([])
velocities = np.array([])

for i in values:
    found = re.search('position=\<(.?\d+), (.?\d+)\> velocity=\<(.?\d+), (.?\d+)\>', i)
    # print found.group(2)
    if len(positions) == 0:
        positions = np.array([[long(found.group(1))], [long(found.group(2))]])
        velocities = np.array([[long(found.group(3))], [long(found.group(4))]])
    else:
        positions = np.append(positions, [[long(found.group(1))], [long(found.group(2))]], 1)
        velocities = np.append(velocities, [[long(found.group(3))], [long(found.group(4))]], 1)

pos_max = np.max(positions, 1)
pos_min = np.min(positions, 1)
pos_max_x = pos_max[0]
pos_max_y = pos_max[1]
pos_min_x = pos_min[0]
pos_min_y = pos_min[1]

num_iters = 0

def get_second(start, end, stepsize, min_extent, min_sec):
    best_sec_this = 1e9
    global num_iters
    # num_iter = 0
    for sec in range(start, end, stepsize):
        sec_position = positions + sec * velocities
        # print sec_position
        pos_max = np.max(sec_position, 1)
        pos_min = np.min(sec_position, 1)
        pos_max_x = pos_max[0]
        pos_max_y = pos_max[1]
        pos_min_x = pos_min[0]
        pos_min_y = pos_min[1]

        extent = [pos_max_x - pos_min_x, pos_max_y - pos_min_y]
        extent_area =  extent[0] * extent[1]
        num_iters += 1
        if extent_area < min_extent:
            min_extent = extent_area
            min_sec = sec
            best_sec_this = sec
        elif sec > best_sec_this:
            return min_sec, min_extent
    return min_sec, min_extent

extent = [pos_max_x - pos_min_x, pos_max_y - pos_min_y]
min_extent = extent[0] * extent[1]
ms, min_extent = get_second(0, 100000, 10000, min_extent, 0)
ms, min_extent = get_second(ms - 5000, ms + 5000, 1000, min_extent, ms)
ms, min_extent = get_second(ms - 500, ms + 500, 100, min_extent, ms)
ms, min_extent = get_second(ms - 50, ms + 50, 10, min_extent, ms)
ms, min_extent = get_second(ms - 5, ms + 5, 1, min_extent, ms)

print "Algorithm took " + str(num_iters) + " steps"

print 'Seconds to wait is: ' + str(ms)

optimal_position = positions + ms * velocities
pos_max = np.max(optimal_position, 1)
pos_min = np.min(optimal_position, 1)
pos_max_x = pos_max[0]
pos_max_y = pos_max[1]
pos_min_x = pos_min[0]
pos_min_y = pos_min[1]

optimal_position = optimal_position - np.array([[pos_min_x], [pos_min_y]])

# print pos_max_x
# print pos_min_x

max_plt = np.max(optimal_position, 1)
max_plt_x = max_plt[0] + 1 
max_plt_y = max_plt[1] + 1

img = np.zeros([max_plt_y, max_plt_x])
for j in range(len(optimal_position[0])):
    img[optimal_position[1][j], optimal_position[0][j]] = 1

from matplotlib import pyplot as plt
aa = plt.imshow(img)
plt.show()


# print extent