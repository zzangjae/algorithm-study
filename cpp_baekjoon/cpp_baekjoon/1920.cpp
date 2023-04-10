#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <algorithm>
using namespace std;
int n, m;
const int SIZE = 100'000;
int a[SIZE];

bool binary_search(int num) {

	int left, mid, right;

	left = 0;
	right = n-1;

	while (left <= right) {
		mid = (left + right) / 2;

		if (a[mid] == num) return true;
		else if (a[mid] > num) {
			right = mid - 1;
		}
		else {
			left = mid + 1;
		}
	}

	return false;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	freopen("input.txt", "r", stdin);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}

	cin >> m;
	sort(a, a + n);

	for (int i = 0; i < m; i++) {
		int temp_num;
		cin >> temp_num;
		if (binary_search(temp_num)) cout << 1 << endl;
		else cout << 0 << endl;
	}

	return 0;
}