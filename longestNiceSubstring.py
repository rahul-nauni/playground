# string s is nice if
# every alphabet in s appears as both lowercase and uppercase
# Example: abABB -> 'a' and 'A' appear, 'b' and 'B' appear.
# abA is not nice -> 'b' appears but 'B' does not.
from typing import Set

# approach:
# for every lowercase alphabet check remaining substring for uppercase
# keep track of what alphabets we have seen so far in set
# O(n^2) time complexity

class Solution:
    @staticmethod
    def is_valid(window: Set[str]) -> bool:
        for char in window:
            if char.lower() not in window or char.upper() not in window:
                return False
        return True

    def longestNiceSubstring(self, s: str):
        # if there are none, return empty string
        if len(s) <= 1:
            return ""

        # sliding pointers
        left = 0
        right = 0
        n = len(s)
        window = set()
        longest = ""

        return longest


s = "abAAB"
sol = Solution()
print(sol.longestNiceSubstring(s))
