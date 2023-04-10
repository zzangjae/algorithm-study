#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <set>
const int SIZE = 101;
int union_lst[SIZE];
using namespace std;


int find_union(int x) {

	if (union_lst[x] == x) return x;

	return find_union(union_lst[x]);
}

void make_union(int x, int y) {
	int root_x = find_union(x);
	int root_y = find_union(y);

	if (root_x != root_y) union_lst[root_y] = root_x;
}

int main(int argc, char** argv)
{
	int test_case;
	int t;

	freopen("input.txt", "r", stdin);
	cin >> t;

	for (test_case = 1; test_case <= t; ++test_case){
		int n, m;
		cin >> n >> m;


		for (int i = 1; i <= n; i++) {
			union_lst[i] = i;
		}

		for (int i = 0; i < m; i++) {
			int x, y;
			cin >> x >> y;
			make_union(x, y);
		}

		set<int> temp_set;
		for (int i = 1; i <= n; i++) {
			temp_set.insert(find_union(i));
		}

		cout << '#' << test_case << ' ' << temp_set.size() << endl;

	}


	return 0;
}