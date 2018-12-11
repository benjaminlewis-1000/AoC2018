#! /usr/bin/env python

import numpy as np

with open('day6_input.txt') as fh:
	coord_list = fh.read().split('\n')


# Convert to numpy
# coord_list = ['1, 1', '1,6','8,3','3,4','5, 5', '8,9']
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
    clist2[coord + 1] = [x,y]

# print clist2

gridsize = max(maxx, maxy) + 1
grid = np.zeros([gridsize, gridsize])
# print grid.shape

keylist = clist2.keys()
for each in range(len(keylist)):
    key = keylist[each]
    x, y = clist2[key]
    
def mark_closest(manhat_dist, coord_num):

    # Propose pairs
    count_up = range(manhat_dist + 1)
    count_down = range(manhat_dist, -1, -1)
    x_c, y_c = clist2[coord_num]
    # print x_c, y_c
    grid[y_c, x_c] = -1

    possible_coords = []
    # print "MD: " + str(manhat_dist)
    # print "Center: " + str(clist2[coord_num])
    for i in range(len(count_up)):
        x_off = count_up[i]
        y_off = count_down[i]
        p1 = [x_c + x_off, y_c + y_off]
        p2 = [x_c - x_off, y_c + y_off]
        p3 = [x_c + x_off, y_c - y_off]
        p4 = [x_c - x_off, y_c - y_off]
        if p1 not in possible_coords:
            possible_coords.append(p1)
        if p2 not in possible_coords:
            possible_coords.append(p2)
        if p3 not in possible_coords:
            possible_coords.append(p3)
        if p4 not in possible_coords:
            possible_coords.append(p4)

    # Evaluate the possible coordinates
    changed_any = False
    for x_poss, y_poss in possible_coords:
        if x_poss < 0 or y_poss < 0:
            pass # Reject - out of grid
        elif x_poss >= gridsize or y_poss >= gridsize:
            pass # Reject - out of grid
        else: # Valid coordinate
            # print x_poss, ' ', y_poss
            grid_val = grid[y_poss, x_poss]
            if grid_val < 0:
                if manhat_dist < abs(grid_val):
                    grid[y_poss, x_poss] = coord_num
                else:
                    continue # Already equidistant from at least two 
            elif grid_val == 0:
                grid[y_poss, x_poss] = coord_num
                changed_any = True
            else:
                dist_to_gridval = abs(x_poss - clist2[grid_val][0]) + abs(y_poss - clist2[grid_val][1])
                if grid_val == coord_num:
                    pass # Already marked for this coordinate
                elif manhat_dist < dist_to_gridval:
                    grid[y_poss, x_poss] = coord_num
                    changed_any = True
                elif manhat_dist  == dist_to_gridval:
                    grid[y_poss, x_poss] = -manhat_dist
                else:
                    pass # Do nothing

    if changed_any:
        mark_closest(manhat_dist + 1, coord_num)

grid[:, :] = 1
grid[clist2[1][0], clist2[1][1]] = -1

for i in range(1, len(coord_list)):
    print "Calculating for coordinate {}/{}...".format(i + 1, len(coord_list) )
    mark_closest(1, i + 1)

unique, counts = np.unique(grid, return_counts=True)
# print grid
areas_dict = dict(zip(unique, counts))
# print areas_dict

infinite_areas = set( grid[0, : -1] ).union( set( grid[:-1,0] ) ).union( set( grid[-1, :-1] ).union( set( grid[:-1, -1] ) ) ) 

all_points = range(len(coord_list))
all_points = [x + 1 for x in all_points]
valid_areas = list( set( all_points ) - infinite_areas)
non_infinite_extent = 0
check_val = 0
for check in valid_areas:
    if areas_dict[check] > non_infinite_extent:
        non_infinite_extent = areas_dict[check]
        check_val = check

print "Biggest non-infinite extent is : " + str(non_infinite_extent + 1)

from matplotlib import pyplot as plt
img = plt.imshow(grid)
plt.draw()
plt.pause(0.001)

# Part 2
grid_safe = np.zeros([gridsize, gridsize])
for xval in range(gridsize):
    # print xval
    for yval in range(gridsize):
        for val in clist2.keys():
            x_coord, y_coord = clist2[val]
            manhat_dist = abs(x_coord - xval) + abs(y_coord - yval)
            grid_safe[yval, xval] += manhat_dist

safe_region_size = len(np.where(grid_safe < 10000)[0])
print "Safe region size is " + str(safe_region_size)
