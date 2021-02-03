#include <iostream>
#include <queue>
#include <cstring>
#include <cmath>
using namespace std;
int N, L, R;
int A[50][50];
bool visited[50][50];
int dx[4] = { 1,-1,0,0 };
int dy[4] = { 0,0,1,-1 };
queue<pair<int, int>> q; // е╫╩Ж©К
queue<pair<int, int>> alliance; // ©╛гу

int main(void)
{
	cin >> N >> L >> R;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			cin >> A[i][j];
		}
	}

	int ans = 0;
	bool found = true;
	while (found)
	{
		found = false;
		ans += 1;
		memset(visited, false, sizeof(visited));
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (visited[i][j])
					continue;
				int people = A[i][j];
				visited[i][j] = true;
				q.push({ i,j });
				alliance.push({ i,j });

				while (!q.empty())
				{
					int y = q.front().first;
					int x = q.front().second;
					q.pop();

					for (int d = 0; d < 4; d++)
					{
						int ny = y + dy[d];
						int nx = x + dx[d];

						if (0 > ny || ny >= N || 0 > nx || nx >= N || visited[ny][nx] ||
							abs(A[ny][nx] - A[y][x]) < L || abs(A[ny][nx] - A[y][x]) > R)
							continue;
						found = true;
						q.push({ ny,nx });
						alliance.push({ ny,nx });
						people += A[ny][nx];
						visited[ny][nx] = true;

					}
				}
				
				int p = people / alliance.size();

				while (!alliance.empty()) {
					A[alliance.front().first][alliance.front().second] = p;
					alliance.pop();
				}
			}
		}
	}

	cout << ans-1;
	return 0;
}