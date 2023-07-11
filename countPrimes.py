# Description: Count the number of prime numbers less than a non-negative number, n.
start = 1
end = 11

count = 0
for i in range(start, end+1):
    if i == 1:
        continue
    if i == 2:
        count += 1
    elif i % 2 == 0:
        continue
    else:
        for j in range(3, i, 2): # start at 3, end at i, step by 2 because even numbers are not prime
            print(f"i: {i}, j: {j}")
            if i % j == 0: # if i is divisible by j, it is not prime because it has a factor other than 1 and itself
                break
        else:
            count += 1

print(f"Prime numbers in range: {count}")