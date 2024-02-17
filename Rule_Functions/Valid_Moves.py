
# this will serve as a method of evaluating the game space for all valid moves
# returned item will be a list of valid moves

# WARNING - THIS DOES NOT CONTAIN THE ABILITY TO RESTRICT MOVES WHICH MIMIC THE PRIOR MOVE STATE
# ADD THAT AS A SEPERATE CONTROL LATER ON.

def calculate_valid_moves(board_state, max_size, piece_colour):
    # base input is the dictionary board_state.
    # max size added to search for invalid positions
    # piece colour = 0.5 or 1, for black and white respectively
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
        # we've removed all occupied squares
        # now the only rule that remains, is if the square has liberties
        # ADDENDUM : this *technically* only applies if it would have no liberties after the move
        # for now, add the liberties logic. Then, add a function for capturing
        # then, for each move, add a check for capture logic, and apply this here
        #liberties would be defined as having all *valid* adjacent points occupied by an enemy
        true_valid_moves = []
        for checkval in prelim_valid_moves:
            var1, var2 = checkval.split('-')
            m1 = var1 + 1
            m2 = var1 - 1
            m3 = var2 + 1
            m4 = var2 - 1
            valid_checks = []
            if m1 > 0 & m1 <= max_size:
                checkvar = str(m1) + '-' + str(var2)
                valid_checks.append(checkvar)
            if m2 > 0 & m2 <= max_size:
                checkvar = str(m2) + '-' + str(var2)
                valid_checks.append(checkvar)
            if m3 > 0 & m3 <= max_size:
                checkvar = str(var1) + '-' + str(m3)
                valid_checks.append(checkvar)
            if m4 > 0 & m4 <= max_size:
                checkvar = str(var1) + '-' + str(m4)
                valid_checks.append(checkvar)
            # default to assuming its a valid move
            valid_move = True
            # if any of the pieces are either empty (0) or the same piece, the move is valid
            # if all of them are not one of these options, it is not
            valid_options = [0, piece_colour]
            num_fails = 0
            num_options = len(valid_checks)
            for ii in valid_checks:
                holdval = board_state[ii]
                if holdval not in valid_options:
                    num_fails += 1
            if num_fails == num_options:
                valid_move = False
            if valid_move:
                true_valid_moves.append(checkval)

        return true_valid_moves




