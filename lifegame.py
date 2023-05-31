def display_board(board):
    grid = []
    for row in board:
        row_str = ''
        for cell in row:
            if cell == 1:
                row_str += '#'
            else:
                row_str += '*'
        grid.append(row_str)
    return '\n'.join(grid)