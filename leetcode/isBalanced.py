def isBalanced(s):
  brackets = {
    '{': '}',
    '[': ']',
    '(': ')'
  }
  
  stack = []
  
  for char in s:
    if char in brackets:
      stack.append(char)
    else:
      if brackets[stack.pop()] != char:
        return False
  
  return True

s = "{)"
print(isBalanced(s))