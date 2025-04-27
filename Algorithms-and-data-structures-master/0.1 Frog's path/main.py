import numpy as np
import sys

len_of_arr = int(sys.stdin.readline())
arr_of_mosquitos = np.fromstring(sys.stdin.readline(), sep=' ', dtype=np.int32)

if(len_of_arr==1):
    print(arr_of_mosquitos[0])
    print(1)
elif (len_of_arr == 2):
    print(-1)
else:
    arr = np.empty(len_of_arr, dtype=np.int64)
    arr[0] = arr_of_mosquitos[0]
    arr[1] = -1
    arr[2] = arr_of_mosquitos[2] + arr_of_mosquitos[0]
    for i in range(3, len_of_arr):
        arr[i] = arr_of_mosquitos[i] + max(arr[i - 2], arr[i - 3])
    print(arr[len_of_arr - 1])

    i = len_of_arr - 1
    path = []
    while i >= 2:
        path.append(i + 1)
        previous_count_of_mosquitos = arr[i] - arr_of_mosquitos[i]
        if (arr[i - 2] == previous_count_of_mosquitos):
            i -= 2
        else:
            i -= 3
    path.append(1)
    path.reverse()
    print(*path)
