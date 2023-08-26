# how many bit flips to make a string of all 0s equal to target string
# 1. if the first bit is 1, flip it
# 2. if the next bit is different from the previous bit, flip it
# 3. repeat step 2 until the end of the string
# end
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
