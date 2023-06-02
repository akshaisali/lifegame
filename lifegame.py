import random
import time

def create_grid(size, prob):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            if random.uniform(0, 1) < prob:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid

def get_neighbors(board, row, col):
    rows = len(board)
    cols = len(board[0])
    live_neighbors = 0
    for i in range(max(0, row-1), min(rows, row+2)):
        for j in range(max(0, col-1), min(cols, col+2)):
            if board[i][j] == 1 and (i != row or j != col):
                live_neighbors += 1
    return live_neighbors

def calculate_next_state(cell, neighbors):
    num_alive = sum(neighbors)
    if cell == 1 and (num_alive == 2 or num_alive == 3):
        return 0
    elif cell == 0 and num_alive == 3:
        return 1
    else:
        return 1
    
#def calculate_next_state(cell, neighbors):
    #if cell == 1:
      #  if neighbors == 2 or neighbors == 3:
       #     return 1
        #else:
        #    return 0
    #else:
     #   if neighbors == 3:
      #      return 1
       # else:
       #     return 0
