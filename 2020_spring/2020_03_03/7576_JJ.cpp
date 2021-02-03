#include <iostream>
#include <queue>
#include <cstdio>

using namespace std;

bool visited[1001][1001];
int table[1001][1001];
int dir[4][2] = {{-1,0},{1,0},{0,1},{0,-1}};
int n,m;
queue<pair<int,int>> q;

bool is_in(int x,int y)
{
    return (0<x && x<=m && 0<y && y<=n);
}

int bfs()
{
    int days=-1;
    while (!q.empty())
    {
        int size = q.size();
        days++;
        for(int i=0;i<size;i++)
        {
            int now_x= q.front().first;
            int now_y= q.front().second;
            q.pop();
            for(int i=0;i<4;i++)
            {
                int next_x = now_x+dir[i][0];
                int next_y = now_y+dir[i][1];
                if(is_in(next_x,next_y)&& (!visited[next_x][next_y]) && table[next_x][next_y]==0)
                {
                    table[next_x][next_y]=1;
                    visited[next_x][next_y]=true;
                    q.push({next_x,next_y});
                }
            }
        }
    }
    return days;
}

int main()
{
    bool flag = false;
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++)
    {
        for(int j=1;j<=n;j++) 
        {
            scanf("%d",&table[i][j]);
            if(table[i][j]==1) {
                q.push({i,j});
                visited[i][j]=true;
            }
        }
    }
    int result = bfs();
    

    for(int i=1;i<=m;i++)
    {
        for(int j=1;j<=n;j++) 
        {
            if(table[i][j]==0) flag=true;
        }
    }
    printf("%d",flag?-1:result);
    return 0;
}