import lifegame


def test_gmeoflfe_display_dead():
    assert lifegame.display_grid([[1,1,1],[1,1,1],[1,1,1,]]) == '111\n111\n111'

def test_gmeoflfe_display_dead_live():
    assert lifegame.display_grid([[1,1,1],[1,1,0],[1,1,0]]) == '111\n110\n110'



# def test_gmeoflfe_play():
#       assert lifegame.ply_game([[1,1,1,1,1],[1,1,1,0,1],[1,1,1,0,1],[1,1,1,1,1],[1,1,1,1,1]]) == '#####\n#####\n#####\n#####\n#####\n'

def sample_board():
    return [[0,1,0],[0,0,1],[1,1,1]]

def test_next_live_or_dead():
    expected_board = [[0,0,0],[1,0,1],[0,1,1]]
    board = sample_board()
    assert lifegame.next_generation(board) == expected_board

def test_nieghbours_live_dead():
    board = [[0,1,0],[0,1,0],[0,1,0]]
    assert lifegame.count_live_dead_neighbors(board,1,1) == 2