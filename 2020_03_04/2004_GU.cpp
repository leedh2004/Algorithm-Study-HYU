#include <iostream>
using namespace std;
int main(void)
{
	long long N, M,cnt5=0,cnt2=0;
	cin >> N >> M;
	
	for (long long i = 5; i <= N; i *= 5)
		cnt5 += N / i;
	for (long long i = 5; i <= N - M; i *= 5)
		cnt5 -= (N - M) / i;
	for (long long i = 5; i <= M; i *= 5)
		cnt5 -= M / i;
	for (long long i = 2; i <= N; i *= 2)
		cnt2 += N / i;
	for (long long i = 2; i <= N - M; i *= 2)
		cnt2 -= (N - M) / i;
	for (long long i = 2; i <= M; i *= 2)
		cnt2 -= M / i;

	if (cnt5 >= cnt2)
		cout << cnt2;
	else
		cout << cnt5;
	return 0;
}
/*
int main(void)
{
	long long N,M;
	cin >> N >> M;

	long long upper = 1, bottom = 1, res = 0;
	if (N == M or M ==0)
	{
		cout << 0;
	}
	else
	{
		if (M > (N / 2))
		{
			M = (N - M);
		}
		for (long long i = 0; i < M; i++)
		{
			upper *= (N - i);
			bottom *= (M - i);
		}
		if (bottom == 0)
		{
			return -1;
		}
		else
			res = upper / bottom;
		int len = 0;
		long long tmp = res;
		do{
			tmp = tmp / 10;
			len++;
		} while (tmp> 0);
		int cnt = 0;
		while(true)
		{
			if ((res % 10) != 0 || res == 0)
			{
				break;
			}
			else {
				cnt++;
				res /= 10;
			}
		}
		cout << cnt;
	}
	return 0;
}*/