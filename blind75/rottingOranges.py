# Problem: Rotting Oranges
"""You are given an m x n grid where each cell can have one of three values:

    - 0 representing an empty cell,
    - 1 representing a fresh orange, or
    - 2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1."""

from typing import List
from collections import deque
class Solution:
    def __init__(self):
        self.fresh = 0
        self.rotten = deque()
        self.ticks = 0
        self.directions = [
                (0, 1), # right
                (0, -1), # left
                (-1, 0), # up
                (1, 0), # down
            ]

    def view_grid(self, grid):
        for row in grid:
            print(row)
        print()

    def spoil_oranges(self, grid, row, col) -> bool:
        for direction in self.directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                grid[new_row][new_col] = 2 # spoil orange
                self.fresh -= 1
                self.rotten.append((new_row, new_col, self.ticks + 1))


    def rottingOranges(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self.fresh += 1
                elif grid[row][col] == 2:
                    self.rotten.append((row, col, 0)) # (row, col, ticks)
        
        while self.rotten:
            row, col, t = self.rotten.popleft()
            self.ticks = max(t, self.ticks)
            self.spoil_oranges(grid, row, col)
        return self.ticks if self.fresh == 0 else -1

grid = [
        [2, 1, 1],
        [1, 1, 1],
        [0, 1, 2]
    ]
s = Solution()
print(s.rottingOranges(grid))