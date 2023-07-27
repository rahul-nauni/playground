from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        open = close = 0
        res = []
        def backtrack(s, open, close):
            if len(s) == 2*n:
                res.append(s)
                return
            # we can always add an opening parenthesis if we haven't reached the limit
            if open < n:
                backtrack(s+'(', open+1, close)
            # we can only add a closing parenthesis if we have more open than close
            if close < open:
                backtrack(s+')', open, close+1)
        backtrack('', open, close)
        return res
    
    
s = Solution()
print(s.generateParenthesis(3))