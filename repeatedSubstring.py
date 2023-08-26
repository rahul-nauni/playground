def repeatedSubstringPattern(s: str) -> bool:
    if len(s) < 2:
        return False
    
    # find repeated substring
    # if s is a repeated substring, then s must be a substring of s + s
    # e.g. s = "abab", s + s = "abababab", s is a substring of s + s
    # if s is not a repeated substring, then s cannot be a substring of s + s
    # e.g. s = "abab", s + s = "abababab", s is not a substring of s + s

    # divide and conquer
    def divide(s, left, right) -> bool:
        if left == right:
            return False
        mid = (left + right) // 2
        if s in (s + s)[mid+1:-1]:
            return True
        else:
            return divide(s, left, mid) or divide(s, mid+1, right)
        
    return divide(s, 0, len(s)-1)

s = "babbabbabbabbab"
print(repeatedSubstringPattern(s))