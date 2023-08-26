from typing import List


def sumDiagonal(arr: List[List[int]], startIndex: int, endIndex: int, direction: List[int], step: int) -> int:
    next_col = -1
    diagSum = 0
    for i in range(startIndex, endIndex, step):
        next_row = i + direction[0]
        next_col += direction[1]
        diagSum += arr[next_row][next_col]

    return diagSum


def diagonalDifference(arr: List[List[int]]) -> int:
    n = len(arr)  # matrix size

    left = 0
    right = 0

    directions = [
        [1, 1],  # left diag
        [-1, 1]  # right diag
    ]
    primary = True
    if primary:
        left = sumDiagonal(arr, -1, n-1, directions[0], 1)
        primary = False
    if not primary:
        right = sumDiagonal(arr, n, 0, directions[1], -1)

    diff = abs(left - right)
    return diff


arr = [
    [11, 2, 4],
    [4, 5, 6],
    [10, 8, -12]
]
print(diagonalDifference(arr))

