#! /usr/bin/env python
 
import numpy as np
 
powers = np.zeros([300, 300])
 
grid_serial = 7165
 
for xcoord in range(300):  
    for ycoord in range(300):
        x_1idx = xcoord + 1
        y_1idx = ycoord + 1
        rack_id = x_1idx + 10
        power_level = rack_id * y_1idx
        power_level = power_level + grid_serial
        power_level = power_level * rack_id
        keep_hundreds = int(power_level) % 1000 / 100
        power_level = keep_hundreds - 5
        powers[ycoord, xcoord] = power_level
        # print power_level
 
maxpow = -9 * 9
bestx = 0
besty = 0
for xcoord in range(1, 299):
    for ycoord in range(1, 299):
        xm1 = xcoord - 1
        xp1 = xcoord + 2
        ym1 = ycoord - 1
        yp1 = ycoord + 2
        val = powers[ym1:yp1, xm1:xp1].sum()
        if val > maxpow:
            bestx = xcoord 
            besty = ycoord 
            maxpow = val
 
print "Top left of 3x3 (answer 1): " + str(bestx) + ' ' + str(besty)

 
max_score = np.zeros([300, 300])
best_size = np.zeros([300, 300])

import time
start_time = time.time()

for xcoord in range(0, 300):
    if xcoord % 10 == 0:
        # print xcoord
        stop_time = time.time()
        print str(xcoord) + ", time for these ten: " + str(stop_time - start_time)
        start_time = stop_time
    # print val_cum   
    for ycoord in range(0, 300):
        val_cum = 0
        max_coord = max(xcoord, ycoord)
        max_size = 300 - max_coord + 1
        for i in range(1, max_size):
            # val = powers[ycoord:ycoord + i, xcoord:xcoord + i].sum()
            val_shell = powers[ycoord + i - 1, xcoord:xcoord + i].sum()
            val_shell += powers[ycoord:ycoord + i , xcoord + i - 1].sum()
            val_shell -= powers[ycoord + i - 1, xcoord + i - 1]
            # print val_cum   
            val_cum = val_shell + val_cum
            # print val
            # print val_cum
            # assert val == val_cum
            if val_cum > max_score[ycoord, xcoord]:
                max_score[ycoord,xcoord]=val_cum
                best_size[ycoord,xcoord]=i 

xy_val = np.unravel_index(np.argmax(max_score, axis=None), max_score.shape)
x = xy_val[1] + 1
y = xy_val[0] + 1
size = int(best_size[xy_val])

print "Part 2 answer: {},{},{}".format(x, y, size)