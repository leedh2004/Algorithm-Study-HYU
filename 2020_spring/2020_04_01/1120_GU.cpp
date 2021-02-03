#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(void)
{
	string a, b;
	cin >> a >> b;
	int diff = 0, tmp = 0, res = 50;
	int cal = b.size() - a.size();
	int a_len = a.size();
	int b_len = b.size();
	int minimum = 999999;
	for (int i = 0; i <= cal; i++)
	{
		tmp= 0;
		for (int j = 0; j < a_len; j++)
		{
			if (a[j] != b[i + j]) tmp++;
		}
		res = min(res, tmp);
	}

	cout << res << '\n';

	return 0;
}

/*
int chk_diff(string a, string b)
{
	int diff = 0;
	for (int i = 0; i < a.size(); i++)
	{
		if (a[i] != b[i]) diff++;
	}

	return diff;
}

int main(void)
{
	string a, b;
	cin >> a >> b;
	int diff = 0;
	int cal = b.size() - a.size();
	int b_len = b.size();

	for (int i = 0; i < cal; i++)
	{
		int tmp = 0;
		tmp = chk_diff(b[0] + a, b);
		if (chk_diff(a + b[b_len - 1], b) >= tmp)
		{
			a = b[0] + a;
		}
		else {
			a = a + b[b_len - 1];
		}
	}

	cout << chk_diff(a, b);


	return 0;
}*/