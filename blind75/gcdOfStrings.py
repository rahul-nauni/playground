class Solution:
    def is_valid(self, base: str, str1: str, str2: str) -> bool:
        # check if str1 is a multiple of str2
        # if str1 is a multiple of str2, then str1 must be a substring of str2 + str2 ...
        # e.g. str1 = "ABABAB", str2 = "ABAB"
        # str2 + str2 = "ABABABABAB", str1 is a substring of str2 + str2
        # if str1 is not a multiple of str2, then str1 cannot be a substring of str2 + str2

        if str1 != base * (len(str1) // len(base)) or str2 != base * (len(str2) // len(base)):
            return False
        return True
        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # because we want to find the longest common divisor,
        # we start from the shorter string
        if len(str1) > len(str2): 
            str1, str2 = str2, str1
        
        # base is the longest common divisor
        base = str1
        while base:
            if self.is_valid(base, str1, str2):
                return base
            base = base[:-1]
        return ""
    
    
s = Solution()
print(s.gcdOfStrings("ABABAB", "ABAB"))