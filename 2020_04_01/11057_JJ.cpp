#include <iostream>
#include <cstdio>

using namespace std;

int dp[1001][10][10];
int m=10007;


int recur(int len,int s, int e)
{
    if(len==0 || s==e) return 1;
    if(len==1) return e-s+1;
    if(dp[len][s][e]!=0) return dp[len][s][e];
    int now=0;
    for(int i=s;i<=e;i++)
    {
        for(int j=i;j<=e;j++)
        {
            now =(now + recur(len-2,i,j)%m)%m;
        }
    }
    return dp[len][s][e]=now;
}

int main()
{
    int n;scanf("%d",&n);
    printf("%d",recur(n,0,9));
    return 0;
}
