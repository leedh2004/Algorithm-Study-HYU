#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
	long long N, res = 0, f = 0;
	int cipher = 0;
	cin >> N;
	for (int i = 9; i > -1; i--)
	{
		if (N < pow(10, i) && N >= pow(10,i-1)) {
			cipher = i;
			break;
		}
	}
	
	for (int i = 1; i < cipher; i++)
	{
		res += i* 9 * pow(10, i-1);
		f += 9 * pow(10, i - 1);
	}

	res += cipher * (N - f);

	cout << res;
	return 0;
}