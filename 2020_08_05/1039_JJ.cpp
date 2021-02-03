#include <iostream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int k,sz;
int ans = 0;
string n;
int dp[1000001][11];

string change(string num,int i,int j){
    char tmp;
    //swap
    tmp = num[i]; num[i] = num[j]; num[j] = tmp;
    return num;
}


int dfs(string num, int t){

    //최적의 발견
    if(t==k)return stoi(num);
    
    //메모제이션 활용
    if(dp[stoi(num)][t]!=-1) return dp[stoi(num)][t];

    //모든 경우 탐색
    for(int i=1;i<sz;i++){
        for(int j=0;j<i;j++){
            
            //바꿨을 때 0으로 시작하는 경우
            if(num[i]=='0'&&j==0) continue;
            string new_num = change(num,i,j);
            dp[stoi(num)][t] = max(dp[stoi(num)][t],dfs(new_num,t+1));
        }
    }
    return dp[stoi(num)][t];
}


int main(){

    //입력
    cin>>n>>k;
    sz = n.size();

    //초기화
    memset(dp,-1,sizeof(dp));

    //교환할수없는 조건 - 1자리 or 2자리인데 0포함
    if(sz==1 || (sz==2 && (n[0]=='0' || n[1]=='0'))){
        cout<<"-1\n";
        return 0;
    }
    cout<<dfs(n,0)<<"\n";
    return 0;
}
