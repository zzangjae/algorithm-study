#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
using namespace std;
const short SIZE = 50;
short num_lst[SIZE][SIZE];
short n;
short visit[SIZE][SIZE];

short dfs(short r, short c, short temp_sum);

int main(int argc, char** argv)
{
	short test_case;
	short T;

	freopen("input.txt", "r", stdin);
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case)
	{
		cin >> n;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> num_lst[i][j];
				fill_n(visit[i], n, 130);
			}
		}

		dfs(0, 0, num_lst[0][0]);
		cout << '#' << test_case << ' ' << visit[n-1][n-1] << endl;
	}

	return 0;
}


short dfs(short r, short c, short temp_sum) {

	if (r < n && visit[r + 1][c] > temp_sum + num_lst[r + 1][c]) {
		visit[r + 1][c] = temp_sum + num_lst[r + 1][c];
		dfs(r + 1, c, temp_sum + num_lst[r + 1][c]);
	}

	if (c < n && visit[r][c + 1] >  temp_sum + num_lst[r][c + 1]) {
		visit[r][c + 1] = temp_sum + num_lst[r][c + 1];
		dfs(r, c + 1, temp_sum + num_lst[r][c + 1]);
	}

	return 0;
}
