def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

def palindromIndex(s):
    if isPalindrome(s):
        return -1
    else:
        for i in range(len(s)):
            print(f"{s[:i]} + {s[i+1:]}")
            if isPalindrome(s[:i]+s[i+1:]):
                return i
        return -1

s = "cabababd"
print(palindromIndex(s))