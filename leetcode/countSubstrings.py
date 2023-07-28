# Count palindromic substrings

class Solution:
    def _reverse(self, s):
        start = len(s) - 1
        end = 0
        while start > end:
            s[start], s[end] = s[end], s[start]
            start -= 1
            end += 1
        return s
    
    def expand(self, s, left, right):
        count = 0
        while right < len(s) and left >= 0:
            if s[right] == s[left]:
                count += 1
                left -= 1
                right += 1
            else:
                break
        return count
    
    
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        count = 0
        for i in range(len(s)):
            left = i
            right = i
            count += self.expand(s, left, right) # odd length palindromes
            count += self.expand(s, left, right+1) # even length palindromes
        return count
    
s = "aaa"
print(Solution().countSubstrings(s))