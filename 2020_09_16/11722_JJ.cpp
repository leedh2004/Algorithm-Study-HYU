#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int n;
int arr[1001];
int dp[1001];
int ans = 0;

void solve(){
    for(int i=1;i<=n;i++){
        for(int j=1;j<i;j++){
            if(arr[i] < arr[j]) {
                dp[i] = max(dp[i],dp[j]+1);
                ans = max(ans,dp[i]);
            }
        }
    }
}

int main(){

    //입력
    scanf("%d",&n);
    for(int i=1;i<=n;i++) scanf("%d",&arr[i]);
    
    solve();
    printf("%d\n",ans+1);

    return 0;
}