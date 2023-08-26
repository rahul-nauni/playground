def checkSimilarPasswords(oldPassword, newPassword):
    oldPassword = oldPassword.lower()
    newPassword = newPassword.lower()
    # check if oldPassword is subsequence of newPassword
    # if yes, return true
    # else return false
    # use two pointers
    # one for oldPassword
    # one for newPassword
    # take new password , choose set of indices and
    # change the characters at those indices to next character in alphabet
    # check if oldPassword is subsequence of newPassword
    # if yes, return true
    # else return false
    # a subsequence is a sequence that can be derived from another sequence
    # by deleting some or no elements without changing the order of the remaining elements
    

print(checkSimilarPasswords("abdbc", "baacbab"))