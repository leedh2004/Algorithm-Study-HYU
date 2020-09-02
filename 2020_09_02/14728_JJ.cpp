#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;


int n,t;
int dp[10001];
int Time[1001];
int point[1001];


int main(){

    //입력
    scanf("%d%d",&n,&t);
    for(int i=1;i<=n;i++){
        scanf("%d%d",&Time[i],&point[i]);
    }

    for(int i=1;i<=n;i++){
        for(int j=t;j>=Time[i];j--) dp[j] = max(dp[j],dp[j-Time[i]]+point[i]);
    }

    printf("%d\n",dp[t]);
    return 0;
}