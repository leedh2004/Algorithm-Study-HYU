#include <cstdio>
#include <iostream>

using namespace std;

int dp[100001];

int main()
{
    int n;scanf("%d",&n);

    //n:i
    for(int i=1;i<=n;i++)
    {
        //j:제곱수
        for(int j=1;j*j<=i;j++)
        {
            if( ((i-j*j)>=0) )
            {
                dp[i] = dp[i]?(min(dp[i],dp[i-j*j]+1)):dp[i-j*j]+1;
            }
        }
    }
    printf("%d\n",dp[n]);
    return 0;
}