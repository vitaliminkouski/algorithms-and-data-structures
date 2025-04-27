#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {
	std::ifstream fin("input.txt"); // Open the file

	std::string str;
	fin >> str;
	fin.close();
	if (!str.size()) {
		return 0;
	}

	int str_len = str.size();
	int** matrix = new int* [str_len];
	for (int i = 0; i < str_len; i++)
	{
		matrix[i] = new int[str_len];
	}

	matrix[str_len - 1][str_len - 1] = 1;
	for (int i = 0; i < str_len - 1; i++)
	{
		matrix[i][i] = 1;
		if (str[i] == str[i + 1]) {
			matrix[i][i + 1] = 2;
		}
		else {
			matrix[i][i + 1] = 1;
		}
	}

	for (int j = 2; j < str_len; j++)
	{
		for (int i = j - 2; i > -1; i--)
		{
			if (str[i] == str[j])
			{
				matrix[i][j] = matrix[i + 1][j - 1] + 2;
			}
			else {
				matrix[i][j] = std::max(matrix[i + 1][j], matrix[i][j - 1]);
			}
		}
	}

	std::vector<char> palindrome;

	int i = 0;
	int j = str_len - 1;
	while (i <= j) {
		if (str[i] == str[j]) {
			palindrome.push_back(str[i]);
			i++;
			j--;
		}
		else if (matrix[i][j] == matrix[i + 1][j]) {
			i++;
		}
		else {
			j--;
		}
	}

	int temp_len = matrix[0][str_len - 1] / 2;
	for (int i = temp_len - 1; i > -1; i--)
	{
		palindrome.push_back(palindrome[i]);
	}



	std::ofstream fout("output.txt");
	fout << matrix[0][str_len - 1] << "\n";
	for (int i = 0; i < palindrome.size(); i++)
	{
		fout << palindrome[i];
	}
	fout.close();


	for (int i = 0; i < str_len; i++)
	{
		delete[] matrix[i];
	}
	delete[] matrix;
	return 0;
}