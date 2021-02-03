#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void)
{
	int N = 0, res = 0;
	int A[1001],d[1001];
	d[0] = 0;
	scanf("%d", &N);
	for (int i = 1; i <= N; i++) {
		scanf("%d", &A[i]);
		d[i] = 0;
		//printf("%d ", A[i]);
	}
	for (int i = 0; i <= N; i++) {
		int longest = 0;
		for (int j = 0; j < i; j++) {
			if (A[i] < A[j] && d[j] > longest) {
				longest = d[j];
			}
		}
		d[i] = longest + 1;
		res = max(d[i],res);
	}
	printf("%d\n", res);
	return 0;
}