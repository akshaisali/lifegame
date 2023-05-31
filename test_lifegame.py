# DEAD = * * *
# ALIVE = ###
import lifegame

def test_display_board_dead():
    board = [[0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]]
    expected_output = '***\n***\n***'

    assert lifegame.display_board(board) == expected_output

