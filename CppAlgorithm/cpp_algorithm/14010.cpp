#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <algorithm>
using namespace std;

int left_search = 0;
int right_search = 0;
const int SIZE = 500002;
int a_lst[SIZE];
int b_lst[SIZE];

int binary_search(int l, int r, int key);

//int main(int argc, char** argv)
//{
//	int test_case;
//	int T;
//
//	freopen("input.txt", "r", stdin);
//	cin >> T;
//
//	for (test_case = 1; test_case <= T; ++test_case)
//	{
//		int n;
//		int m;
//		cin >> n;
//		cin >> m;
//
//		for (int i = 0; i < n; i++) {
//			cin >> a_lst[i];
//		}
//		sort(a_lst, a_lst + n);
//
//		for (int i = 0; i < m; i++) {
//			cin >> b_lst[i];
//		}
//
//		int result = 0;
//
//		for (int i = 0; i < m; i++) {
//			left_search = 0;
//			right_search = 0;
//			
//			if (binary_search(0, n - 1, b_lst[i])) result++;
//		}
//
//		cout << '#' << test_case << ' ' << result << endl;
//	}
//
//	return 0;
//}


int binary_search(int l, int r, int key) {
	int m = (l + r) / 2;

	if (a_lst[m] == key) {
		return key;
	}

	if (l >= r) return 0;

	if (a_lst[m] < key) {
		right_search++;
		left_search = 0;

		if (right_search > 1) return 0;
		else return binary_search(m + 1, r, key);
	}
	else {
		left_search++;
		right_search = 0;
		if (left_search > 1) return 0;
		else return binary_search(l, m - 1, key);
	}
}