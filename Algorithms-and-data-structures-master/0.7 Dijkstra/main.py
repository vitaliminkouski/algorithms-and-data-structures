import heapq

INF = 2 ** 63 - 1


def run_Dijkstra(n, adjacency_matrix, start=1):
    dist = [INF] * (n + 1)
    visited = [False] * (n + 1)
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        cur_dist, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True

        for (u, w) in adjacency_matrix[v]:
            if dist[v] + w < dist[u]:
                dist[u] = dist[v] + w
                heapq.heappush(heap, (dist[u], u))

    return dist


with open("input.txt", "r") as f:
    n, m = map(int, f.readline().split())

    adjacency_matrix = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v, cost = map(int, f.readline().split())

        adjacency_matrix[u].append((v, cost))
        adjacency_matrix[v].append((u, cost))

dist = run_Dijkstra(n, adjacency_matrix, start=1)

with open("output.txt", "w") as f:
    f.write(f"{dist[n]}")
