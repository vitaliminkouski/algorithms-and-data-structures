#include <fstream>
#include <deque>
#include <vector>


int main() {
    std::ifstream fin("huffman.in");

    int n;
    fin >> n;

    std::vector<int> frequences(n);

    for (int i = 0; i < n; i++) {
        fin >> frequences[i];
    }
    fin.close();

    std::vector<int> sec_vect;


    long long result = 0;
    int sum_of_mins;
    int min1, min2;

    int index = 0;
    int temp_size;
    while (n + sec_vect.size() > 1) {
        if (sec_vect.empty() || (!sec_vect.empty() and sec_vect[sec_vect.size() - 1] > frequences[index])) {
            min1=frequences[index];
            index++;
            n--;
        }
        else {
            min1 = sec_vect.back();
            sec_vect.pop_back();
        }

        if (sec_vect.empty() || (!sec_vect.empty() and sec_vect[sec_vect.size() - 1] > frequences[index])) {
            min2 = frequences[index];
            index++;
            n--;
        }
        else {
            min2 = sec_vect.back();
            sec_vect.pop_back();
        }

        sum_of_mins = min1 + min2;

        result += sum_of_mins;
        sec_vect.push_back(sum_of_mins);
        temp_size = sec_vect.size();
        if (temp_size>sec_vect[temp_size - 1] > sec_vect[temp_size - 2]) {

        }
    }

    std::ofstream fout("huffman.out");

    fout << result;

    fout.close();
    return 0;
}