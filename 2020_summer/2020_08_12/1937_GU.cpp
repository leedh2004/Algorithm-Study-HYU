#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int bamboo[500][500];
int d[500][500];
int N;
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };

bool inRange(int i,int j)
{
    return (0 <= i && i < N && 0 <= j && j < N);
}

int dfs(int x, int y)
{
    // 0이 아님 -> 이미 방문
    if (d[x][y] != 0) { return (d[x][y]); }
    // 자기 자신에 있어도 하루는 버티므로 +1
    d[x][y] = 1;
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (inRange(nx, ny) && (bamboo[x][y] < bamboo[nx][ny])) {
            //d[x][y] = x,y 위치에서 시작했을 때 버틸 수 있는 날짜
            d[x][y] = max(d[x][y], dfs(nx,ny) + 1);
        }
    }
    return (d[x][y]);
}

int main()
{
    cin >> N;
    int maximum = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> bamboo[i][j];
            d[i][j] = 0;
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            maximum = max(maximum, dfs(i, j));
        }
    }

    /*for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << d[i][j] << ' ';
        }
        cout << '\n';
    }*/
    cout << maximum;
    return 0;
}


/*     bfs n*n번 -> 메모리초과 ...
int bamboo[501][501];
int d[501][501];
int N;
int maximum;
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };
queue<pair<int, int>> q;

bool inRange(int i, int j)
{
    return (0 < i && i <= N && 0 < j && j <= N);
}

void bfs(int a, int b)
{
    q.push({ a,b });
    //int cnt = 1;
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        if (d[x][y] > maximum) { maximum = d[x][y]; }
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (inRange(nx, ny) && bamboo[x][y] < bamboo[nx][ny]) {
                q.push({ nx,ny });
                d[nx][ny] = max(d[nx][ny], d[x][y] + 1);
            }
        }
    }
}

int main()
{
    cin >> N;
    maximum = 0;

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            cin >> bamboo[i][j];
            d[i][j] = 0;
        }
    }

    for (int j = 0; j <= N; j++) {
        d[0][j] = 0;
    }

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            bfs(i, j);
        }
    }
    cout << maximum + 1;
    return 0;
}*/