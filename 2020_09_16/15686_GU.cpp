#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int N, M, chicken;
vector<pair<int,int>> home;
vector<pair<int,int>> chicken_;

int comb(int r)
{
	vector<int> iter, d;
	int dist = 0, res = 999999;
	for (int i = 0; i < chicken-r; i++) {
		iter.push_back(0);
	}
	for (int i = 0; i < r; i++) {
		iter.push_back(1);
	}
	for (int i = 0; i < home.size(); i++) {
		d.push_back(999999);
	}
	// 집에서 가장 가까운! ! ! !
	do {
		for (int i = 0; i < iter.size(); i++) {
			if (iter[i]) {
				for (int j = 0; j < home.size(); j++) {
					dist = 0;
					dist += abs(chicken_[i].first - home[j].first);
					dist += abs(chicken_[i].second - home[j].second);
					d[j] = min(d[j], dist);
				}
			}
		}
		int tmp = 0;
		for (int i = 0; i < home.size(); i++) {
			tmp += d[i];
			d[i] = 999999;
		}
		res = min(res, tmp);
	} while (next_permutation(iter.begin(), iter.end()));

	return res;
}

int main(void)
{	
	chicken = 0;
	int tmp = 0;
	scanf("%d %d", &N, &M);
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			scanf("%d", &tmp);
			if (tmp == 1) { home.push_back(make_pair(i, j)); }
			else if (tmp == 2) {
				chicken_.push_back(make_pair(i, j));
				chicken += 1;
			}
		}
	}

	printf("%d\n", comb(M));
	return 0;
}