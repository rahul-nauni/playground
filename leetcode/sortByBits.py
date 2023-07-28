from typing import List
def sortByBits(arr: List[int]) -> List[int]:
    def countBits(n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    return sorted(arr, key=lambda x: (countBits(x), x))
arr = [0,1,2,3,4,5,6,7,8]
print(sortByBits(arr))