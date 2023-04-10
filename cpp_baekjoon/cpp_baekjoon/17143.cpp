#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
using namespace std;


const int SIZE = 101;
int board[SIZE][SIZE][4];
int directions[5][2] = { {0, 0}, {-1, 0}, {1, 0}, {0, 1}, {0, -1} };
int board_r, board_c, shark_num;
int angler_c;
int result;


void move(int r, int c) {

	if (board[r][c][2] != 0) {
		int speed = board[r][c][0];
		int direction = board[r][c][1];
		int size = board[r][c][2];
		int is_moved = board[r][c][3];

		int temp_r = r + directions[direction][0] * speed;
		int temp_c = c + directions[direction][1] * speed;
		int temp_direction = direction;

		while (!(1 <= temp_r && temp_r <= board_r && 1 <= temp_c && temp_c <= board_c))
		{
			if (temp_r < 1) { temp_r = -1 * (temp_r - 1) + 1; temp_direction = 2; }
			else if (temp_r > board_r) { temp_r = board_r - (temp_r - board_r); temp_direction = 1; }

			if (temp_c < 1) { temp_c = -1 * (temp_c - 1) + 1; temp_direction = 3;}
			else if (temp_c > board_c) { temp_c = board_c - (temp_c - board_c); temp_direction = 4; }
		}

		board[r][c][0] = 0;
		board[r][c][1] = 0;
		board[r][c][2] = 0;
		board[r][c][3] = 0;

		if (board[temp_r][temp_c][3] == 1) {
		move(temp_r, temp_c);
		}
		
		if (board[temp_r][temp_c][2] == 0) {
			board[temp_r][temp_c][0] = speed;
			board[temp_r][temp_c][1] = temp_direction;
			board[temp_r][temp_c][2] = size;
		}
		else if (board[temp_r][temp_c][2] < size) {
			board[temp_r][temp_c][0] = speed;
			board[temp_r][temp_c][1] = temp_direction;
			board[temp_r][temp_c][2] = size;
		}
	}
}


int main() {
	freopen("input.txt", "r", stdin);

	cin >> board_r >> board_c >> shark_num;

	for (int i = 0; i < shark_num; i++) {
		int r, c, s, d, z;
		cin >> r >> c >> s >> d >> z;

		board[r][c][0] = s;
		board[r][c][1] = d;
		board[r][c][2] = z;
		board[r][c][3] = 1;
	}

	angler_c = 1;

	while (angler_c <= board_c) {

		for (int i = 1; i <= board_r; i++) {
			if (board[i][angler_c][2] != 0) {
				result += board[i][angler_c][2];
				board[i][angler_c][0] = 0;
				board[i][angler_c][1] = 0;
				board[i][angler_c][2] = 0;
				board[i][angler_c][3] = 0;
				break;
			}
		}

		for (int r = 1; r <= board_r; r++) {
			for (int c = 1; c <= board_c; c++) {
				if (board[r][c][3] == 1) move(r, c);
			}
		}

		for (int r = 1; r <= board_r; r++) {
			for (int c = 1; c <= board_c; c++) {
				if (board[r][c][2] != 0) board[r][c][3] = 1;
			}
		}

		angler_c++;
	}

	cout << result;
	return 0;
}