#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

int n,s,m,val;
bool check[101][1001];

int main(){

    //입력
    cin>>n>>s>>m;
    memset(check,false,sizeof(check));
    check[0][s]=true;
    bool flag =false;

    for(int i=1;i<=n;i++){
        cin>>val;
        flag=false;

        //예전에 이렇게 짰지만, 모든 배열을 보지않고 bfs로 돌면 더 좋았을 것같음.
        for(int j=0;j<=m;j++){
            //해당곡 연주가능할때
            if(check[i-1][j]==true){
                if(m>=j+val){
                    flag=true;
                    check[i][j+val] =true;
                }
                if(0<=j-val){
                    flag=true;
                    check[i][j-val] =true;
                }
            }
        }
        if(!flag) {
            cout<<"-1";
            return 0;
        }
    }
    for(int i=m;i>=0;i--){
        //거꾸로 오면서 최대값 출력 및 종료
        if(check[n][i]==true){
            cout<<i;
            return 0;
        }
    }
    return 0;
}