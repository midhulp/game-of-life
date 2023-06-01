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
    no_zero_set = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0] #excludes set (0,0)

    for i,j in no_zero_set:
        neighbor_i = row + i
        neighbor_j = col + j

        if 0 <= neighbor_i< len(grid) and 0 <= neighbor_j < len(grid[0]):
            if grid[neighbor_i][neighbor_j] == 1:
               live_neighbor_count += 1

    return live_neighbor_count

def new_gen_update(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_gen_grid = [[0] * cols for _ in range(rows)]
    # updated_board=[]
    for i in range(rows):
        for j in range(cols):
            live_neighbors = get_count_live_neighbors(grid, i, j)
            if grid[i][j] == 1 :
                if live_neighbors < 2 or live_neighbors > 3: #death condition
                    new_gen_grid[i][j] = 0
                else:
                    new_gen_grid[i][j] = 1
            else:
                if live_neighbors == 3:                      #new born condition
                    new_gen_grid[i][j] = 1

    return new_gen_grid    

def main():
    print(display(),'\n\n')

    print("The initial grid (3x3):")
    grid=[[0,1,0],[0,1,0],[0,1,0]]
    # User input 


    while True:
       
        print(show_newgrid(grid))
        # Update the grid to the next generation
        grid = new_gen_update(grid)
        

        #Asks user to continue or exit
        choice = input("Press Enter to see the next generation or 'E' to exit: ")
        if choice.lower() == 'e':
            break

if __name__ == '__main__':
    main()

