import numpy as np


def find_parent(parent_arr, u):
    if (parent_arr[u] != u):
        parent_arr[u] = find_parent(parent_arr, parent_arr[u])
        return parent_arr[u]
    return u


def set_union(parent_arr, size_arr, u, v, temp_amount):
    parent_u = find_parent(parent_arr, u)
    parent_v = find_parent(parent_arr, v)
    if (parent_u != parent_v):
        if (size_arr[parent_u] < size_arr[parent_v]):
            parent_arr[parent_u] = parent_v
            size_arr[parent_v] += size_arr[parent_u]
        else:
            parent_arr[parent_v] = parent_u
            size_arr[parent_u] += size_arr[parent_v]
        return temp_amount - 1
    return temp_amount


with open("input.txt", "r") as f:
    cities_amount, requests_amount = map(int, f.readline().split())
    parent_arr = np.empty((cities_amount), dtype="int")
    size_arr = np.empty((cities_amount), dtype="int")
    for i in range(cities_amount):
        parent_arr[i] = i
        size_arr[i] = 1

    temp_amount = cities_amount
    components = []
    for i in range(requests_amount):
        u, v = map(int, f.readline().split())
        u -= 1
        v -= 1
        temp_amount = set_union(parent_arr, size_arr, u, v, temp_amount)
        components.append(temp_amount)

with open("output.txt", "w") as f:
    for i in range(len(components)):
        f.write(f"{components[i]}\n")
