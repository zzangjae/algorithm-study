#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
using namespace std;

const short SIZE = 10;
int cost_lst[SIZE][SIZE];
int result;
int n;
bool visit[SIZE] = { false };

int dfs(int depth, int temp_sum, int start_idx);

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
//		for (int i = 0; i < n; i++) {
//			for (int j = 0; j < n; j++) {
//				cin >> cost_lst[i][j];
//			}
//		}
//
//		fill_n(visit, SIZE, false);
//		visit[0] = true;
//		result = 1000;
//
//		dfs(0, 0, 0);
//		cout << '#' << test_case << ' ' << result << endl;
//	}
//
//	return 0;
//}


int dfs(int depth, int temp_sum, int start_idx) {
	cout << depth << ' ' << temp_sum << ' ' << start_idx << endl;
	
	if (depth == n-1) {
		if(temp_sum + cost_lst[start_idx][0] < result) result = temp_sum + cost_lst[start_idx][0];
		return 0;
	}

	for (int i = 0; i < n; i++) {
		if (!(visit[i])) {
			visit[i] = true;
			dfs(depth + 1, temp_sum + cost_lst[start_idx][i], i);
			visit[i] = false;
		}
	}
	return 0;
}