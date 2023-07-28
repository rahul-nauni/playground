arr = [1, 2, 3, 4, 5]
minimum = min(arr)
maximum = max(arr)

arr.remove(minimum)
arr.remove(maximum)
common = sum(arr)
print(minimum + common, maximum + common)