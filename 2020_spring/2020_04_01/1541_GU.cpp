#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main(void)
{
	vector<char> op;
	vector<int> tmp_, nums;
	string expression;
	getline(cin, expression);

	for (int i = 0; i < expression.length(); i++)
	{
		if (expression[i] <= '9' && expression[i] >= '0') {
			tmp_.push_back(expression[i] - '0');
		}
		else {
			int a = 0, j = 0;
			while (!tmp_.empty()) {
				a += tmp_.back() * int(pow(10, j));
				tmp_.pop_back();
				j++;
			}
			nums.push_back(a);
			op.push_back(expression[i]);
		}
	}

	int a = 0, i = 0;
	while (!tmp_.empty()) {
		a += tmp_.back() * int(pow(10, i));
		tmp_.pop_back();
		i++;
	}
	nums.push_back(a);

	for (int i = 0; i < op.size();) {
		if (op[i] == '+') {
			int tmp = nums[i] + nums[i + 1];
			nums[i] = tmp;
			nums.erase(nums.begin() + i+1);
			op.erase(op.begin() + i);
		}
		else{
			i++;
		}
	}
	int res = nums[0];
	for (int i = 1; i < nums.size(); i++)
	{
		res -= nums[i];
	}

	cout << res;
	/*
	vector<int>::iterator it;
	vector<char>::iterator cit;
	for (it = nums.begin(); it != nums.end(); it++) {
		cout << *it << " ";
	}
	for (cit = op.begin(); cit != op.end(); cit++) {
		cout << *cit << " ";
	}*/


	return 0;
}