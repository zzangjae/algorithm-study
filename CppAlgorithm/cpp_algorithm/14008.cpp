#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <algorithm>
using namespace std;
const int SIZE = 1000002;
int num_lst[SIZE];

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
//		cin >> n;
//
//		for (int i = 0; i < n; i++) {
//			cin >> num_lst[i];
//		}
//
//		sort(num_lst, num_lst + n);
//		cout << '#' << test_case << ' ' << num_lst[n / 2] << endl;
//	}
//}