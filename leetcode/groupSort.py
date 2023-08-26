arr = [4, 2, 1, 2, 2]

freq = {}
for i in range(len(arr)):
    freq[arr[i]] = freq.get(arr[i], 0) + 1

sorted_freq = sorted(freq.items(), key=lambda x: (x[1], -x[0]), reverse=True)
print(sorted_freq)


# =============================================================================
# create regex to check if string begins and ends with same character
# we can use a backreference to capture the first character and then use it again
# to check if it is the last character
# remember that single character is in itself a match
# =============================================================================

import re
s = "ab"
#regularExpression = r"^(.).*\1$"
regularExpression = r"^.?$ || ^(.).*\1$"
pattern = re.compile(regularExpression)
# explanation:
# ^ - start of string
# (.) - capture group 1, any character
# .* - any number of any character
# \1 - backreference to capture group 1
def check(pattern, s):
    if pattern.match(s):
        print("true")
    else:
        print("false")

check(pattern, s)