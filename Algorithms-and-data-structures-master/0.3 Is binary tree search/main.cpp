#include <iostream>
#include <fstream>
#include <vector>
#include <limits>
#include <string>

struct Node {
    long long value;
    int left = -1;
    int right = -1;
    int parent = -1;
};

std::string is_binary_tree_search(const std::vector<Node>& tree, int nodes_amount) {


    std::vector<std::pair<long long, long long>> intervals;
    intervals.push_back({ LLONG_MIN, LLONG_MAX });

    for (int i = 1; i < nodes_amount; i++) {
        long long value = tree[i].value;
        int parent_index = tree[i].parent;
        long long min_value, max_value;

        if (tree[parent_index].left == i) {
            min_value = intervals[parent_index].first;
            max_value = tree[parent_index].value;
        }
        else {
            min_value = tree[parent_index].value;
            max_value = intervals[parent_index].second;
        }

        intervals.push_back({ min_value, max_value });
        if (value < min_value || value >= max_value)
            return "NO";
    }
    return "YES";
}

int main() {
    std::ifstream fin("bst.in");
    std::ofstream fout("bst.out");

    int n;
    fin >> n;

    if (n == 0) {
        fout << "YES";
        return 0;
    }

    std::vector<Node> tree(n);
    fin >> tree[0].value;

    for (int i = 1; i < n; i++) {
        long long value;
        int parent;
        char side;
        fin >> value >> parent >> side;
        tree[i].value = value;
        tree[i].parent = parent - 1;

        if (side == 'L') {
            tree[parent - 1].left = i;
        }
        else {
            tree[parent - 1].right = i;
        }
    }

    fout << is_binary_tree_search(tree, n);

    return 0;
}
