def minFlips(target: str):
    flips = 0
    for i in range(len(target)):
        if i == 0:
            if target[i] == '1':
                flips += 1
        else:
            if target[i] != target[i-1]:
                flips += 1
    return flips

target = "101"
print(minFlips(target))
