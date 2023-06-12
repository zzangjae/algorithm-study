#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <stdio.h>
using namespace std;
const int SIZE = 14;

short operators[4];
short cards[SIZE];
int n;
long maximum = -100000000;
long minimum = 100000000;

long get_min(short depth, long temp_sum);
long get_max(short depth, long temp_sum);

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
//		cin >> n;
//
//		for (int i = 0; i < 4; i++) {
//			cin >> operators[i];
//		}
//
//		for (int i = 0; i < n; i++) {
//			cin >> cards[i];
//		}
//
//		maximum = -100000000;
//		minimum = 100000000;
//
//		get_min(0, cards[0]);
//		get_max(0, cards[0]);
//
//		cout << "#" << test_case << ' ' << maximum - minimum << endl;
//	}
//	return 0;
//}

long get_min(short depth, long temp_sum) {

	if (depth == n-1) {
		if (minimum > temp_sum) minimum = temp_sum;
		return 0;
	}

	for (int i = 0; i < 4; i++) {
		if (operators[i] > 0) {
			switch (i) {
			case 0:
				operators[i]--;
				get_min(depth + 1, temp_sum + cards[depth + 1]);
				operators[i]++;
				break;
			case 1: 
				operators[i]--;
				get_min(depth + 1, temp_sum - cards[depth + 1]);
				operators[i]++;
				break;
			case 2:
				operators[i]--;
				get_min(depth + 1, temp_sum * cards[depth + 1]);
				operators[i]++;
				break;
			case 3:
				operators[i]--;
				get_min(depth + 1, temp_sum / cards[depth + 1]);
				operators[i]++;
				break;
			}
		}
	}

	return 0;
}

long get_max(short depth, long temp_sum) {

	if (depth == n-1) {
		if (temp_sum > maximum) maximum = temp_sum;
		return 0;
	}

	for (int i = 0; i < 4; i++) {
		if (operators[i] > 0) {
			switch (i) {
			case 0:
				operators[i]--;
				get_max(depth + 1, temp_sum + cards[depth + 1]);
				operators[i]++;
				break;
			case 1:
				operators[i]--;
				get_max(depth + 1, temp_sum - cards[depth + 1]);
				operators[i]++;
				break;
			case 2:
				operators[i]--;
				get_max(depth + 1, temp_sum * cards[depth + 1]);
				operators[i]++;
				break;
			case 3:
				operators[i]--;
				get_max(depth + 1, temp_sum / cards[depth + 1]);
				operators[i]++;
				break;
			}
		}
	}

	return 0;
}