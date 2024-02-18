
from Rule_Functions.Valid_Moves import calculate_valid_moves

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
