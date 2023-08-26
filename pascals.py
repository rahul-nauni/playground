from typing import List

class Solution:
    def generate(self, numRows: int):
        pascal = []
        for row in range(numRows):
            pascal.append([])
            for col in range(row+1):
                if col == 0 or col == row:
                    pascal[row].append(1)
                else:
                    pascal[row].append(pascal[row-1][col-1] + pascal[row-1][col])
        return pascal

    def print(self, pascal: List[List[int]]):
        for row in pascal:
            print(row)

s = Solution()
pascal = s.generate(5)
s.print(pascal)