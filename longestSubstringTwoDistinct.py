from collections import defaultdict
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
        if len(s) == 1:
            return 0
        
        seen = defaultdict(int)
        longest = 0
        left = 0
        right = 0
        while right < len(s):
            seen[s[right]] += 1

            if len(seen) > 2:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                left += 1
            longest = max(longest, right-left+1)
            right += 1
        return longest

s = "ccaabbb"
print(lengthOfLongestSubstringTwoDistinct(s))