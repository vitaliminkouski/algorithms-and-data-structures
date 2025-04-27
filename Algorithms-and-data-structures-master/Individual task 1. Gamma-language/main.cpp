#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

void sort(int* arr, int* arr_of_indices, int len_of_arr) {
	std::vector<std::pair<int, int>> temp_vector(len_of_arr);
	for (int i = 0; i < len_of_arr; i++) {
		temp_vector[i] = { arr[i], arr_of_indices[i] };
	}
	std::sort(temp_vector.begin(), temp_vector.end());

	for (int i = 0; i < len_of_arr; i++) {
		arr[i] = temp_vector[i].first;
		arr_of_indices[i] = temp_vector[i].second;
	}
}

int binary_search(int* arr, int len_of_arr, int x) {
	int right_index = len_of_arr;
	int left_index = 0;
	int middle_index;
	while (left_index < right_index) {
		middle_index = (right_index + left_index) / 2;
		if (arr[middle_index] == x) {
			return middle_index;
		}
		else if (arr[middle_index] > x) {
			right_index = middle_index;
		}
		else {
			left_index = middle_index + 1;
		}
	}
	return -1;
}

int lower_bound(int* arr, const int& len_of_arr, const int& x) {
	int right_index = len_of_arr;
	int left_index = 0;
	int middle_index;
	while (left_index < right_index) {
		middle_index = (right_index + left_index) / 2;
		if (arr[middle_index] >= x)
		{
			right_index = middle_index;
		}
		else
		{
			left_index = middle_index + 1;
		}
	}
	return left_index;
}



int main() {
	int len_of_text1, len_of_text2;

	std::ifstream fin("input.txt");
	fin >> len_of_text1;
	fin >> len_of_text2;
	int* text1 = new int[len_of_text1];
	int* text2 = new int[len_of_text2];

	for (int i = 0; i < len_of_text1; i++)
	{
		fin >> text1[i];
	}
	for (int i = 0; i < len_of_text2; i++)
	{
		fin >> text2[i];
	}
	fin.close();

	int* text2_indices = new int[len_of_text2];
	for (int i = 0; i < len_of_text2; i++)
	{
		text2_indices[i] = i;
	}

	sort(text2, text2_indices, len_of_text2);


	int* indices = new int[len_of_text2];
	int indices_amount = 0;
	int index;

	for (int i = 0; i < len_of_text1; i++)
	{
		index = binary_search(text2, len_of_text2, text1[i]);
		if (index != -1)
		{
			indices[indices_amount] = text2_indices[index];
			indices_amount++;
		}
	}


	int* dp = new int[indices_amount];
	int dp_index = 0;
	if (indices_amount > 0)
	{
		dp[0] = indices[0];
		dp_index = 1;
		for (int i = 1; i < indices_amount; i++)
		{
			if (indices[i] > dp[dp_index - 1]) {
				dp[dp_index] = indices[i];
				dp_index++;
			}
			else {
				dp[lower_bound(dp, dp_index, indices[i])] = indices[i];
			}
		}
	}

	std::ofstream fout("output.txt");
	fout << dp_index;
	fout.close();


	delete[] text1;
	delete[] text2;
	delete[] dp;
	delete[] indices;
	delete[] text2_indices;
	return 0;
}