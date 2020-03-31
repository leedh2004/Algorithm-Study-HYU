#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
vector<int> a,b,c;

int main(void)
{
	int x, y,tmp;
	int x_ = 0, y_ = 0,z_ = 0;
	cin >> x >> y;

	while (x!=0)
	{
		a.push_back(x % 10);
		x /= 10;
	}
	while (y != 0)
	{
		b.push_back(y % 10);
		y /= 10;
	}
	int x_sz = a.size();
	int y_sz = b.size();
	for (int i = 0; i < x_sz; i++)
	{
		tmp = a.back();
		x_ += (int(pow(10, i))*tmp);
		a.pop_back();
	}
	for (int i = 0; i < y_sz; i++)
	{
		tmp = b.back();
		y_ += (int(pow(10, i)) * tmp);
		b.pop_back();
	}
	//cout << x_ << ' ' << y_;
	int z = x_ + y_;
	while (z != 0)
	{
		c.push_back(z % 10);
		z /= 10;
	}
	int z_sz = c.size();

	for (int i = 0; i < z_sz; i++)
	{
		tmp = c.back();
		z_ += (int(pow(10, i)) * tmp);
		c.pop_back();
	}

	cout << z_ << '\n';

	return 0;
}