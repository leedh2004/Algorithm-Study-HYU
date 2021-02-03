#include <cstdio>
#include <iostream>

using namespace std;

int coin[101];
int dp[100001];
int k,n;

int main()
{
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++)  scanf("%d", &coin[i]);

    //cost를 기준으로한 dp
    for(int i=1;i<=n;i++)
    {
        dp[coin[i]]++;
        for(int j=1;j<=k;j++)
        {
            if((j-coin[i])>=0) dp[j]=dp[j]+dp[j-coin[i]];
        }
    }

    printf("%d\n",dp[k]);
    return 0;
}