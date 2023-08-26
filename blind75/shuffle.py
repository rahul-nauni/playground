nums = [1,1,2,2]
n = 2

i = 0
j = n
ans = []
while i < n and j < 2*n:
    ans.append(nums[i])
    ans.append(nums[j])
    i += 1
    j += 1

print(ans)

