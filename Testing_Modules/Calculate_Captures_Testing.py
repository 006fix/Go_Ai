
from Rule_Functions.Calculate_Captures import calculate_captures

#test 1 - generic empty board, see valid captures
board_space = {}
for i in range(1,20):
    for j in range(1, 20):
        ref_str = f'{i}-{j}'
        board_space[ref_str] = 0

# single piece placed
board_space['2-1'] = 1
captures = calculate_captures(board_space, 1, '2-1', 19)
print(captures)
# test complete

# test two : add in a black piece in 1-1
board_space['1-1'] = 0.5
captures = calculate_captures(board_space, 1, '2-1', 19)
print(captures)
# test complete

#now we add in a third piece in 1-2, which captures the black piece in 1-1
board_space['1-2'] = 1
captures = calculate_captures(board_space, 1, '2-1', 19)
print(captures)
checkvals = ['1-1','1-2','2-1']
for i in checkvals:
    holdval = board_space[i]
    print(holdval)
# all pieces working, but capture logic is NOT. why?