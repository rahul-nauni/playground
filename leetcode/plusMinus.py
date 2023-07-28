arr = [-4, 3, -9, 0, 4, 1]
n = len(arr)
ratios = {}
zeros = 0
positives = 0
negatives = 0
for i in range(n):
    if arr[i] == 0:
        zeros += 1
    elif arr[i] > 0:
        positives += 1
    else:
        negatives += 1
        
ratios["positives"] = positives / n
ratios["negatives"] = negatives / n
ratios["zeros"] = zeros / n

print("{0:.6f}".format(ratios["positives"]))
print("{0:.6f}".format(ratios["negatives"]))
print("{0:.6f}".format(ratios["zeros"]))