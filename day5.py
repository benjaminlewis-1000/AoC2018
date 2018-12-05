#! /usr/bin/env python

# Day 5 - polymer scanning

with open('day5_input.txt') as fh:
    data = fh.read()

def stringToMag(in_string):
    charlist = list(in_string)
    maglist = []
    for each in  charlist:
        if each.isupper():
            val = -1 * ord(each.lower())
        else:
            val = ord(each.lower())
        maglist.append(val)
    return maglist

def reactBases(maglist):

    didPop = True
    while didPop:
        didPop = False
        i = len(maglist) - 1
        while i > 0:
        # for i in xrange(len(maglist) - 1, 0, -1):
            # print i
            if maglist[i] + maglist[i-1] == 0:
                maglist.pop(i)
                maglist.pop(i-1)
                didPop = True
                i -= 1
            i -= 1 
        # print len(maglist)
    # print maglist
    return len(maglist)

testStr = "dabAcCaCBAcCcaDA"
maglist = (stringToMag(data))
# print maglist
print "The number of remaining base pairs is : " + str( reactBases(maglist) )

# Part 2

unique_bases = list(set(map(abs, maglist)))
print len(maglist)
# All base pairs would still react (or not exist), so we 
# can start with the altered maglist.  

bestLength = len(maglist)
best_base = 0
for eachBase in unique_bases:
    sublist = [x for x in maglist if abs(x) != eachBase]
    # print len(sublist)
    react_len = reactBases((sublist))
    if react_len < bestLength:
        bestLength = react_len
        best_base = eachBase

print "Best length is {} with the best base to remove being {}".format(bestLength, chr(best_base))
