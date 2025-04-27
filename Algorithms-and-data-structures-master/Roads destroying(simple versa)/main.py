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
    cities_amount, roads_amount, earthquakes_amount = map(int, f.readline().split())
    roads_arr = np.empty((3, roads_amount), dtype="int")

    for i in range(roads_amount):
        roads_arr[0][i], roads_arr[1][i] = map(int, f.readline().split())
        roads_arr[0][i] -= 1
        roads_arr[1][i] -= 1
        roads_arr[2][i] = 0

    roads_nums_to_destroy_arr = np.empty((earthquakes_amount), dtype="int")
    for i in range(earthquakes_amount):
        road_num = int(f.readline().strip()) - 1
        roads_nums_to_destroy_arr[i] = road_num
        roads_arr[2][road_num] = 1

parent_arr = np.empty((cities_amount), dtype="int")
size_arr = np.empty((cities_amount), dtype="int")
for i in range(cities_amount):
    parent_arr[i] = i
    size_arr[i] = 1

components_amount = cities_amount
components_amount_arr = np.empty((earthquakes_amount), dtype="int")

for i in range(roads_amount):
    if (roads_arr[2][i] == 0):
        components_amount = set_union(parent_arr, size_arr, roads_arr[0][i],
                                      roads_arr[1][i], components_amount)

for i in range(earthquakes_amount - 1, -1, -1):
    if (components_amount == 1):
        components_amount_arr[i] = 1
    else:
        components_amount_arr[i] = 0
        components_amount = set_union(parent_arr, size_arr,
                                      roads_arr[0][roads_nums_to_destroy_arr[i]],
                                      roads_arr[1][roads_nums_to_destroy_arr[i]],
                                      components_amount)

with open("output.txt", "w") as f:
    for i in range(earthquakes_amount):
        f.write(f"{components_amount_arr[i]}")
