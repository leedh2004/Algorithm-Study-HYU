#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<pair<int, int>> info;
int main(void)
{
	int T = 0, N = 0, x,y;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int s_min = 100000, m_min = 100000, res = 0;
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			cin >> x >> y;
			if (x == 1) {
				m_min = y;
			}
			else{ info.push_back({ x,y }); }
		}
		
		if (info.empty()) { cout << 1 << '\n'; }
		else {
			sort(info.begin(), info.end());
			vector<pair<int, int>>::iterator it;
			for (it = info.begin(); it != info.end();it++)
			{
				if (it->second < m_min) { 
					res++;
					m_min = it->second;
				}
			}
			cout << res + 1 << '\n';
		}
		info.clear();
	}

	return 0;
}

/*
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<pair<int, int>> info;
int main(void)
{
	int T = 0, N = 0, x,y;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int s_min = 100000, m_min = 100000, res = 0;
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			cin >> x >> y;
			if (x == 1) {
				m_min = y;
				//cout << m_min << '\n';
			}
			if (y == 1) {
				s_min = x;
				//cout << s_min << '\n';
			}
			if (x != 1 && y != 1) {
				info.push_back({ x,y });
			}
		}

		if (info.empty()) { cout << N << '\n'; }
		else {
			vector<pair<int, int>>::iterator it;
			for (it = info.begin(); it != info.end();it++)
			{
				if (it->first < s_min && it->second < m_min) { res++; }
			}
			cout << res + 2 << '\n';
		}
		info.clear();
	}

	return 0;
}
*/