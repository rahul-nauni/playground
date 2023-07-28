# Problem: Game of Life
# Problem Statement: https://leetcode.com/problems/game-of-life/
class Solution(object):
    def checkNeighbors(self, board, i, j):
        
        self.liveNeighbors = 0

        for direction in self.directions:
            row = i + direction[0]
            col = j + direction[1]
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                continue
            if row == i and col == j:
                continue
            if self.stateMap[(row, col)] == 1:
                self.liveNeighbors += 1
        
        return self.liveNeighbors

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Find neighbors of each cell using directions
        self.directions = [
            (-1, -1), # Top left
            (-1, 0), # Top
            (-1, 1), # Top right
            (0, -1), # Left
            (0, 1), # Right
            (1, -1), # Bottom left
            (1, 0), # Bottom
            (1, 1) # Bottom right
        ]
        
        self.stateMap = {}

        # Create a state map of the board
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                self.stateMap[(i,j)] = board[i][j]
        
        # Iterate through the board and update the state of each cell based on rules
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                self.liveNeighbors = self.checkNeighbors(board, i, j)
                if self.stateMap[(i, j)] == 1: # Alive cell
                    if self.liveNeighbors < 2 or self.liveNeighbors > 3:
                        board[i][j] = 0
                    elif self.liveNeighbors == 2 or self.liveNeighbors == 3:
                        board[i][j] = 1
                elif self.stateMap[(i, j)] == 0: # Dead cell
                    if self.liveNeighbors == 3:
                        board[i][j] = 1
                #else:
                #    board[i][j] = 0

        return board

board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]


s = Solution()
new_board = s.gameOfLife(board)

print(f"\nOriginal state of board:")
for row in range(len(board)):
    for col in range(len(board[0])):
        print(board[row][col], end="  ")
    print()
    
print(f"\nNext state of board:")
for row in range(len(new_board)):
    for col in range(len(new_board[0])):
        print(new_board[row][col], end="  ")
    print()


