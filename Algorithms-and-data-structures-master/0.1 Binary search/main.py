import numpy as np
import sys

len_of_arr = int(sys.stdin.readline())
arr = np.fromstring(sys.stdin.readline(), sep=' ', dtype=np.int16)
num_of_requests = int(sys.stdin.readline())
arr_of_requests = np.fromstring(sys.stdin.readline(), sep=' ', dtype=np.int16)


def binary_search(arr, len_of_arr, x):
    right_index = len_of_arr
    left_index = 0
    while left_index < right_index:
        middle_index = (right_index + left_index) // 2
        if (arr[middle_index] == x):
            return 1
        elif (arr[middle_index] > x):
            right_index = middle_index
        else:
            left_index = middle_index + 1
    return 0


def lower_bound(arr, len_of_arr, x):
    right_index = len_of_arr
    left_index = 0
    while (left_index < right_index):
        middle_index = (right_index + left_index) // 2
        if (arr[middle_index] >= x):
            right_index = middle_index
        else:
            left_index = middle_index + 1
    return left_index


def upper_bound(arr, len_of_arr, x):
    right_index = len_of_arr
    left_index = 0
    while (left_index < right_index):
        middle_index = (right_index + left_index) // 2
        if (arr[middle_index] > x):
            right_index = middle_index
        else:
            left_index = middle_index + 1
    return left_index


for request in arr_of_requests:
    b = binary_search(arr, len_of_arr, request)
    l = lower_bound(arr, len_of_arr, request)
    r = upper_bound(arr, len_of_arr, request)
    sys.stdout.write(f'{b} {l} {r}\n')
