# using np for printing out the grid in a better format
import numpy as np

# recall: grid in python is grid[col][row] for whatever reasons: not row,col.

def main():
    grid = [[5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]]
    print("Sudoku:")
    print(np.matrix(grid))
    print("Would you like to solve? (y/n)")
    if input() == "y":
        if solve(grid):
            print("Ploof gersploosh! Behold:") 
            print(np.matrix(grid))
        else:
            print("Solution does not exist.\nWhat a waste of precious computation.\nToodles.")
    else: 
        print("You have denied my help, though you needn't worry - I've already moved on to better things.")

# determines if n is a valid solution to cell (y,x)
def is_valid(y,x,n,grid):
    # check if any value in this col = n
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    # check if any value in this row = n
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    # (x0,y0) is the top left value in the 3x3 box
    x0 = (x//3)*3
    y0 = (y//3)*3
    # check if any value in (x,y)'s 3x3 box = n
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True
            
def solve(grid):
    for y in range(0,9):
        for x in range(0,9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if is_valid(y,x,n,grid):
                        # assign new valid value to y,x
                        grid[y][x] = n
                        # recursively call solve() on changed grid
                        if not solve(grid):
                            # if this point is reached, it means n in (y,x)
                            # doesn't allow for a full solution, so reset to 0
                            # and pick the next valid number
                            grid[y][x] = 0
                # if we go through all numbers and none work, a soln DNE
                if grid[y][x] == 0:
                    return False
    return True
    
if __name__ == "__main__":
    main()
