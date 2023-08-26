from typing import List
def padGrid(rows, cols):
    # pad the 1's with 0's
    # so that we can move right and down
    # without going out of bounds
    # 0's represent a path/edge
    # 1's represent a cell
    # no 1's can be adjacent to each other
    # all corners are 0's
    # all edges are 0's
    # all cells are 1's
    #rows = len(grid)
    #cols = len(grid[0])
    padded_grid = [[0 for _ in range(2*rows - 1)] for _ in range(2*cols - 1)]
    for i in range(2*rows - 1):
        for j in range(2*cols - 1):
            prev = padded_grid[i][j - 1]
            prev_up = padded_grid[i - 1][j]
            if prev == 1 or prev_up == 1 or i % 2 != 0:
                padded_grid[i][j] = 0
            else:
                padded_grid[i][j] = 1
    return padded_grid


def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))

padded_grid = padGrid(3, 3)
print_grid(padded_grid)