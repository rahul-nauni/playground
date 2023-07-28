class Solution():
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.directions = {
        (-1, 0), # up
        (1, 0), # down
        (0, 1), # right
        (0, -1), # left
        }

        self.visited = set()
        self.islands = 0
        
        def dfs(grid, i, j):
            # OOB
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return 0
            
            if (i, j) in self.visited:
                return 0
            
            self.visited.add((i, j)) # add current cell to visited
            for direction in self.directions:
                row = i + direction[0] # change row index
                col = j + direction[1] # change col index

                # call recursively
                dfs(grid, row, col)


        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in self.visited: # only check for lands and previously not visited
                    dfs(grid, i, j)
                    self.islands += 1
        # return num of islands
        return self.islands

grid =[  
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
s = Solution()
print(s.numIslands(grid))