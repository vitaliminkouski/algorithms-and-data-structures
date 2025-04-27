from collections import deque
import numpy as np


def BFS(matrix, num_of_v):
    label = 1
    labels_arr = np.zeros((num_of_v), dtype="int")
    visited_arr = np.full((num_of_v), False, dtype=np.bool)
    for start in range(num_of_v):

        if (not visited_arr[start]):
            q = deque()
            q.append(start)
            visited_arr[start] = True

            while (len(q) > 0):
                v = q.popleft()
                labels_arr[v] = label
                label += 1
                for i in range(num_of_v):
                    if (matrix[v][i] and not visited_arr[i]):
                        q.append(i)
                        visited_arr[i] = True

    return labels_arr


with open("input.txt", "r") as f:
    num_of_v = int(f.readline().strip())
    matrix = np.empty((num_of_v, num_of_v), dtype="int")
    for i in range(num_of_v):
        matrix[i] = np.fromstring(f.readline(), sep=" ", dtype="int")

labels_arr = np.empty((num_of_v), dtype="int")
labels_arr = BFS(matrix, num_of_v)
with open("output.txt", "w") as f:
    for i in range(num_of_v):
        f.write(f"{labels_arr[i]} ")
