def display():
    a=("Welcome to game of life")
    return a


def collect_grid():
    grid = []
    for _ in range(3):
        row = input("Enter a row (('x' or '0') -separated by comma): ")
        grid.append(row.split(","))
    return grid


    
       





