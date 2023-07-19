s="ceabaacb"

def minCut(s):
    if len(s) <= 0:
        return 0


    charMap = {}
    charSet = set()
    count = 0

    for char in s:
        charMap[char] = charMap.get(char, 0) + 1

    for value in charMap.values():
        while value in charSet and value != 0:
            value -= 1
            count += 1
        charSet.add(value)

    return count


print(minCut(s))


    