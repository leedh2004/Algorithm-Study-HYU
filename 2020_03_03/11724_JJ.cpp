#include <cstdio>
#include <vector>

using namespace std;

vector<int> adj[1001];
bool visited[1001];
int n,m;

void dfs(int node)
{
    visited[node]=true;
    for(int i=0;i<adj[node].size();i++)
    {
        if(!visited[adj[node][i]]) dfs(adj[node][i]);
    }
    return ;
}

int main()
{
    int s,e,ans=0;
    scanf("%d%d",&n,&m);
    while(m--)
    {
        scanf("%d%d",&s,&e);
        adj[s].push_back(e);
        adj[e].push_back(s);
    }
    for(int i=1;i<=n;i++)
    {
        if(!visited[i])
        {
            dfs(i);
            ans++;
        }
    }
    printf("%d",ans);
    return 0;
}