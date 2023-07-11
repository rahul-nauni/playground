"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false"""

def isValid(s:str) -> bool:
    stack = []
    lookup = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    if len(s) % 2 != 0:
        return False
    for i in range(0,len(s)):
        if s[i] in lookup:
            stack.append(s[i])
        elif len(stack) == 0 or (ord(lookup[stack.pop()]) - ord(s[i])) % 2 != 0:
            return False
    return True if len(stack) == 0 else False

s = "(]"
if isValid(s):
    print('Valid')
else:
    print('Invalid')

