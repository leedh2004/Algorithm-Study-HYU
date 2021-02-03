#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
using namespace std;
int N;
int price[10][10];
int tmp[10][10];
bool chk[10][10];

void check(int i, int j)
{
	chk[i][j] = !chk[i][j];
	chk[i - 1][j] = !chk[i - 1][j];
	chk[i + 1][j] = !chk[i + 1][j];
	chk[i][j - 1] = !chk[i][j - 1];
	chk[i][j + 1] = !chk[i][j + 1];
}

int flower_road(int res, int cnt)
{
	//3 flowers
	if (cnt == 3) { return res; }
	// maximum 3000
	int ans = 999999;

	for (int i = 1; i < N-1; i++) {
		for (int j = 1; j < N-1; j++) {
			// all 5 spaces must be checked
			if (chk[i][j] && chk[i+1][j] && chk[i-1][j] && chk[i][j+1] && chk[i][j-1]) {
				check(i , j);
				ans = min(ans,flower_road(res + price[i][j], cnt + 1));
				check(i , j);
			}
		}
	}
	return ans;
}


int main(void)
{
	//bool chk[10][10];
	scanf("%d", &N);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			scanf("%d", &price[i][j]);
			//tmp for sum of 5 spaces
			tmp[i][j] = price[i][j];
			chk[i][j] = true;
		}
	}

	for (int i = 1; i < N-1; i++) {
		for (int j = 1; j < N-1; j++) {
			price[i][j] += tmp[i][j + 1];
			price[i][j] += tmp[i][j - 1];
			price[i][j] += tmp[i - 1][j];
			price[i][j] += tmp[i + 1][j];
			//printf("%d ", price[i][j]);
		}
		//printf("\n");
	}

	printf("%d", flower_road(0, 0));
	return 0;
}