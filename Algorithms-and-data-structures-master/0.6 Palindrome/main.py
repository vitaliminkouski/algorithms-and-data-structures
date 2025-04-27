import numpy as np

with open('input.txt', 'r') as f:
    str = f.readline()

str_len = len(str)

matrix = np.empty((str_len, str_len), dtype=int)
for i in range(0, str_len - 1):
    matrix[i][i] = 1
    if (str[i] == str[i + 1]):
        matrix[i][i + 1] = 2
    else:
        matrix[i][i + 1] = 1
matrix[str_len - 1][str_len - 1] = 1

for j in range(2, str_len):
    for i in range(j - 2, -1, -1):
        if str[i] == str[j]:
            matrix[i][j] = matrix[i + 1][j - 1] + 2
        else:
            matrix[i][j] = max(matrix[i + 1][j], matrix[i][j - 1])


palindrome = ""
i = 0
j = str_len - 1
while (i <= j):
    if (str[i] == str[j]):
        palindrome += str[i]
        i += 1
        j -= 1
    elif (matrix[i][j] == matrix[i + 1][j]):
        i += 1
    else:
        j -= 1

temp_len = matrix[0][-1] // 2

for k in range(temp_len - 1, -1, -1):
    palindrome += palindrome[k]
with open('output.txt', 'w') as f:
    f.write(f'{matrix[0][-1]}\n')
    f.write(palindrome)