#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int N, S;
vector<int> A;

int comb(int r)
{
	vector<int> iter;
	int tmp = 0, cnt = 0;
	for (int i = 0; i < N-r; i++) {
		iter.push_back(0);
	}
	for (int i = 0; i < r; i++) {
		iter.push_back(1);
	}

	do {
		tmp = 0;
		for (int i = 0; i < iter.size(); i++) {
			if (iter[i]) {
				tmp += A[i];
			}
		}
		if (tmp == S) {
			cnt += 1;
		}
	} while (next_permutation(iter.begin(), iter.end()));

	return cnt;
}

int main(void)
{	
	int tmp, res=0;
	scanf("%d %d", &N, &S);
	for (int i = 0; i < N; i++) {
		scanf("%d", &tmp);
		A.push_back(tmp);
	}
	// 수열 크기 1부터 N개
	for (int i = 1; i <= N; i++) {
		res += comb(i);
	}
	printf("%d\n", res);
	return 0;
}