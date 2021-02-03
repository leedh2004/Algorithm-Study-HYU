#include <iostream>
#include <cstdio>

using namespace std;

int n;
int dp[21];

int dp_recursive(int num)
{
    if(dp[num]!=0) return dp[num];
    return dp[num]=dp_recursive(num-1)*2+1;
}


void print_recursive(int num,int before,int after)
{
    if(num==1) {
        printf("%d %d\n",before,after);
        return ;
    }
    int mid=6-before-after;
    print_recursive(num-1,before,mid);
    printf("%d %d\n",before,after);
    print_recursive(num-1,mid,after);
    return ;
}

int main()
{
    scanf("%d",&n);
    dp[1]=1;
    printf("%d\n",dp_recursive(n));
    print_recursive(n,1,3);
    return 0;
}