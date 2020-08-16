#include <iostream>
#include <algorithm>

using namespace std;

int n;
int ans=0;
pair<int,int> p[16];

void dfs(int today , int cost){
    //오늘부터 쭉 돈다.
    for(int i=today ; i<=n;i++) {
        //퇴사전까지 일할수 있는 경우
        if(i+p[i].first <= n +1) {
            //시작날과 cost바꿔서 다시 탐색
            dfs(i+p[i].first,cost+p[i].second);
            ans = max(ans,cost+p[i].second);
        }
    }
}


int main()
{
    cin>>n;
    //p에는 걸리는 날짜과,각각의 금액이 들어간다. 
    for(int i=1;i<=n;i++) cin>>p[i].first>>p[i].second;
    //완전탐색
    dfs(1,0);
    cout<<ans<<'\n';
    return 0;
}