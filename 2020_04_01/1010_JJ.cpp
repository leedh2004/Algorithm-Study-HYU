#include <iostream>
#include <cstdio>

typedef long long int ll;

using namespace std;

ll dp[31][31];

void pascal_traingle()
{
    dp[0][0]=1;
    for(int i=1;i<=30;i++)
    {
        dp[i][0]=1;
        dp[i][i]=1;
        for(int j=1;j<i;j++)
        {
            dp[i][j]=dp[i-1][j]+dp[i-1][j-1];
        }
    }
}


int main()
{
    int t; scanf("%d",&t);
    int n,m;
    pascal_traingle();
    while (t--)
    {
        scanf("%d%d",&n,&m);
        printf("%lld\n",dp[m][n]);
    }
    return 0;
}