s = 'bab'
t = 'aba'

from collections import Counter
def isAnagram(s, t):
    #return Counter(s) == Counter(t)
    #return sorted(s) == sorted(t)
    if len(s) != len(t):
            return False

    """dict = {}
    count = 0

    for i in range(len(s)):
        dict[s[i]] = dict.get(s[i], 0) + 1

    for char in t:
        if dict.get(char, 0) != 0:
            dict[char] -= 1
        else:
            count += 1
    return True if sum(dict.values()) == 0 else False, count"""
    steps = 0
    s_counter = Counter(s)
    t_counter = Counter(t)

    for char, count in s_counter.items():
        if char not in t_counter:
            steps += count
        else:
            steps += max(count - t_counter[char], 0)
    return True if steps == 0 else False, steps
        

isAnagram, count = isAnagram(s, t)

if isAnagram:
    print('Both strings are anagrams')
else:
    print('Given strings are not anagrams')
    print(f"character to be changed: {count}")