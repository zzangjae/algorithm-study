#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <deque>
using namespace std;
const int SIZE = 100;
int visited[SIZE][SIZE];
int cost_lst[SIZE][SIZE];
int dr[4] = { -1, 0, 1, 0 };
int dc[4] = { 0, 1, 0, -1 };
int n;

struct Position {
	int r;
	int c;
};

int main(int argc, char** argv)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int t;

	freopen("input.txt", "r", stdin);
	cin >> t;
	
	for (int tc_num = 1; tc_num <= t; ++tc_num)
	{
		cin >> n;

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> cost_lst[i][j];
				visited[i][j] = 100000000;
			}
		}

		visited[0][0] = 0;
		deque<Position> queue;
		queue.push_back({ 0, 0 });

		while (!queue.empty())
		{
			int r = queue.front().r;
			int c = queue.front().c;
			queue.pop_front();

			for (int i = 0; i < 4; i++) {

				int temp_r = r + dr[i];
				int temp_c = c + dc[i];

				if (0 <= temp_r && temp_r < n && 0 <= temp_c && temp_c < n) {
					int temp_cost = (cost_lst[temp_r][temp_c] - cost_lst[r][c]) > 0 ? 1 + (cost_lst[temp_r][temp_c] - cost_lst[r][c]) : 1;

					if (visited[temp_r][temp_c] > visited[r][c] + temp_cost) {
						visited[temp_r][temp_c] = visited[r][c] + temp_cost;
						queue.push_back({ temp_r, temp_c });
					}
				}
			}
		}
		
		cout << '#' << tc_num << ' ' << visited[n - 1][n - 1] << endl;
	}

	return 0;
}

