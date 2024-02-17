
# this will serve as a method of evaluating the game space for all valid moves
# returned item will be a list of valid moves

def calculate_valid_moves(board_state):
    # base input is the dictionary board_state.
    # obviously - any square currently populated is invalid. so lets reduce the search space
    prelim_valid_moves = []
    # control for if all are valid - in that case we can skip everything else and return the list
    any_invalid = False
    for key in board_state:
        holdval = board_state[key]
        if holdval == 0:
            prelim_valid_moves.append(key)
        else:
            any_invalid = True

    if any_invalid == False:
        return prelim_valid_moves

    # main body of the function goes here now.
    else:
