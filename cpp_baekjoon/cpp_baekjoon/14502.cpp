#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
using namespace std;
int n, m;
const int SIZE = 8;
int board[SIZE][SIZE];
int result = 0;
vector<pair<int, int>> birus_lst;
int dr[4] = { -1, 0, 1, 0 };
int dc[4] = { 0, 1, 0, -1 };




int get_birus_num() {
	vector<pair<int, int>> stack;
	stack.assign(birus_lst.begin(), birus_lst.end());
	int temp_board[SIZE][SIZE];
	copy(&board[0][0], &board[0][0] + SIZE * SIZE, &temp_board[0][0]);

	while (!stack.empty()) {
		int r, c;
		r = stack.back().first;
		c = stack.back().second;
		stack.pop_back();

		for (int i = 0; i < 4; i++) {
			int temp_r = r + dr[i];
			int temp_c = c + dc[i];

			if (0 <= temp_r && temp_r < n && 0 <= temp_c && temp_c < m) {

				if (temp_board[temp_r][temp_c] == 0) {
					temp_board[temp_r][temp_c] = 2;
					stack.push_back(make_pair(temp_r, temp_c));
				}
			}
		}
	}

	int temp_result = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (temp_board[i][j] == 0) temp_result++;
		}
	}

	return temp_result;
}

void dfs(int r = 0, int c = 0, int walls = 3) {

	if (walls <= 0) {
		int temp_sum = get_birus_num();
		if (temp_sum > result) result = temp_sum;
	}

	else {
		for (int i = r; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (board[i][j] == 0) {
					board[i][j] = 1;
					dfs(i, j, walls - 1);
					board[i][j] = 0;
				}
			}
		}
	}
}



int main() {
	freopen("input.txt", "r", stdin);
	cin >> n >> m;

	for (int r = 0; r < n; r++) {
		for (int c = 0; c < m; c++) {
			cin >> board[r][c];
		}
	}

	for (int r = 0; r < n; r++) {
		for (int c = 0; c < m; c++) {
			if (board[r][c] == 2) birus_lst.push_back(make_pair(r, c));
		}
	}

	dfs();
	cout << result;

	return 0;
}