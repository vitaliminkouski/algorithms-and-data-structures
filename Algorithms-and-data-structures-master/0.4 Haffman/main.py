from collections import deque

with open("huffman.in", "r") as f:
    n = int(f.readline().strip())

    freq_deq = deque((map(int, f.readline().split())))



second_deq = deque()
result = 0

while len(freq_deq) + len(second_deq) > 1:
    if not second_deq or (freq_deq and freq_deq[0] <= second_deq[0]):
        min1 = freq_deq.popleft()
    else:
        min1 = second_deq.popleft()

    if not second_deq or (freq_deq and freq_deq[0] <= second_deq[0]):
        min2 = freq_deq.popleft()
    else:
        min2 = second_deq.popleft()

    sum_of_mins = min1 + min2
    result += sum_of_mins
    second_deq.append(sum_of_mins)

with open("huffman.out", "w") as f:
    f.write(f"{result}\n")
