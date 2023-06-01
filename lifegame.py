def display():
    a=("Welcome to game of life!")
    return a


# def collect_grid():
#     grid = []
#     for _ in range(3):
#         row = input("Enter a row (('1' or '0') -separated by comma): ")
#         grid.append(row.split(","))
#     return grid


def show_newgrid(grid):
    newgrid = []
    for row in grid:
        val = ''
        for item in row:
            if item == 1:
                val += '1 '
            else:
                val += '0 '
        newgrid.append(val)
    return '\n'.join(newgrid)





