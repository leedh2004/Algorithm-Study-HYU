#include <iostream>
#include <cstring>
using namespace std;

struct CCTV
{
	int type, r, c;
};
CCTV cctv[8];
int cctv_cnt;
int N, M;
int ans = 64;
int map[8][8];

//int direction[4] = { 0,1,2,3 }; // north east south west
int dy[4] = { -1,0,1,0 };
int dx[4] = { 0,1,0,-1 };

void map_cpy(int desc[8][8], int src[8][8])
{
	for (int r = 0; r < N; ++r)
		for (int c = 0; c < M; ++c)
			desc[r][c] = src[r][c];
}

void watch(int r,int c, int d)
{
	d %= 4;
	if (d == 0) {
		while (r - 1 >= 0) {
			r--;
			if (map[r][c] == 6) break;
			if(map[r][c]==0) map[r][c] = -1;
		}
	}
	else if (d == 1) {
		while (c + 1 <= M - 1) {
			c++;
			if (map[r][c] == 6) break;
			if (map[r][c] == 0) map[r][c] = -1;
		}
	}
	else if (d == 2) {
		while (r + 1 <= N-1) {
			r++;
			if (map[r][c] == 6) break;
			if (map[r][c] == 0) map[r][c] = -1;
		}
	}
	else {
		while (c - 1 >= 0) {
			c--;
			if (map[r][c] == 6) break;
			if (map[r][c] == 0) map[r][c] = -1;
		}
	}
}

void solve(int cctv_idx)
{
	if (cctv_idx == cctv_cnt)
	{
		int cnt = 0;
		for (int r = 0; r < N; r++)
		{
			for (int c = 0; c < M; c++)
			{
				if (map[r][c] == 0)
					cnt++;
			}
		}
		if (ans > cnt)
			ans = cnt;
	}

	int c_type = cctv[cctv_idx].type;
	int r = cctv[cctv_idx].r;
	int c = cctv[cctv_idx].c;
	int K;
	
	int before[8][8];
	map_cpy(before, map);
	switch (c_type) {

	case 1:
		for (int dir = 0; dir < 4; dir++) {
			watch(r,c,dir);
			solve(cctv_idx + 1);

			map_cpy(map, before);
		}
		break;

	case 2:
		for (int dir = 0; dir < 2; dir++) {
			watch(r,c,dir);
			watch(r, c,dir+2);
			solve(cctv_idx + 1);

			map_cpy(map, before);
		}
		break;

	case 3:
		for (int dir = 0; dir < 4; dir++) {
			watch(r, c, dir);
			watch(r, c, (dir+1)%4);
			solve(cctv_idx + 1);

			map_cpy(map, before);
		}
		break;

	case 4:
		for (int dir = 0; dir < 4; dir++) {
			watch(r, c, dir);
			watch(r, c, (dir+1)%4);
			watch(r, c, (dir+2)%4);
			solve(cctv_idx + 1);

			map_cpy(map, before);
		}
		break;

	case 5:
		for (int dir = 0; dir < 4; dir++)
			watch(r, c, dir);

		solve(cctv_idx + 1);
		map_cpy(map, before);
	}

}
	
	


int main(void)
{
	//ios::sync_with_stdio(false);
	//cin.tie(NULL); cout.tie(NULL);

	M = 0;
	N = 0;
	cctv_cnt = 0;

	cin >> N >> M;
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			cin >> map[i][j];
			if (map[i][j] >= 1 && map[i][j] <= 5) {
				cctv[cctv_cnt].r = i;
				cctv[cctv_cnt].c = j;
				cctv[cctv_cnt].type = map[i][j];
				++cctv_cnt;
			}
		}
	}
	solve(0);
	cout << ans;

	return 0;
}