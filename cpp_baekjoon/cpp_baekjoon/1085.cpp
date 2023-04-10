#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <set>
#include <string>
using namespace std;

struct Compare {
	bool operator() (const string &a, const string &b) const {
		if (a.size() == b.size()) return a < b;
		else return a.size() < b.size();
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	freopen("input.txt", "r", stdin);

	cin >> n;
	set<string, Compare> temp_set;

	for (int i = 0; i < n; i++) {
		string temp_string;
		cin >> temp_string;
		temp_set.insert(temp_string);
	}

	for (string temp_string : temp_set) {
		cout << temp_string << endl;
	}

	return 0;
}