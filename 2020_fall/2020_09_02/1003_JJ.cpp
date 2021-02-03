#include <cstdio>
#include <vector>

using namespace std;

typedef long long int ll;

vector<pair<ll,ll> > dp;

int main(){

    // 값을 미리 구해놓는다.
    dp.resize(41);
    dp[0].first = 1;
    dp[1].second = 1;
    for(int i=2;i<=40;i++){
        dp[i].first = dp[i-2].first + dp[i-1].first;
        dp[i].second = dp[i-2].second + dp[i-1].second;
    }

    //입력
    int t; scanf("%d",&t);
    while (t--)
    {
        int n; scanf("%d",&n);
        printf("%lld %lld\n",dp[n].first,dp[n].second);
    }
    return 0;
}