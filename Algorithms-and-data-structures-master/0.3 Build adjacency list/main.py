with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())
    matrix = []
    for i in range(n):
        matrix.append([0])

    for i in range(m):
        v1, v2 = map(int, f.readline().split())
        matrix[v1 - 1].append(v2)
        matrix[v1 - 1][0] += 1

        matrix[v2 - 1].append(v1)
        matrix[v2 - 1][0] += 1

with open("output.txt", "w") as f:
    for i in range(n):
        for x in matrix[i]:
            f.write(f"{x} ")
        f.write("\n")
