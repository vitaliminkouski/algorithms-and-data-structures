with open("input.txt", "r") as f:
    heap_len = int(f.read())

x = 1
with open("output.txt", "w") as f:
    for i in range(63):
        if (x & heap_len):
            f.write(f"{i}\n")
        heap_len=heap_len>>1
