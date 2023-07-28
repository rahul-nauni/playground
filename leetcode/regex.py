import re
def is_char(s):
    regex = re.compile('[a-zA-Z]')
    if regex.match(s):
        return True
    else:
        return False
    
def get_count(s):
    count = ""
    for char in s:
        if is_char(char):
            break
        count += char
    return count

def betterCompression(s):
    dict = {}
    res = ""

    while s:
        count = get_count(s)
        s = s[len(count):]
        if not s:
            break
        char = s[0]
        s = s[1:]
        if char not in dict:
            dict[char] = 0
        dict[char] += int(count)
        

    keys_sorted = sorted(dict.keys())
    for key in keys_sorted:
        res = res + key + str(dict[key])
    return res

s = "d12a12b56a3c1b20d44"
print(betterCompression(s))