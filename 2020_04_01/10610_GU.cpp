#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
using namespace std;

int main(void)
{
	string n;
	long long sum = 0;
	bool no_zero = true;
	cin >> n;
	vector<int> nums;
	for(int i=0;i<n.length();i++)
	{
		nums.push_back(n[i]-'0');
		if (n[i] == '0')
			no_zero = false;
		sum += n[i] - '0';
	}
	
	if (no_zero || sum%3 !=0) {
		cout << -1 << '\n';
	}
	else {
		sort(nums.begin(), nums.end(), greater<>());

		vector<int>::iterator it;
		for (it = nums.begin(); it != nums.end(); it++)
			cout << *it;
	}
	return 0;
}