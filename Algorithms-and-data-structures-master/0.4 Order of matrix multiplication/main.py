import numpy as np


def min_matrix_mult_ord(amount_of_matrices, matrix_of_dmn):
    matrix = np.empty((amount_of_matrices, amount_of_matrices), np.int64)
    for i in range(amount_of_matrices - 1):
        matrix[i][i] = 0
        matrix[i][i + 1] = matrix_of_dmn[i][0] * matrix_of_dmn[i][1] * matrix_of_dmn[i + 1][1]
    matrix[amount_of_matrices - 1][amount_of_matrices - 1] = 0

    for k in range(2, amount_of_matrices):
        for i in range(0, amount_of_matrices - k):
            j = k + i
            matrix[i][j] = matrix[i + 1][j] + \
                           matrix_of_dmn[i][0] * matrix_of_dmn[i][1] * matrix_of_dmn[j][1]
            for l in range(i + 1, j):
                temp_amount = matrix[i][l] + matrix[l + 1][j] + \
                              matrix_of_dmn[i][0] * matrix_of_dmn[l][1] * matrix_of_dmn[j][1]
                if (temp_amount < matrix[i][j]):
                    matrix[i][j] = temp_amount
    return matrix[0][amount_of_matrices - 1]


with open('input.txt', 'r') as f:
    amount_of_matrices = int(f.readline())
    matrix_of_dimensities = np.empty((amount_of_matrices, 2), np.int32)
    for i in range(amount_of_matrices):
        matrix_of_dimensities[i][0], matrix_of_dimensities[i][1] = map(int, f.readline().split())

with open('output.txt', 'w') as f:
    f.write(f'{min_matrix_mult_ord(amount_of_matrices, matrix_of_dimensities)}')
