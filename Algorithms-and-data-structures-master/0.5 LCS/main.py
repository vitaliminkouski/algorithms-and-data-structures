import numpy as np

len_of_seq = int(input())
first_seq = np.fromstring(input(), sep=' ', dtype=int)
second_seq = np.fromstring(input(), sep=' ', dtype=int)

matrix = np.zeros((len_of_seq + 1, len_of_seq + 1), dtype=int)

for i in range(1, len_of_seq + 1):
    for j in range(1, len_of_seq + 1):
        if (first_seq[i - 1] == second_seq[j - 1]):
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])

first_list_of_indices = []
second_list_of_indices = []
i = j = len_of_seq
while (i != 0 and j != 0):
    if (first_seq[i - 1] == second_seq[j - 1]):
        first_list_of_indices.append(i - 1)
        second_list_of_indices.append(j - 1)
        i -= 1
        j -= 1
    elif (matrix[i][j] == matrix[i - 1][j]):
        i -= 1
    else:
        j -= 1
first_list_of_indices.reverse()
second_list_of_indices.reverse()
print(*first_list_of_indices)
print(*second_list_of_indices)
