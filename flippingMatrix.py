def flip(matrix, i):
    n = len(matrix)
    for j in range(n):
        matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix) // 2
    for i in range(n):
        for j in range(n):
            # check four corners
            max_val = max(
                matrix[i][j], # top left
                matrix[i][2 * n - 1 - j], # bottom left
                matrix[2 * n - 1 - i][j], # top right
                matrix[2 * n - 1 - i][2 * n - 1 - j] # bottom right
            )

            if max_val == matrix[i][j]:
                continue
            
            max_val_index = matrix[i].index(max_val)
            if max_val_index >= n:
                flip(matrix, i)
            else:
                flip(matrix, max_val_index)
                



matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
flipped = flippingMatrix(matrix)

for i in range(len(flipped)):
    for j in range(len(flipped[0])):
        print(flipped[i][j], end=' ')
    print()