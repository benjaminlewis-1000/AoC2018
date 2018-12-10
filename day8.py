#! /usr/bin/env python

from time import sleep

with open('day8_input.txt') as fh:
	data = fh.read().split()

# Part 1

# data = '2 3 0 3  10 11 12 1 1 0 1 99 2 1 1 2'.split()
# data = '2 3   0 3                      						   			   10 11 12   1 1   0 1 99   2   1 1 2'.split() # 135
# data = '2 3   1 3    2 3     0 2 2 2     1 2     0 1 7     5 5    1 2 3    10 11 12   1 1   0 1 99   2   1 1 2'.split() # + 27 = 162
# data = '2 3   1 3    0 3       1 2 3    10 11 12   1 1   0 1 99   2   1 1 2'.split() # + 27 = 162
data_ints = [int(x) for x in data]

def process_subtree(data, rd):

	meta_sum = 0
	num_children = data.pop(0)
	num_metadata = data.pop(0)

	for i in range(num_children):
		meta_sum += process_subtree(data, rd + 1)

	for j in range(num_metadata):
		meta_sum += data.pop(0)

	return meta_sum

ms = process_subtree(data_ints, 0)

print "Metadata sum is: " + str(ms)

# Part 2 

data_ints = [int(x) for x in data]

def val_of_node(data):
	num_children = data.pop(0)
	num_metadata = data.pop(0)

	children_values = []
	for i in range(num_children):
		children_values.append(val_of_node(data))

	metadata_vals = []
	for j in range(num_metadata):
		metadata_vals.append(data.pop(0))

	if num_children == 0:
		meta_val = sum(metadata_vals)
	else:
		meta_val = 0 
		for i in metadata_vals:
			if i > len(children_values):
				meta_val += 0
			else:
				meta_val += children_values[i - 1]

	return meta_val

print val_of_node(data_ints)