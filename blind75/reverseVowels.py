def swap(s, i, j):
    s[i], s[j] = s[j], s[i]

def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = list(s)

    start = 0
    end = len(s) - 1
    while start < end:
        if s[start].lower() not in vowels:
            start += 1
        elif s[end].lower() not in vowels:
            end -= 1
        else:
            swap(s, start, end)
            start += 1
            end -= 1
    return "".join(s)

s = "hellodarknessmyoldfriendIvecometotalkwithyouagain"
print(reverseVowels(s))