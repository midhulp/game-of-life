import lifegame

def test_show_display():
    assert lifegame.display()=="Welcome to game of life!"

# def test_collect_grid(monkeypatch):
#     input = ["1,1,1", "0,0,0", "1,1,1"] 
#     monkeypatch.setattr('builtins.input', lambda _: input.pop(0))
#     new_grid = [['1', '1', '1'], ['0', '0', '0'], ['1', '1', '1']]
#     assert lifegame.collect_grid() == new_grid

def test_show_newgrid():
    grid=[[1, 1, 1], ['0', '0', '0'], [1, 1, 1]]
    assert lifegame.show_newgrid(grid) == "1 1 1 \n0 0 0 \n1 1 1 "
    
