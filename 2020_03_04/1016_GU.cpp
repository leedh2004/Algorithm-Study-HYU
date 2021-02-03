#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;
static long long check[1000001];
int main(void)
{
	memset(check, false, sizeof(check));
	long long min, max, cnt = 0;
	cin >> min >> max;
	for (long long i = 2; i * i <= max; i++) {

		long long x = min / (i * i);
		if (min % (i * i) != 0)
			x++;

		while (x * (i * i) <= max) {
			check[x * (i * i) - min] = true;
			x++;
		}

	}
	for (int i = 0; i <= max - min; i++) {
		if (check[i] == 0)
			cnt++;
	}

	cout << cnt;
	return 0;
}

/* why .......
int main(void)
{
	memset(check, false, sizeof(check));
	//memset(dv_by_square, false, sizeof(dv_by_square));
	long long min, square, max, cnt = 0;
	cin >> min >> max;

	long long sq_max = (long long)sqrt(max);
	for (long long i = 2; i * i <= max; i++) {
		if (check[i] == false) {
			for (long long j = i * i; j <= max; j++) {
				check[j] = true;
			}
		}
	}
	for (long long i = 2; i <= sq_max; i++) {
		if (check[i]) { continue; }
		square = i * i; // sosu good
		for (long long j = min; j <= max; j++) {
			if (j % square == 0) {
				cnt++;
			}
		}
	}

	cout << (max - min + 1) - cnt;
	return 0;
}
*/

/* run fucg time f error
int main(void)
{
	memset(check, false, sizeof(check));
	//memset(dv_by_square, false, sizeof(dv_by_square));
	long long minimum,square, maximum,cnt=0;
	cin >> minimum >> maximum;

	long long sq_max = (long long)sqrt(maximum);

	for (long long i = 2; i <= sq_max; i++) { // i가 개쳐딸림
		// 이미 체크된 수의 배수들은 합성수임이 자명
		if (check[i] == true)
			continue;
		// i를 제외한 i의 배수들을 0으로 체크
		for (long long j = i + i; j <= maximum; j += i) {
			check[j] = true;
		}
	}

	for (long long i = 2; i <= sq_max; i++)
	{
		if (check[i] == true) { continue; } // i is sosu
		square = i * i;
		for (long long j = minimum; j <= maximum; j++) // j가 딸림
		{
			//if (j < square || dv_by_square[j]) { continue; }
			if (j % square == 0) {
				cnt++;
				//dv_by_square[j] = true;
			}
		}
	}

	cout << (maximum - minimum +1) -cnt;
	return 0;
}
*/

/* time over fuck
#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
vector<long long> squares;
long long is_prime(long long n)
{
	if (n == 1) return 0;
	long long i = 0, root = 0;
	root = long(sqrt(n));
	for (i = 2; i <= root; i++)
	{
		if (n % i == 0) return 0;
	}
	return 1;
}


int main(void)
{
	long long min, max, cnt = 0, tmp = 0;
	cin >> min >> max;

	for (long long i = 2; i <= max; i++)
	{
		if (is_prime(i) == 1)
		{
			squares.push_back(i);
			//printf("%lld ", i);
		}
	}
	vector<long long>::iterator it;
	for (long long i = min; i <= max; i++)
	{
		for (it = squares.begin(); it != squares.end(); it++)
		{
			tmp = (*it) * (*it);
			if (tmp > i) { break; }
			if (i % tmp == 0) {
				cnt++;
				break;
			}
		}
	}

	cout << (max - min + 1) - cnt;
	return 0;
}*/

//static long long squares[999999];
//vector<long long> squares;
//vector<long long> nums;
/*
for (long long i = min; i <= max; i++)
{
	nums.push_back(i);
}

for (long long i = 2; i * i < max; i++)
{
	squares.push_back(i * i);
}
vector<long long>::iterator it;
for (it = squares.begin(); it != squares.end();it++)
{
	cout << *it << '\n';
}

for (long long i = 0; i < squares.size(); i++)
{
	for (it = nums.begin();it!=nums.end();)
	{
		if (*it % squares[i] == 0)
		{
			it = nums.erase(it);
			cnt++;
		}
		else
			it++;
	}
}
*/