arr = [5, 3, 2, 4, 1]

sorted_arr = sorted(arr)
print(sorted_arr)

i, j = 0, len(sorted_arr) - 1

while j > i:
    i += 1
    j -= 1

print(i)
median = sorted_arr[i]
print(median)