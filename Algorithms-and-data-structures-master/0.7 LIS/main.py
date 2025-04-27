INF = 10**9 + 1

def upper_bound(arr, len_of_arr, x):
    right_index = len_of_arr
    left_index = 0
    while left_index < right_index:
        middle_index = (right_index + left_index) // 2
        if arr[middle_index] > x:
            right_index = middle_index
        else:
            left_index = middle_index + 1
    return left_index

with open('input.txt', 'r') as f:
    len_of_seq = int(f.readline().strip())
    seq = list(map(int, f.readline().split()))

dp = [-float('inf')] + [INF] * len_of_seq

for num in seq:
    j = upper_bound(dp, len_of_seq + 1, num)
    if dp[j - 1] < num < dp[j]:
        dp[j] = num

max_len = max(i for i in range(len_of_seq + 1) if dp[i] < INF)

with open('output.txt', 'w') as f:
    f.write(f'{max_len}')