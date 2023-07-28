from collections import defaultdict, Counter

s = "loveleetcode"
def firstUniqChar(s):
    uniq = -1
    counter = Counter(s)
    print(counter.most_common()[-1])
    
    for i in range(len(s)):
        if counter[s[i]] == 1:
            uniq = i
            break
    return uniq 

print(firstUniqChar(s))
