#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int n;
int adj[101][101];
int ans[101][101];
vector<pair<int,int>> v;

void dfs(int x,int y)
{
   ans[x][y]=1;
   for(int i=1;i<=n;i++)
   {
       if(adj[y][i]&& (!ans[x][i])) dfs(x,i);
   }
   return ;
}

int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++) scanf("%d",&adj[i][j]);
    }

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++) 
        {
            if(adj[i][j]==1) dfs(i,j);
        }
    }
     for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++) 
        {
            printf("%d ",ans[i][j]);
        }
        printf("\n");
    }
    return 0;
}