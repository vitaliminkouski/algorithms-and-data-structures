#include <fstream>
#include <vector>
#include <queue>


const long long INF = 4000000000;

std::vector<long long> run_Dijkstra(int n, const std::vector<std::vector<std::pair<int, int>>>& adjacency_matrix, int start = 1) {
    std::vector<long long> dist(n + 1, INF);
    std::vector<bool> visited(n + 1, false);
    dist[start] = 0;

    std::priority_queue<std::pair<long long, int>, std::vector<std::pair<long long, int>>, std::greater<>> heap;
    heap.push({ 0, start });

    long long cur_dist;
    int v;
    while (!heap.empty()) {
        cur_dist = heap.top().first;
        v = heap.top().second;
        heap.pop();
        if (visited[v])
            continue;
        visited[v] = true;

        for (const auto& edge : adjacency_matrix[v]) {
            int u = edge.first;
            int w = edge.second;
            if (dist[v] + w < dist[u]) {
                dist[u] = dist[v] + w;
                heap.push({ dist[u], u });
            }
        }
    }
    return dist;
}

int main() {
    std::ifstream fin("input.txt");

    int n, m;
    fin >> n >> m;

    std::vector<std::vector<std::pair<int, int>>> adjacency_matrix(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v, cost;
        fin >> u >> v >> cost;
        adjacency_matrix[u].push_back({ v, cost });
        adjacency_matrix[v].push_back({ u, cost });
    }
    fin.close();

    std::vector<long long> dist = run_Dijkstra(n, adjacency_matrix, 1);
    std::ofstream fout("output.txt");
    fout << dist[n];
    fout.close();

    return 0;
}
