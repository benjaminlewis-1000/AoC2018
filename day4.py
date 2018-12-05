#! /usr/bin/env python

import re
import numpy as np

with open('day4_input.txt') as fh:
	guard_times = fh.read().split('\n')

guard_times.sort()

current_guard = -1
guard_compilation = {}
time_fell_asleep = 0
for log in guard_times:

    time_parse = re.search('\[\d+-\d+-\d+ \d+:(\d+)\].*', log)
    minute = int(time_parse.group(1))
    if 'begins shift' in log:
    	guard_num = re.search(".*Guard #(\d+).*", log)
    	# print guard_num.group(1)
        current_guard = int(guard_num.group(1))
        if current_guard not in guard_compilation.keys():
            guard_compilation[current_guard] = [np.zeros( 60 ), 1]
        else:
            guard_compilation[current_guard][1] += 1
    if 'falls asleep' in log:
        time_fell_asleep = minute
    if 'wakes up' in log:
        guard_compilation[current_guard][0][time_fell_asleep:minute] += 1

sleepiest_guard = -1
most_slept = 0
for guard in guard_compilation.keys():
    time_slept = guard_compilation[guard][0].sum()
    print guard_compilation[guard][1]
    if time_slept > most_slept:
        most_slept = time_slept
        sleepiest_guard = guard

print "Sleepiest guard is {}".format(sleepiest_guard)
best_min = guard_compilation[sleepiest_guard][0].argmax()
print "Best minute is " + str(best_min)
print "Answer is " + str(best_min * int(sleepiest_guard))

# Part 2
most_sleepy_times = 0
guard_num = -1
for guard in guard_compilation.keys():
    sleepiest_minute = guard_compilation[guard][0].argmax()
    num_times = guard_compilation[guard][0][sleepiest_minute]
    if num_times > most_sleepy_times:
        guard_num = guard
        most_sleepy_times = num_times

sleepy_minute = guard_compilation[guard_num][0].argmax()
print guard_compilation[guard_num][0]
print most_sleepy_times
print "Sleepy times times minute: " + str( sleepy_minute * guard_num )