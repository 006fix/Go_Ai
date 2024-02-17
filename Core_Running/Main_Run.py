
import pandas as pd

# base logic for the game:
# will be played on a N*N grid.
# location will be defined by a string, containing two numbers
# i.e, 5-15 = 5th column, 15th row. indexing will start at 1

# maximum row will be extracted and stored for future reference.
# training will by necessity take place on a specified value of N - in this case, 19*19

# empty slots on board shall contain value of 0. black = 0.5. white = 1
# each AI shall consider itself as playing white for the purposes of training (requires inversion of scoring)
# play order will be randomised.

# lets define our board.
board_space = {}
for i in range(1,20):
    for j in range(1, 20):
        ref_str = f'{i}-{j}'
        board_space[ref_str] = 0

#now lets do a test of converting our dictionary into a pandas dataframe for a neural network
#test_df = pd.DataFrame(board_space, index=[0])
# test complete, works as intended. i might need to modify this to pass in a index based on turn count.
# print(test_df.head(5))
