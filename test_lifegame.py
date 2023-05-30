import lifegame


def test_show_display():
    assert lifegame.display()=="Welcome to game of life"

def test_store_grid():
    assert lifegame.store_grid([["x","x","x"],["0","0","0"],["x","x","x"]])=="""xxx
000
xxx"""
                                                                    



