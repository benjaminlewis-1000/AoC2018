#! /usr/bin/env python

curSum = '0'

with open('day1_input.txt') as fh:
    data = fh.read()

data_list = data.split()

# Part 1
resulting_freq = eval(' '.join(data_list))
print resulting_freq

# Part 2 
sums_iter1 = [0]
first_sum = 0
cur_sum = 0

# Intuition: The first repeated frequency will be within the first iteration of the list, since we're justt offsetting by 
# the resulting_freq (after one iteration) every time. This is positive, but we have a super-negative number,
# so it requires that we iterate several times.
# Since any number we iterate to after this first time will come after that first step, we don't have to worry
# about hitting those later numbers until we hit the first set of numbers. I think. Got the right answer, anyway. 
for i in range(len(data_list)):
    nextSum = eval( str(cur_sum) + data_list[i])
    sums_iter1.append((nextSum))
    cur_sum = nextSum

def doit(cur_sum):
    for k in range(1000):
        for i in range(len(data_list)):
            nextSum = eval( str(cur_sum) + data_list[i])
            if nextSum in sums_iter1:
                print "The answer for part 2 is: " + str(nextSum) + " after {} iterations.".format(k)
                return
            # sums_iter1.append((nextSum))
            cur_sum = nextSum

doit(cur_sum)



# print sums_iter1[len(sums_iter1)/2: -1]
# print min(sums_iter1[len(sums_iter1)/2: -1])
# print max(sums_iter1[len(sums_iter1)/2: -1])
# print min(sums_iter1[1:len(sums_iter1)/2])
# print max(sums_iter1[1:len(sums_iter1)/2])