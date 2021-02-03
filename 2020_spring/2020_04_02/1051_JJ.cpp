#include <cstdio>
#include <iostream>

using namespace std;

int table[51][51];
int n,m;
int ans = 1;

bool is_in(int x, int y)
{
    return (0<x && x<=n)&&(0<y && y<=m);
}

int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++) scanf("%1d",&table[i][j]);
    }

    //size
    for(int i=1;i<=min(n,m);i++)
    {
        for(int j=1;j<=n;j++)
        {
            for(int k=1;k<=m;k++)
            {
                if(is_in(j+i,k+i))
                {
                    if( (table[j][k]==table[j+i][k])&&(table[j][k+i]==table[j+i][k+i])&& (table[j][k+i]==table[j+i][k])) ans=max(ans,(i+1)*(i+1));
                }
            }
        }  
    }
    printf("%d\n",ans);
    return 0;
}