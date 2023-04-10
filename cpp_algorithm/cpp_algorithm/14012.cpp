#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
using namespace std;

short batteries[52];

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
//		for (int i=1; i <= n-1; i++) {
//			cin >> batteries[i];
//		}
//		batteries[n] = 100;
//
//		int result = 0;
//		int station_index = 1;
//
//		while (station_index < n) {
//			int battery_num = batteries[station_index];
//
//			int next_index = 0;
//			int temp_max = 0;
//
//			for (int i = station_index + 1; i <= station_index + battery_num; i++) {
//				if (i + batteries[i] > temp_max) {
//					temp_max = i + batteries[i];
//					next_index = i;
//				}
//			}
//
//			station_index = next_index;
//			result++;
//		}
//
//		cout << '#' << test_case << ' ' << result - 1<< endl;
//	}
//	return 0;
//}