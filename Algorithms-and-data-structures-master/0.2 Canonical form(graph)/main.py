import numpy as np

with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    can_form = np.zeros((n), dtype=int)
    for i in range(n - 1):
        e1, e2 = map(int, f.readline().split())
        can_form[e2 - 1] = e1

with open("output.txt", "w") as f:
    for i in range(n):
        f.write(f"{can_form[i]} ")
