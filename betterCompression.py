import re
def is_char(s):
    regex = re.compile('[a-zA-Z]')
    if regex.match(s):
        return True
    else:
        return False

def betterCompression(s):
    # Write your code here
    dict = {}
    freq = ""
    res = ""
    prev = ""

    for char in s:
        if is_char(char):
            if freq:
                dict[prev] += int(freq)
                freq = ""
            if char not in dict:
                dict[char] = 0
            prev = char
            continue
        freq += char
    dict[prev] += int(freq)
    keys_sorted = sorted(dict.keys())
    for key in keys_sorted:
        res = res + key + str(dict[key])
    return res


s = "d12a12b56a3c1b20d44"
print(betterCompression(s))
