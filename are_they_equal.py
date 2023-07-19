def are_they_equal(array_a, array_b):
    if len(array_a) != len(array_b):
        return False
    N = len(array_a)
    
    a_count = {}
    b_count = {}
    
    for i in range(N):
        a_count[array_a[i]] = a_count.get(array_a[i], 0) + 1
        b_count[array_b[i]] = b_count.get(array_b[i], 0) + 1

    return a_count == b_count

print(are_they_equal([1, 2, 3, 4], [1, 4, 3, 2]))