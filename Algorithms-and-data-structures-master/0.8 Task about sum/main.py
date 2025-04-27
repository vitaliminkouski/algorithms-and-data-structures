import numpy as np
import sys

arr_len = int(sys.stdin.readline())
arr = np.fromstring(sys.stdin.readline(), sep=" ", dtype="int64")
requests_amount = int(sys.stdin.readline())
arr_of_requests = []
for i in range(requests_amount):
    parts = sys.stdin.readline().split()
    if parts[0] == "Add":
        i = int(parts[1])
        x = int(parts[2])
        arr_of_requests.append((0, i, x))
    else:
        l = int(parts[1])
        r = int(parts[2])
        arr_of_requests.append((1, l, r))

size = 4 * arr_len
arr_of_left_bounds = np.zeros(size, dtype="int64")
arr_of_right_bounds = np.zeros(size, dtype="int64")
intermedia_result_arr = np.zeros(size, dtype="int64")

def build_segment_tree(left_bound, right_bound, index):
    arr_of_left_bounds[index] = left_bound
    arr_of_right_bounds[index] = right_bound
    if left_bound == right_bound:
        intermedia_result_arr[index] = arr[left_bound]
        return
    mid = (left_bound + right_bound) // 2
    build_segment_tree(left_bound, mid, 2*index+1)
    build_segment_tree(mid+1, right_bound, 2*index+2)
    intermedia_result_arr[index] = intermedia_result_arr[2*index+1] + intermedia_result_arr[2*index+2]

def find_sum_between(l, r, index=0):
    if arr_of_right_bounds[index] < l or arr_of_left_bounds[index] >= r:
        return 0
    if l <= arr_of_left_bounds[index] and arr_of_right_bounds[index] < r:
        return intermedia_result_arr[index]
    return find_sum_between(l, r, 2*index+1) + find_sum_between(l, r, 2*index+2)

def add_value(index, pos, value):
    if arr_of_left_bounds[index] == arr_of_right_bounds[index]:
        intermedia_result_arr[index] += value
        return
    mid = (arr_of_left_bounds[index] + arr_of_right_bounds[index]) // 2
    if pos <= mid:
        add_value(2 * index + 1, pos, value)
    else:
        add_value(2 * index + 2, pos, value)
    intermedia_result_arr[index] = intermedia_result_arr[2*index+1] + intermedia_result_arr[2*index+2]

build_segment_tree(0, arr_len-1, 0)

for req in arr_of_requests:
    if req[0] == 0:
        add_value(0, req[1], req[2])
    else:
        res = find_sum_between(req[1], req[2])
        print(res)