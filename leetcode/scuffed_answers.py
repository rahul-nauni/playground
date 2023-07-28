def reverse(s):
    return s[::-1]

def swap_answers(C, N):
    for i in range(N):
        if C[i] == "A":
            C = C[:i] + "B" + C[i+1:]
        else:
            C= C[:i] + "A" + C[i+1:]
    return C

C = "BBBBB"
N = len(C)
print(swap_answers(C, N))