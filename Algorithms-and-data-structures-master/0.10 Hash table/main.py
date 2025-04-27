import numpy as np

with open("input.txt", "r") as f:
    m, c, keys_amount = map(int, f.readline().split())

    hash_table = np.full(m, -1, dtype=int)

    for _ in range(keys_amount):
        num = int(f.readline().strip())
        position = num % m
        while hash_table[position] != -1:
            position = (position + c) % m
        hash_table[position] = num

with open("output.txt", "w") as f:
    for i in range(m):
        f.write(f"{hash_table[i]} ")


