#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
#define INF 99999999
vector<pair<int, int>> info;
long long dist[20001];
int N, M;

bool cmp(int a, int b) {
	if (dist[a] > dist[b])
		return b;
	else if (dist[a] == dist[b])
	{
		if (a > b) return b;
		else return a;
	}
	else
		return a;
}

void dijkstra()
{
	//vector<int> q;
	queue<int> q;
	dist[1] = 0;
	q.push(1);
	
	while (!q.empty())
	{
		int cur = q.front();
		q.pop();
		vector<pair<int, int>>::iterator it;
		for (it = info.begin(); it != info.end(); it++)
		{
			int nw = dist[cur] + 1;
			if (it->first == cur) {
				if (dist[it->second] > nw) {
					dist[it->second] = nw;
					q.push(it->second);
				}
			}
		}
		//sort(&q.front(),&q.back(), cmp);
	}

	int maximum = 0, minimum = 0, cnt = 1;
	for (int i = 1; i <= N; i++)
	{
		if (dist[i] > maximum) {
			maximum = dist[i];
			minimum = i;
			cnt=1;
		}
		else if (dist[i] == maximum) {
			cnt++;
		}
	}
	cout << minimum << ' ' << dist[minimum] << ' '<< cnt << '\n';
}

int main()
{
	int A_i,B_i;
	cin >> N >> M;
	fill_n(dist, 20001, INF);
	for (int i = 0; i < M; i++) {
		cin >> A_i >> B_i;
		info.push_back({ A_i,B_i });
		info.push_back({ B_i,A_i });
	}
	sort(info.begin(),info.end());
	dijkstra();
	/*
	vector<pair<int, int>>::iterator it;
	for (it = info.begin(); it != info.end(); it++)
		cout << it->first << " " << it->second;
	*/
	return 0;
}