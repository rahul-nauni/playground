# Reverse words in a string
# https://leetcode.com/problems/reverse-words-in-a-string/
import re
class Solution:
    def preprocess(self, s:str):
        s = re.sub("\s+", ' ', s)
        return s
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s.reverse()
        return " ".join(s) 
    
s = "the sky is blue"
print(Solution().reverseWords(s))