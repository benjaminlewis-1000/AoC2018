#! /usr/bin/env python

import re

with open('day12_input.txt') as fh:
    plant_rules = fh.read().split('\n')

# plant_rules = '''initial state: #..#.#..##......###...###

# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #'''

# right_ans = '''....#..#.#..##......###...###............
# .....#...#....#.....#..#..#..#............
# .....##..##...##....#..#..#..##...........
# ....#.#...#..#.#....#..#..#...#...........
# .....#.#..#...#.#...#..#..##..##..........
# ......#...##...#.#..#..#...#...#..........
# ......##.#.#....#...#..##..##..##.........
# .....#..###.#...##..#...#...#...#.........
# .....#....##.#.#.#..##..##..##..##........
# .....##..#..#####....#...#...#...#........
# ....#.#..#...#.##....##..##..##..##.......
# .....#...##...#.#...#.#...#...#...#.......
# .....##.#.#....#.#...#.#..##..##..##......
# ....#..###.#....#.#...#....#...#...#......
# ....#....##.#....#.#..##...##..##..##.....
# ....##..#..#.#....#....#..#.#...#...#.....
# ...#.#..#...#.#...##...#...#.#..##..##....
# ....#...##...#.#.#.#...##...#....#...#....
# ....##.#.#....#####.#.#.#...##...##..##...
# ...#..###.#..#.#.#######.#.#.#..#.#...#...
# ...#....##....#####...#######....#.#..##..
# '''.split('\n')
# plant_rules = plant_rules.split('\n')

orig_state = plant_rules.pop(0)
blnk = plant_rules.pop(0)

for eachrule in range(len(plant_rules)):
    plant_rules[eachrule] = plant_rules[eachrule].split(' => ')
    # plant_rules[eachrule][0] = plant_rules[eachrule][0].replace('.', '\.')


orig_state = orig_state[15:]
orig_state = orig_state
print orig_state
# print plant_rules

import random

def findInString(pattern, inString):
    indices = []
    idx1 = 0
    while 1:
        try:
            idx = inString[idx1:].index(pattern)
            indices.append(idx + idx1 + 2)
            idx1 += idx + 1
        except ValueError as ve:
            return indices

start_idx = 0

def pad_state(orig_state, start_idx):
    if orig_state[0] != '.':
        orig_state = '.' + orig_state
        start_idx -= 1
    if orig_state[:2] != '..':
        orig_state = '.' + orig_state
        start_idx -= 1
    if orig_state[:3] != '...':
        orig_state = '.' + orig_state
        start_idx -= 1
    if orig_state[:4] != '....':
        orig_state = '.' + orig_state
        start_idx -= 1
    if orig_state[-1:] != '.':
        orig_state += '.'
    if orig_state[-2:] != '..':
        orig_state += '.'
    if orig_state[-3:] != '...':
        orig_state += '.'
    if orig_state[-4:] != '....':
        orig_state += '.'
    return orig_state, start_idx

orig_state, start_idx = pad_state(orig_state, start_idx)

def findAnswer(orig_state, start_idx, num_iters):
    for generation in range(num_iters):
        # next_state = '%s' % orig_state
        next_state = ['.'] * len(orig_state)
        # for j in range(len(next_state)):
        #     next_state[j] = '.'
        # print orig_state
        # print ('----')
        random.shuffle(plant_rules)
        for eachrule in plant_rules:
            pattern = eachrule[0]
            post_presence = eachrule[1]
            # print pattern, ' ', post_presence
            found_indices = findInString(pattern, orig_state)
            for j in found_indices:
                next_state[j] = post_presence
            # print ''.join(next_state)

        next_state = ''.join(next_state)
        # print next_state
        # print right_ans[generation + 1]
        # print generation
        # assert next_state == right_ans[generation + 1]
        # print '---'
        orig_state = next_state 
        orig_state, start_idx = pad_state(orig_state, start_idx)

    # Indices of the plants
    plant_idx = re.finditer('#', orig_state)
    idx = [m.start(0) + start_idx for m in plant_idx]
    # 985 too low
    return sum(idx)

print "The value after 20 iterations is: " + str(findAnswer(orig_state, start_idx, 20))

# Part 2 


last_answer = 0
answer_nums = []
test_num_iters = 130
for j in range(test_num_iters + 1):
    this_ans =  findAnswer(orig_state, start_idx, j)
    # print "---"
    # print this_ans - last_answer
    last_answer = this_ans
    answer_nums.append(this_ans)

# 50 billion is too many to compute, even with efficient algorithms.
# Found a pattern (steady-state): Adds 78 (for my input) to the sum
# for each iteration after ~110 or so. The above loop shows the pattern. 

# oneseventy = (170 - test_num_iters) * (answer_nums[-1] - answer_nums[-2]) + answer_nums[-1] 
# print findAnswer(orig_state, start_idx, 170)
# print oneseventy
fifty_bil = (50000000000 - test_num_iters) * (answer_nums[-1] - answer_nums[-2]) + answer_nums[-1] 
print "Value after 50 billion iterations is " + str(fifty_bil)