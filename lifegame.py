def display():
    a=("Welcome to game of life!")
    return a

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

def get_count_live_neighbors(grid, row, col):
    live_neighbor_count = 0
    no_zero_set = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

    for i,j in no_zero_set:
        neighbor_i = row + i
        neighbor_j = col + j

        if 0 <= neighbor_i< len(grid) and 0 <= neighbor_j < len(grid[0]):
            if grid[neighbor_i][neighbor_j] == 1:
               live_neighbor_count += 1

    return live_neighbor_count

