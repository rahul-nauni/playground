def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and ((i == 0 and flowerbed[i+1] == 0) or (i == len(flowerbed) - 1 and flowerbed[i-1] == 0)):
            flowerbed[i] = 1
            n -= 1
        elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            n -= 1
    return n <= 0

flowerbed = [0]
n = 1
print(canPlaceFlowers(flowerbed, n))