#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int dy[4] = { -1, 0, 1, 0 };// north east south west
int dx[4] = { 0, 1, 0, -1 };

bool check[50][50];
int field[50][50];
int N;
int M;
int r;
int c;
int d;

int DFS(int r, int c, int d)
{
	int clean = 0;
	int next_x, next_y;

	while (true)
	{
		if (field[r][c] == 0) {
			field[r][c] = 2;
			clean++;
		}

		int turn = 0;

		for (int i = 0; i < 4; i++)
		{
			d = (d + 3) % 4; // turn left
			next_x = c + dx[d];
			next_y = r + dy[d];

			if (field[next_y][next_x] != 0 ||next_x < 0 || next_x >= M || 
				next_y < 0 || next_y >= N) {
				turn++;
				continue;
			}

			if (field[next_y][next_x] == 0) {
				r = next_y;
				c = next_x;
				break;
			}
		}

		if (turn == 4)
		{
			if (field[r-dy[d]][c-dx[d]] == 1 || c - dx[d] < 0 || c - dx[d] >= M ||
				r - dy[d] < 0 || r - dy[d] >= N) {
				break;
			}
			else {
				r -= dy[d];
				c -= dx[d];
			}
		}
	}

	return clean;
}

int main(void)
{
	memset(field, -1, sizeof(field));
	
	N=0;
	M = 0;
	r = 0;
	c = 0;
	d = 0;

	cin >> N >> M;
	cin >> r >> c >> d;

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> field[i][j];
		}
	}

	cout << DFS(r, c, d);

	return 0;
}