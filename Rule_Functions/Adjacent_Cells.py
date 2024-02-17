
# this is designed to take a board state, and a cell location, and return adjacent cells
# also takes max size for variable board size games

def adjacent_cells(board_state, cell_location, max_size):
    valid_checks = []
    var1, var2 = cell_location.split('-')
    m1 = var1 + 1
    m2 = var1 - 1
    m3 = var2 + 1
    m4 = var2 - 1
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

    return valid_checks