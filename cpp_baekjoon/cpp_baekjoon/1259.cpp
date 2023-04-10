#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("input.txt", "r", stdin);

	string input_int;
	cin >> input_int;

	do {
		string result = "yes";

		for (int i = 0; i < input_int.size() / 2; i++) {
			if (input_int[i] != input_int[input_int.size() - 1 - i]) result = "no";
		}

		cout << result << endl;
		cin >> input_int;
	} while (input_int != "0");

	return 0;
}