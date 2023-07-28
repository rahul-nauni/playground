def breakPalindrome(palindrome: str) -> str:
    if len(palindrome) == 1:
        return ""
    
    for i in range(len(palindrome)//2):
        if palindrome[i] != "a":
            newstr = palindrome[:i] + "a" + palindrome[i+1:]
            if newstr < palindrome:
                return newstr
        newstr = palindrome[:-1] + "b"
        if newstr < palindrome:
            return newstr
    return "IMPOSSIBLE"

palindrome = "ab"
print(breakPalindrome(palindrome))
