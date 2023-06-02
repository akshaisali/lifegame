import pytest
import lifegame


def test_create_grid():
    size = 5
    prob = 0.5
    grid = lifegame.create_grid(size, prob)
    assert len(grid) == size
    for row in grid:
        assert len(row) == size

def test_get_neighbor():
    board=[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    assert lifegame.get_neighbors(board,1,1)==2