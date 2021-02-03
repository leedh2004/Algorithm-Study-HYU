#include <iostream>
using namespace std;

int main(void)
{
	int N, F,i;
	cin >> N;
	cin >> F;

	N = (N / 100)*100;

	for (i = 0; i < 100; i++)
	{
		int N_ = N + i;
		if (N_ % F == 0) { break; }
	}

	if (i < 10)
		cout << 0;
	cout << i;
	return 0;
}