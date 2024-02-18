
from Rule_Functions.Adjacent_Cells import adjacent_cells

board_space = {}
for i in range(1,20):
    for j in range(1, 20):
        ref_str = f'{i}-{j}'
        board_space[ref_str] = 0

# test 1 : middle of the board
board_space['10-10'] = 1
adjacent = adjacent_cells(board_space, '10-10', 19)
print(adjacent)
# test 1 passed successfully

# test 2 - edge cell
board_space['1-1'] = 1
adjacent = adjacent_cells(board_space, '1-1', 19)
print(adjacent)
# test 2 passed successfully

# test 3 - alternate edge cell
board_space['19-19'] = 1
adjacent = adjacent_cells(board_space, '19-19', 19)
print(adjacent)
# test 3 passed successfully

# test 4-7 : middle edge cases
varsets = ['10-1','10-19','1-10','10-1']
for i in varsets:
    board_space[i] = 1
    adjacent = adjacent_cells(board_space, i, 19)
    print(f'for var {i}, values are {adjacent}')