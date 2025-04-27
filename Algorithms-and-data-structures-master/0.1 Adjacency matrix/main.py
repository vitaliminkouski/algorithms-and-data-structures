import numpy as np

with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    matrix = np.zeros((n, n), dtype="int")
    for i in range(m):
        v1, v2 = map(int, f.readline().split())
        v1 -= 1
        v2 -= 1
        matrix[v1][v2] = 1
        matrix[v2][v1] = 1

with open("output.txt", "w") as f:
    for i in range(n):
        for j in range(n):
            f.write(f"{matrix[i][j]} ")
        f.write("\n")
