#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
const int SIZE = 1001;
Microbiome biomes[SIZE];
int dr[5] = {0, -1, 1, 0, 0 };
int dc[5] = {0,  0, 0, -1, 1 };
int n, m, k;

struct Microbiome
{
	int root_node;
	int row;
	int column;
	int microbe;
	int direction;
};


void move(Microbiome *biome) {
	int r = biome->row;
	int c = biome->column;
	int microbe = biome->microbe;
	int direction = biome->direction;

	int temp_r = r + dr[direction];
	int temp_c = c + dc[direction];

	if (temp_r == 0 || temp_r == n - 1 || temp_c == 0 || temp_c == n - 1) {
		biome->row = temp_r;
		biome->column = temp_c;
		biome->direction = (direction % 2) ? direction + 1 : direction - 1;
		biome->microbe = microbe / 2;
	}
	else {
		biome->row = temp_r;
		biome->column = temp_c;
	}
}

int main(int argc, char** argv)
{
	int test_case;
	int t;

	freopen("input.txt", "r", stdin);
	cin >> t;

	for (test_case = 1; test_case <= t; ++test_case)
	{
		cin >> n >> m >> k;

		for (int i = 1; i <= k; i++) {
			int r, c, microbe, direction;
			cin >> r >> c >> microbe >> direction;
			biomes[i] = {i, r, c, microbe, direction };
		}

		for (int i = 1; i <= m; i++) {

			for (int j = 1; j <= k; k++){
				if (biomes[j].root_node == j) move(&biomes[j]);
			}
		}

		for (Microbiome biome : biomes) {
			cout << '#' << test_case << ' ' << biome.row << ' ' << biome.column << ' ' << biome.microbe << endl;
		}
	}

	return 0;
}