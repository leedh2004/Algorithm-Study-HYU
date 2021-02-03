#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N;
int adj[1001][1001];
vector<int> route;

void Euler(int now)
{
	for (int i = 1; i <= N; i++) {
		if (adj[now][i]) {
			while (adj[now][i] > 0) {
				adj[now][i]--;
				adj[i][now]--;
				Euler(i);
			}
			//Euler(i);
		}
	}
	route.push_back(now);
}

int main(void)
{
	int cnt_ = 0;
	bool Possible = true;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		cnt_ = 0;
		for (int j = 1; j <= N; j++) {
			scanf("%d", &adj[i][j]);
			cnt_ += adj[i][j];
		}
		if (cnt_ % 2 != 0) {
			Possible = false;
			break;
		}
	}

	if (!Possible) {
		printf("-1");
	}
	else {
		Euler(1);
		reverse(route.begin(), route.end());
		for (auto it = route.begin(); it != route.end(); it++) {
			cout << *it << ' ';
		}
	}

	return 0;
}