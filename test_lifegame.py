import lifegame


def test_show_display():
    assert lifegame.display()=="Welcome to game of life"

          
def test_collect_grid(monkeypatch):
    input = ["x,x,x", "0,0,0", "x,x,x"] 
    monkeypatch.setattr('builtins.input', lambda _: input.pop(0))
    new_grid = [['x', 'x', 'x'], ['0', '0', '0'], ['x', 'x', 'x']]
    assert lifegame.collect_grid() == new_grid
