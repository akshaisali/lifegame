# DEAD = * * *
# ALIVE = ###
import lifegame

def test_display_board_dead():
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0], [0,0,0,0,0]]
    expected_output = '*****\n*****\n*****\n*****\n*****'
    assert lifegame.display_board(board) == expected_output

def test_display_board_alive():
    board = [[1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    expected_output = '#####\n#####\n#####\n#####\n#####'
    assert lifegame.display_board(board) == expected_output


def test_display_board_alternative():
    board = [[1,1,1,1,1],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0],]

    expected_output = '#####\n*****\n#####\n*****\n*****'
    assert lifegame.display_board(board) == expected_output
  