
# this will serve as a function to take an inputted board state, and will calculate and remove pieces

from Rule_Functions.Adjacent_Cells import adjacent_cells
def calculate_captures(new_board_state, piece_colour, place_location, max_size):

    # BASIC LOGIC : new board state is added, with piece moved, and location placed
    # this is then checked for all adjacent pieces
    # all adjacent non player pieces form a search start location
    # each of these pieces is checked for adjacent pieces. If any are null, no capture
    # if any are the same colour (enemy colour from this persepctive), that is added to the list to be checked
    # if all pieces within this adjacency search have no free liberties : all pieces are captured
    # several different pieces can be captured with a single move, each chain will have to be checked
    # reset value of all pieces to zero, return secondary board state
    valid_checks = adjacent_cells(new_board_state, place_location, max_size)
    # make a function to handle the capturing mechanics seperately
    cells_captured = []
    for i in valid_checks:
        # default to assuming they'll be captured, if anything resets you can break
        capture_for_chain = True
        # need a way to handle N length chaining - while loop?
        loop_continues = True
        tochecklist = [i]
        all_cells = [i]
        while loop_continues:
            # always take 0th index from tochecklist
            # once an item has been checked, it deletes (del.pop(0))
            # once only one item remains, FALSE loop_continues variable
            new_vals = adjacent_cells(new_board_state, tochecklist[0], max_size)
            for j in new_vals:
                checkingval = new_board_state[j]
                if checkingval == 0:
                    capture_for_chain = False
                elif checkingval == piece_colour:
                    tochecklist.append(j)
                    all_cells.append(j)
            if len(tochecklist) == 1:
                loop_continues = False
            else:
                del tochecklist[0]

        if capture_for_chain:
            for k in all_cells:
                cells_captured.append(k)

        return cells_captured










