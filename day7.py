#! /usr/bin/env python

import re

def moveLeft(idx):
    if len(instructionList) > 1:
        while idx > 0 and instructionList[idx] < instructionList[idx - 1]:
            popval = instructionList.pop(idx)
            instructionList.insert(idx-1, popval)
            idx -= 1

instructionList = []
def putLeftOf(instruction):
    order = re.search('Step ([A-Z]) .* before step ([A-Z]).*', instruction)
    first = order.group(1)
    second = order.group(2)
    # print first, second



    if second in instructionList:
        idx2 = instructionList.index(second)
    else:
        instructionList.append(second)
        moveLeft(len(instructionList) - 1)

    # print instructionList

    idx2 = instructionList.index(second)
    if first in instructionList:
        idx1 = instructionList.index(first)
        if idx1 < idx2:
            pass
        else:
            valpop = instructionList.pop(idx1)
            instructionList.insert(max(idx2, 0), valpop)
            moveLeft(instructionList.index(valpop))
    else:
        if idx2 == 0:
            instructionList.insert(0, first)
        else:
            instructionList.insert(idx2, first)
            moveLeft(idx2)



instructions = '''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''

with open('day7_input.txt') as fh:
    instructions = fh.read()
# import random
# random.seed(1)

steps = instructions.split('\n')
# random.shuffle(steps)
# print '\n'.join(steps)

for eachStep in steps:
    print eachStep
    putLeftOf(eachStep)
    print instructionList

print steps[0]
print instructionList

print ''.join(instructionList)