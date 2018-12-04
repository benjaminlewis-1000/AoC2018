#! /usr/bin/env python

# Part 1
with open('input2.txt') as fh:
    puzzle_input = fh.read()
puzzle_input = puzzle_input.split()

list_exactly_2 = []
list_exactly_3 = []

def has_n_of(string, n):
    unq_letters = list( set( sorted( string) ) );
    for unq in unq_letters:
        if string.count(unq) == n:
            return True

    return False

for eachID in puzzle_input:
    if has_n_of(eachID, 2):
        list_exactly_2.append(eachID)
    if has_n_of(eachID, 3):
        list_exactly_3.append(eachID)

checksum = len(list_exactly_2) * len(list_exactly_3)
print "Answer to part 1 checksum is " + str(checksum)

# Part 2
def edit_dist(string1, string2):
    str1_array = list(string1)
    str1_nums = [ord(x) for x in str1_array]
    str2_array = list(string2)
    str2_nums = [ord(x) for x in str2_array]
#
    diff = 0
    for i in range(len(str1_nums)):
        if str1_nums[i] != str2_nums[i]:
            diff += 1
    return diff

test_in = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']

import itertools
correctPair = ''
for pair in itertools.product(puzzle_input, puzzle_input):
    # print pair
    if edit_dist(pair[0], pair[1]) == 1:
        correctPair = pair

outStr = ''
for i in range(len(correctPair[0])):
    if correctPair[0][i] == correctPair[1][i]:
        outStr += correctPair[0][i]

print "The letters in common between the two similar IDs, in order, are: " + outStr

# common_letters = set(correctPair[0]).intersection(set(correctPair[1]))
# print ''.join(sorted(list(common_letters)))