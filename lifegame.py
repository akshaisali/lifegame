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