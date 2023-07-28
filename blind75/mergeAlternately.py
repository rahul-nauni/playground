from collections import deque
def mergeAlternately(word1: str, word2: str) -> str:
        q = deque()
        for i in range(min(len(word1), len(word2))):
            q.append(word1[i])
            q.append(word2[i])
        
        if len(word1) > len(word2):
            q.append(word1[len(word2):])
        elif len(word2) > len(word1):
            q.append(word2[len(word1):])
        
        return "".join(q)


word1 = "abc"
word2 = "pqrs"
print(mergeAlternately(word1, word2))