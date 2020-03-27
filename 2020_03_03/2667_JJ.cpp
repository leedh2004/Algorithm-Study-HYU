#include <iostream>
#include <queue>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

bool visited[26][26];
int table[26][26];
int dir[4][2] = {{-1,0},{1,0},{0,1},{0,-1}};
int n;
vector<int> ans;
queue<pair<int,int>> q;

bool is_in(int x,int y)
{
    return (0<x && x<=n && 0<y && y<=n);
}

int bfs(int x,int y)
{
    //printf("%d%d\n",x,y);
    int size = 1;
    while (!q.empty())q.pop();
    q.push({x,y});
    visited[x][y]=true;
    while (!q.empty())
    {
        int now_x= q.front().first;
        int now_y= q.front().second;
        q.pop();
        for(int i=0;i<4;i++)
        {
            int next_x = now_x+dir[i][0];
            int next_y = now_y+dir[i][1];
            if(is_in(next_x,next_y)&& (!visited[next_x][next_y]) && table[next_x][next_y])
            {
                size++;
                visited[next_x][next_y]=true;
                q.push({next_x,next_y});
            }
        }
    }
    return size;
}

int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++) scanf("%1d",&table[i][j]);
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++) 
        {
            if( !visited[i][j] && table[i][j])
            {
                ans.push_back(bfs(i,j));
            }
        }
    }
    sort(ans.begin(),ans.end());
    printf("%d\n",ans.size());
    for(int i=0;i<ans.size();i++) printf("%d\n",ans[i]);
    return 0;
}