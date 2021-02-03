#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <queue>

using namespace std;

void dfs(int start,vector<int>graph[],bool check[])
{
    printf("%d ",start);
    check[start] = true;
    for(int i=0;i<graph[start].size();i++)
    {
        if(check[graph[start][i]]==false) dfs(graph[start][i],graph,check);
    }
}

void bfs(int start,vector<int>graph[],bool check[])
{
    queue<int> q;
    q.push(start);
    check[start]=true;
    while(!q.empty())
    {
        int tmp = q.size();
        for(int i=0;i<tmp;i++)
        {
            int now;
            now=q.front();
            q.pop();
            printf("%d ",now);
            for(int j=0;j<graph[now].size();j++)
            {
                if(check[graph[now][j]]==false)
                {
                    q.push(graph[now][j]);
                    check[graph[now][j]]=true;
                }
            }
        }
    }
}

int main()
{
    int n,m,start;
    cin>>n>>m>>start;
    vector<int>graph[n+1];
    bool check[n+1];
    bool ck[n+1];
    fill_n(check,n+1,false);
    fill_n(ck,n+1,false);
    for(int i=0;i<m;i++)
    {
        int a,b;
        cin>>a>>b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    for(int j=1;j<=n;j++) sort(graph[j].begin(),graph[j].end());
    dfs(start,graph,check);
    printf("\n");
    bfs(start,graph,ck);
}