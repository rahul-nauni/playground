from typing import List
def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maxCandies = max(candies)
    res = [True if candies[i] >= maxCandies - extraCandies else False for i in range(len(candies))]
    return res

candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))