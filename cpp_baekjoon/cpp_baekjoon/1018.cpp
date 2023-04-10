#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
using namespace std;
const int SIZE = 50;
char board[SIZE][SIZE];


int get_color_num(int r, int c) {
	int temp_result_w = 0;
	int temp_result_b = 0;

	for (int i = r; i < r + 8; i++) {
		for (int j = c; j < c + 8; j++) {
			if ((((i+j) % 2) && board[i][j] == 'W') || (((i + j + 1) % 2) && board[i][j] == 'B')) temp_result_w++;
		}
	}

	for (int i = r; i < r + 8; i++) {
		for (int j = c; j < c + 8; j++) {
			if ((((i + j) % 2) && board[i][j] == 'B') || (((i + j + 1) % 2) && board[i][j] == 'W')) temp_result_b++;
		}
	}

	return (temp_result_b > temp_result_w) ? temp_result_w : temp_result_b;
}

int main() {
	int n, m;
	freopen("input.txt", "r", stdin);

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		cin >> board[i];
	}

	int result = 64;

	for (int i = 0; i <= n - 8; i++) {
		for (int j = 0; j <= m - 8; j++) {
			int temp_result = get_color_num(i, j);
			result = (temp_result < result) ? temp_result : result;
		}
	}

	cout << result << endl;

	return 0;
}
