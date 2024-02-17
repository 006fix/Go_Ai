
# this will serve as a function to take an inputted board state, and will calculate and remove pieces

def calculate_captures(new_board_state, piece_colour, place_location):

    # BASIC LOGIC : new board state is added, with piece moved, and location placed
    # this is then checked for all adjacent pieces
    # all adjacent non player pieces form a search start location
    # each of these pieces is checked for adjacent pieces. If any are null, no capture
    # if any are the same colour (enemy colour from this persepctive), that is added to the list to be checked
    # if all pieces within this adjacency search have no free liberties : all pieces are captured
    # reset value of all pieces to zero, return secondary board state