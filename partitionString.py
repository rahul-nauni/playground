"""
class Solution:
    def __init__(self):
        self.count = 1
        self.partitions = set()

    def partitionString(self, s: str) -> int:
        seen = set()
        sub = ""
        for i, ch in enumerate(s):
            if ch not in seen:
                sub += ch
                seen.add(ch)
            elif ch in seen or i == len(s):
                if sub in self.partitions:
                    while sub in self.partitions:
                        sub = sub[:-1]
                self.partitions.add(sub)
                self.count += 1
                seen.clear()
                return self.partitionString(s[len(sub):])    
        return self.count
"""

class Solution:
    def partitionString(self, s: str):
        count = 1
        seen = set()
        for i, ch in enumerate(s):
            if ch not in seen:
                seen.add(ch)
            elif ch in seen:
                count += 1
                seen.clear()
                seen.add(ch)
        return count


s = "abacaba"
sol = Solution()
print(sol.partitionString(s))
