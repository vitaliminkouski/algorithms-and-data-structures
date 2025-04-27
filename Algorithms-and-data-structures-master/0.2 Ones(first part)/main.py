import numpy as np

len_of_row, num_of_ones = map(int, input().split())

matrix = np.empty((len_of_row + 1, len_of_row + 1), dtype=np.int64)

for i in range(len_of_row + 1):
    matrix[i][0] = 1
    matrix[i][i] = 1
    for j in range(1, i):
        matrix[i][j] = (matrix[i - 1][j] + matrix[i - 1][j - 1]) % (10 ** 9 + 7)

print(matrix[len_of_row][num_of_ones])

