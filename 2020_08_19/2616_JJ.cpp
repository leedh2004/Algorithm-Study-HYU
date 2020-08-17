#include <cstdio>
#include <algorithm>

using namespace  std;

int n,m;

//기관차 갯수, 구간 종료 index
int dp[4][50001];

//구간합
int sum[50001];

//용량
int capacity[50001];

int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%d",&capacity[i]);
        sum[i] = sum[i-1] + capacity[i];
    }
    scanf("%d",&m);

    //기관차는 3개
    for(int i=1;i<=3;i++){
        //각 구간
        for(int j=m;j<=n;j++){
            //j부터 m개 칸의 구간합
            int cost = sum[j] - sum[j-m];
            dp[i][j] = max(dp[i][j],max(dp[i-1][j-m]+cost,dp[i][j-1]));
        }
    }
    printf("%d\n",dp[3][n]);
    return 0;
}