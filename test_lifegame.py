import lifegame

def test_show_display():
    assert lifegame.display()=="Welcome to game of life!"

def test_show_newgrid():
    grid=[[1, 1, 1], ['0', '0', '0'], [1, 1, 1]]
    assert lifegame.show_newgrid(grid) == "1 1 1 \n0 0 0 \n1 1 1 "

def test_count_live_neighbors():

    grid=[
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 1]
    ]
    assert lifegame.get_count_live_neighbors(grid, 1, 1) == 5
    assert lifegame.get_count_live_neighbors(grid, 1, 2) == 3



    
