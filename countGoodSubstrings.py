class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        
        left = 0
        right = 0
        count = 0
        seen = set()

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                if len(seen) == 3:
                    count += 1
                    left += 1
                    right = left
                    seen.clear()
                    continue
            else:
                seen.clear()
                left += 1
                right = left
                continue
        return count

s = "aababcabc"
sol =  Solution()
print(sol.countGoodSubstrings(s))
