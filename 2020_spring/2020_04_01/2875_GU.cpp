#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
	int N=0, M=0, K=0;
	cin >> N >> M >> K;

	for (int i = 0; i < K; i++)
	{
		if (N / 2 >= M) { N--; }
		else { M--; }
	}

	cout << min(N / 2, M);

	return 0;
}