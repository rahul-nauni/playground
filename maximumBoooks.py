from typing import List

def maximumBoooks(books: List[int]):
    if not books:
        return 0
    
    n = len(books)
    # we build a dp array of size n+1
    # dp[i] represents the maximum number of books from 0 to i
    dp = [0] * (n+1)
    dp[0] = books[0]
    stack = [books[0]]

    for i in range(1, n):
        for j in range(i+1, n):
            stack.append(books[j])
            if books[j] > books[i]:
                dp[j] = max(dp[i] + 1, dp[j])
            else:
                dp[j] = dp[i]
        stack = []
        

    return max(dp)

books = [8,5,2,7,9]
print(maximumBoooks(books))