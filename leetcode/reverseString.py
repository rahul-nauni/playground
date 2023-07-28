# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

s = ["h","e","l","l","o"]

def reverseString(s):
    start = len(s) - 1
    end = 0
    while start > end:
        s[start], s[end] = s[end], s[start]
        start -= 1
        end += 1
    print(s)
reverseString(s)