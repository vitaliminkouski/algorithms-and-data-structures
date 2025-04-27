#include <iostream>
#include <vector>

int find_parent(std::vector<int>& parent_arr, int u) {
    if (parent_arr[u] != u) {
        parent_arr[u] = find_parent(parent_arr, parent_arr[u]);
        return parent_arr[u];
    }
    return u;
}

int set_union(std::vector<int>& parent_arr, std::vector<int>& size_arr, int u, int v, int temp_amount) {
    int parent_u = find_parent(parent_arr, u);
    int parent_v = find_parent(parent_arr, v);

    if (parent_u!=parent_v)
    {
        if (size_arr[parent_u] < size_arr[parent_v])
        {
            parent_arr[parent_u] = parent_v;
            size_arr[parent_v] += size_arr[parent_u];
        }
        else {
            parent_arr[parent_v] = parent_u;
            size_arr[parent_u] += size_arr[parent_v];
        }
        return temp_amount - 1;
    }
    return temp_amount;
}

int main() {
    int cities_amount, roads_amount;
    std::cin >> cities_amount>> roads_amount;
    std::vector<int> parent_arr(cities_amount);
    std::vector<int> size_arr(cities_amount, 1);
    for (int i = 0; i < cities_amount; i++)
    {
        parent_arr[i] = i;
    }

    std::vector<std::pair<int, int>> roads(roads_amount);
    for (int i = 0; i < roads_amount; i++){
      std::cin >> roads[i].first >> roads[i].second;
    }

    int temp_amount = cities_amount;
    for (int i = 0; i < roads_amount; i++)
    {
        temp_amount = set_union(parent_arr, size_arr, roads[i].first-1,
                              roads[i].second-1, temp_amount);

        if(temp_amount == 1){
          std::cout << temp_amount;
          break;
        }
    }


    return 0;
}