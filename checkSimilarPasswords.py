from typing import List
"""check if newPassword is subsequence of oldPassword
    if yes, return true
    else return false
    use two pointers
    one for oldPassword
    one for newPassword
    take new password , choose set of indices and
    change the characters at those indices to next character in alphabet
    check if oldPassword is subsequence of newPassword
    if yes, return true
    else return false
    a subsequence is a sequence that can be derived from another sequence
    by deleting some or no elements without changing the order of the remaining elements"""

# is old password subsequence of new password
def isSubsequence(old: str, new: str) -> bool:
    if len(old) < len(new):
        return False
    
    i, j = 0, 0
    while i < len(old) and j < len(new):
        if old[i] == new[j]:
            j += 1
        i += 1
    return j == len(new)


def checkSimilarPasswords(oldPasswords: List[str], newPasswords: List[str]) -> List[bool]:
    res = []
    for oldPassword, newPassword in zip(oldPasswords, newPasswords):
        if len(oldPassword) > len(newPassword):
            return False
        
        i, j = 0, 0
        while i < len(oldPassword) and j < len(newPassword):
            if oldPassword[i] == newPassword[j] or oldPassword[i] == chr(ord(newPassword[j]) + 1):
                i += 1
            j += 1
        
        if i == len(oldPassword):
            res.append("YES")
        else:
            res.append("NO")
    return res
   

newPasswords = ["baacbab", "accdb", "baacba"]
oldPasswords = ["abdbc", "ach", "abb"]
print(checkSimilarPasswords(oldPasswords, newPasswords))
# print(isSubsequence("abbaac", "abc"))