#include <iostream>
#include <fstream>
#include <vector>

int main() {
    std::ifstream fin("input.txt");
    std::ofstream fout("output.txt");

    int m, c, keys_amount;
    fin >> m >> c >> keys_amount;

    std::vector<int> hash_table(m, -1);

    for (int i = 0; i < keys_amount; i++) {
        int num;
        fin >> num;
        int position = num % m;
        while (hash_table[position] != -1) {
            position = (position + c) % m;
        }
        hash_table[position] = num;
    }

    for (int i = 0; i < m; i++) {
        fout << hash_table[i] << " ";
    }

    fin.close();
    fout.close();
    return 0;
}
