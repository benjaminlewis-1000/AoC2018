#! /usr/bin/env python

last_marble = 71588 
num_elves = 430

def construct_game(num_marbles):
    scores = []
    board = []
    board = [0, 1]
    cur_idx = 1
    next_idx = 1
    for i in range(2, num_marbles + 1):
        if i % 23 != 0 or i == 0:
            cur_idx = next_idx
            board.insert(cur_idx, i)
            next_idx = (cur_idx + 2) % len(board)
            if next_idx == 0:
                next_idx = len(board)
        else:
            cur_score = i
            remove_idx = (cur_idx - 7) % len(board)
            # a b c d e f (g) -- 6 - 7 % 7
            # a b c d e f (g) h -- 6 - 7 % 8
            # a b c d e f g (h) -- 7 - 7 % 8
            cur_score += board.pop(remove_idx)
            cur_idx = remove_idx
            next_idx = (cur_idx + 2) % len(board)
            if next_idx == 0:
                next_idx = len(board)
            scores.append(cur_score)
        if i % 1000 == 0:
            print "Iteration {} / {}".format(i, num_marbles + 1)
    print cur_idx
    print board[cur_idx]
    return board, scores

board, scores = construct_game(last_marble)
print board
# print scores

def compute_scores(scores, num_players):
    player_scores = [0] * num_players
    for i in range(len(scores)):
        turn_num = (i + 1) * 23
        player_num = turn_num % num_players
        score_val = scores[i]
        player_scores[player_num] += score_val
    return player_scores

player_scores = compute_scores(scores, num_elves)
winning_score = max(player_scores)
print "The winning score is " + str(winning_score)

# Part 2
board, scores = construct_game(last_marble * 100)
player_scores = compute_scores(scores, num_elves)
winning_score = max(player_scores)
# While this eventually gets the right answer, I looked up
# a faster implementation on reddit after getting the answer. 
# See day9_2.py
print "The winning score is " + str(winning_score)