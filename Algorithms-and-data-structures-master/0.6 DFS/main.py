import numpy as np

label=1

def DFS(matrix, num_of_v, labels_arr, v, visited_arr):
    global label
    visited_arr[v]=True
    labels_arr[v]=label
    label+=1

    for i in range(num_of_v):
        if(matrix[v][i] and not visited_arr[i]):
            DFS(matrix, num_of_v, labels_arr, i, visited_arr)



with open("input.txt", "r") as f:
    num_of_v = int(f.readline().strip())
    matrix = np.empty((num_of_v, num_of_v), dtype="int")
    for i in range(num_of_v):
        matrix[i] = np.fromstring(f.readline(), sep=" ", dtype="int")


labels_arr = np.empty((num_of_v), dtype="int")
visited_arr = np.full((num_of_v), False, dtype=np.bool)

for v in range(num_of_v):
    if not visited_arr[v]:
        DFS(matrix, num_of_v, labels_arr, v, visited_arr)
with open("output.txt", "w") as f:
    for i in range(num_of_v):
        f.write(f"{labels_arr[i]} ")