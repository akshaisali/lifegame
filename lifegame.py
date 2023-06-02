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