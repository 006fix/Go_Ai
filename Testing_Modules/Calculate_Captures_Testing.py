
from Rule_Functions.Calculate_Captures import calculate_captures

#test 1 - generic empty board, see valid captures
board_space = {}
for i in range(1,20):
    for j in range(1, 20):
        ref_str = f'{i}-{j}'
        board_space[ref_str] = 0