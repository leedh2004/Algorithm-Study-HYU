#include <iostream>
#include <string>
#include <cstring>
using namespace std;
int map[100][100];

int main(void)
{
	int N = 0, row_cnt = 0,col_cnt=0;
	string board;
	cin >> N;
	getline(cin, board);
	memset(map, 0, sizeof(map));

	for (int i = 0; i < N; i++)
	{
		getline(cin, board);
		for (int j = 0; j < board.length(); j++)
		{
			if (board[j] == 'X') {
				map[i][j] = 1;
			}
		}
	}

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (map[i][j]&& j-2>=0)
			{
				if (!map[i][j - 1] && !map[i][j - 2])
					row_cnt++;
			}
			else if (j == N - 1&& j-1>=0)
			{
				if (!map[i][j] && !map[i][j - 1])
					row_cnt++;
			}
		}
	}

	for (int j = 0; j < N; j++)
	{
		for (int i = 0; i < N; i++)
		{
			if (map[i][j] && i - 2 >= 0)
			{
				if (!map[i-1][j] && !map[i-2][j])
					col_cnt++;
			}
			else if (i == N - 1 && i - 1 >= 0)
			{
				if (!map[i][j] && !map[i-1][j])
					col_cnt++;
			}
		}
	}

	cout << row_cnt << ' ' << col_cnt << '\n';
	return 0;
}