#! /usr/bin/env python
 
import numpy as np
 
with open('day13_input.txt') as fh:
    tracks = fh.read().split('\n')
# with open('day13_test.txt') as fh:
#     tracks = fh.read().split('\n')
 
 
# print tracks
 
track_array = np.zeros([len(tracks), len(tracks[0])])
 
carts = []
cart_directions = []

RIGHT_SLASH=2
LEFT_SLASH=3
 
for trackRow in range(len(tracks)):
    eachTrack = tracks[trackRow]
    pieces = list(eachTrack)
    for p in range(len(pieces)):
        if pieces[p] != ' ':
            track_array[trackRow, p] = 1
        if pieces[p] == '+':
            track_array[trackRow, p] = 4
        if pieces[p] == '/':
            track_array[trackRow, p] = RIGHT_SLASH
        if pieces[p] == '\\':
            track_array[trackRow, p] = LEFT_SLASH
        if pieces[p] == '>':
            carts.append([trackRow, p])
            cart_directions.append('right')
        if pieces[p] == '<':
            carts.append([trackRow, p])
            cart_directions.append('left')
        if pieces[p] == '^':
            carts.append([trackRow, p])
            cart_directions.append('up')
        if pieces[p] == 'v':
            carts.append([trackRow, p])
            cart_directions.append('down')
 
cart_next_tie = ['left'] * len(carts)

direction_adds = {'left': {'straight': [0, -1], 'left': [1, 0], 'right': [-1, 0]},
                  'right': {'straight': [0, 1], 'left': [-1, 0], 'right': [1, 0]},
                  'up': {'straight': [-1, 0], 'left': [0, -1], 'right': [0, 1]},
                  'down': {'straight': [1, 0], 'left': [0, 1], 'right': [0, -1]}  }

direction_dict = {'up': 0, 'right': 1, 'down': 2, 'left': 3}
direction_dict_back = {0: 'up', 1: 'right', 2: 'down', 3: 'left'}
 
import numpy as np

def move_carts(track_array, carts, cart_directions):
    # Sort of updates:
    # order_of_updates = range(len(carts))
    # for i in range(len(carts)):
    a = np.array([(c[0], c[1]) for c in carts], dtype=[('x', '<i4'), ('y', '<i4')])
    order_of_updates = np.argsort(a, order=('x', 'y'))
    # print order_of_updates
    # exit()
    iscrash = False
    to_pop = None

    for cartNum in order_of_updates:
        direction = cart_directions[cartNum]
        position = carts[cartNum]
        # print 'direction is ' + direction
        adds = direction_adds[direction]
        # print adds
        possible_positions = { 'straight': [position[0] + adds['straight'][0], position[1] + adds['straight'][1] ], 
                               'left': [position[0] + adds['left'][0], position[1] + adds['left'][1] ],
                               'right': [position[0] + adds['right'][0], position[1] + adds['right'][1] ]}
        for j in ['straight', 'right', 'left']:
            pp = possible_positions[j]
            # print pp
            if pp[0] < 0 or pp[1] < 0 or pp[0] > len(tracks) - 1 or pp[1] > len(tracks[0]) - 1:
                # print "Removing: {}".format(possible_positions[j])
                possible_positions.pop(j)
                continue
            if track_array[pp[0], pp[1]] == 0:
                possible_positions.pop(j)
                continue
 
        # print possible_positions

        if len(possible_positions) == 1:
            direction_taken = possible_positions.keys()[0]
        else:
            this_position_val = track_array[position[0], position[1]]
            if this_position_val == 1:
                direction_taken = 'straight'
            elif this_position_val == 4: 
                direction_taken = cart_next_tie[cartNum]
                # print direction_taken
                if direction_taken == 'left':
                    cart_next_tie[cartNum] = 'straight'
                elif direction_taken == 'straight':
                    cart_next_tie[cartNum] = 'right'
                elif direction_taken == 'right':
                    cart_next_tie[cartNum] = 'left'
            elif this_position_val == RIGHT_SLASH:
                if direction == 'right':
                    direction_taken = 'left'
                elif direction == 'left':
                    direction_taken = 'left'
                elif direction == 'up':
                    direction_taken = 'right'
                else:
                    direction_taken = 'right'
            elif this_position_val == LEFT_SLASH:
                if direction == 'right':
                    direction_taken = 'right'
                elif direction == 'left':
                    direction_taken = 'right'
                elif direction == 'up':
                    direction_taken = 'left'
                else:
                    direction_taken = 'left'

        carts[cartNum] = possible_positions[direction_taken]
        
        if direction_taken == 'straight':
            pass
        elif direction_taken == 'right':
            index = direction_dict[direction]
            index = (index + 1) % 4
            new_direction = direction_dict_back[index]
            cart_directions[cartNum] = new_direction
        elif direction_taken == 'left':
            index = direction_dict[direction]
            index = (index - 1) % 4
            new_direction = direction_dict_back[index]
            cart_directions[cartNum] = new_direction
 
 
        # Check for crashes after *every* move
        if not iscrash:
            for cartNum in range(len(carts)):
                thisOne = carts[cartNum]
                # iscrash = 0
                other_list = carts[:cartNum] + carts[(cartNum + 1):]
                if thisOne in other_list:
                    # print carts
                    other_index = other_list.index(thisOne)
                    if other_index >= cartNum:
                        other_index += 1
                    # print "crash! at positon " + str(carts[cartNum][1]) + "," + str(carts[cartNum][0]), ' Cart number: ' + str(cartNum), ' other cart number: ' + str(other_index)
                    iscrash = True
                    to_pop = (max(cartNum, other_index), min(cartNum, other_index))

            # print to_pop
            # print iscrash

    if iscrash:
        crash_position = carts[to_pop[0]]
        carts.pop(to_pop[0])
        cart_directions.pop(to_pop[0])
        cart_next_tie.pop(to_pop[0])
        carts.pop(to_pop[1])
        cart_directions.pop(to_pop[1])
        cart_next_tie.pop(to_pop[1])
        return crash_position
    else:
        return 0

    # Remove a cart
    # print len(carts)
    # print len(cart_directions)
    # print len(cart_next_tie)
    # carts.pop(0)
    # cart_directions.pop(0)
    # cart_next_tie.pop(0)


    if len(carts) == 0:
        return 1

    return 0
             
# print carts
# for i in range(200):
    # iscrashed = move_carts(track_array, carts, cart_directions)
    # print carts[2]

iscrashed = 0
while not iscrashed:
    iscrashed = move_carts(track_array, carts, cart_directions)
print "Location of first crash is: {}, {}".format(iscrashed[1], iscrashed[0])

# Part 2:
while len(carts) > 1:
    iscrashed = move_carts(track_array, carts, cart_directions)
print "Remaining cart: {}, {}".format(carts[0][1], carts[0][0])


# Right answer - 143, 43

# print carts
# move_carts(track_array, carts, cart_directions)
# print carts
# move_carts(track_array, carts, cart_directions)
# print carts