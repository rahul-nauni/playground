"""def mySqrt(x: int) -> int:
        count=0
        for i in range(1,x):
            if i%2 != 0:
                x -= i
                count += 1 if x >= 0 else 0
            if x <= 0:
                break
        return count"""

from math import sqrt, floor
def mySqrt(x: int) -> int:
    return floor(sqrt(1))

print(mySqrt(8))