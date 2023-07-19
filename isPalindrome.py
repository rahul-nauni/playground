import re
class Solution:
    def preprocess(self, s: str) -> str:
        s = s.lower()
        s = re.sub('[\W_]+', '', s)
        return s
    
    def isPalindrome(self, s: str) -> bool:
        s = self.preprocess(s)
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))