#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
using namespace std;
const int SIZE = 10000;
long long line_lst[SIZE];


int main() {
	freopen("input.txt", "r", stdin);

	long long n, k;
	cin >> k >> n;
	long long max_num = 0;

	for (int i = 0; i < k; i++) {
		cin >> line_lst[i];
		if (line_lst[i] > max_num) max_num = line_lst[i];
	}

	long long temp_result;
	long long left, right, mid;
	left = 1;
	right = max_num;

	while (left <= right) {
		temp_result = 0;
		mid = (left + right) / 2;

		for (int j = 0; j < k; j++) {
			temp_result += line_lst[j] / mid;
		}

		if (temp_result >= n) {
			left = mid + 1;
	
		}
		else {
			right = mid - 1;
		}
	}

	cout << right << endl;
	return 0;
}