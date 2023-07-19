ans = []
digitToChar = {
            "2": ["a", "b", "c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

digits = "23"

def backtracking(idx, curStr):
    if idx == len(digits):
        ans.append(curStr)
        return
    for letter in digitToChar[digits[idx]]:
        backtracking(idx+1, curStr+letter)

backtracking(0, "")
print(ans)
print(len(ans))