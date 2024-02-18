
from Rule_Functions.Valid_Moves import calculate_valid_moves
import random

# test 1 - generic empty board, see moves
board_space = {}
for i in range(1,20):
    for j in range(1, 20):
        ref_str = f'{i}-{j}'
        board_space[ref_str] = 0

possible_moves = calculate_valid_moves(board_space, 19, 1)
print(len(possible_moves))
# 361 - test one complete

# test two - single piece placed (same colour as mover)
board_space['1-1'] = 1
possible_moves = calculate_valid_moves(board_space, 19, 1)
print(len(possible_moves))
# test two complete

# lets create a situation in which one additional move is invalid

board_space = {}
for i in range(1,20):
    for j in range(1, 20):
        ref_str = f'{i}-{j}'
        board_space[ref_str] = 0

board_space['1-2'] = 1
board_space['2-1'] = 1
# this removes two potential options.
# if moving as white, you should have 359 possible moves
# if moving as black, you should have 358 possible moves
possible_moves = calculate_valid_moves(board_space, 19, 1)
print(f'for white, n valid moves = {len(possible_moves)}')
possible_moves = calculate_valid_moves(board_space, 19, 0.5)
print(f'for black, n valid moves = {len(possible_moves)}')

# test passed successfully

# final test for now : what if we have a piece fully and partially surrounded in the board centre?

board_space = {}
for i in range(1,20):
    for j in range(1, 20):
        ref_str = f'{i}-{j}'
        board_space[ref_str] = 0

# we'll use 10-10 as our reference point
board_space['10-11'] = 1
board_space['10-9'] = 1
board_space['9-10'] = 1
# with this setup, it has a free space
# 3 cells occupied, so expecting 358 for both white and black
possible_moves = calculate_valid_moves(board_space, 19, 1)
print(f'for white, n valid moves = {len(possible_moves)}')
possible_moves = calculate_valid_moves(board_space, 19, 0.5)
print(f'for black, n valid moves = {len(possible_moves)}')
# test successful
# now lets try adding the final extra square
# excepting 357 for white, 356 for black
board_space['11-10'] = 1
possible_moves = calculate_valid_moves(board_space, 19, 1)
print(f'for white, n valid moves = {len(possible_moves)}')
possible_moves = calculate_valid_moves(board_space, 19, 0.5)
print(f'for black, n valid moves = {len(possible_moves)}')
# test passed successfully
# what if we change 11-10 to black? should then be identical for both at 357
board_space['11-10'] = 0.5
possible_moves = calculate_valid_moves(board_space, 19, 1)
print(f'for white, n valid moves = {len(possible_moves)}')
possible_moves = calculate_valid_moves(board_space, 19, 0.5)
print(f'for black, n valid moves = {len(possible_moves)}')
# testing SUCCESS!

# TWO FINAL TESTING STAGES REMAINING
# test 1 : if piece could be placed because it would free up its own liberty via capture
# test 2 : if piece could not be placed because it would cause direct replication of prior board state (needs own testing module)
