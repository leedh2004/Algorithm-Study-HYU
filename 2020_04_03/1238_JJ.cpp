#include <iostream>
#include <cstdio>

using namespace std;

int dist[1001][1001];

int main()
{
    int n,m,x; 
    scanf("%d%d%d",&n,&m,&x);
    
    //초기화
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++) dist[i][j]=987654321;
    }

    int st,ed,cost;
    while(m--)
    {
        scanf("%d%d%d",&st,&ed,&cost);
        dist[st][ed]=cost;
    }

    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            for(int k=1;k<=n;k++)
            {
                if(dist[j][i]+dist[i][k]<dist[j][k]) dist[j][k]=dist[j][i]+dist[i][k];
            }
        }
    }

    int ans=0;
    for(int i=1;i<=n;i++)
    {
        if(i==x) continue;
        ans = max(ans,dist[i][x]+dist[x][i]);
    }
    printf("%d\n",ans);
    return 0;
}