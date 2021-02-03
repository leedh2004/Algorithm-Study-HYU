#include <cstdio>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <cstring>

using namespace std;

int n;
int table[11][11];
int cost[11][11];
int ans=999999;

//    x,y - 기존의 꽃   |   a,b - 새로 심을 꽃
bool is_dead(int x, int y, int a, int b){

    //거리가 가까운경우
    if(abs(x-a) + abs(b-y) <=2 ) return true;

    //심는게 가능한경우
    return false;
}

//값 구하기
int get_cost(int x, int y){
    if(cost[x][y]!=0) return cost[x][y];
    int ret = 0;
    int dir[5][2] = {{0,0},{-1,0},{1,0},{0,1},{0,-1}};
    for(int i=0;i<5;i++){
        int nx = x + dir[i][0];
        int ny = y + dir[i][1];
        ret = ret + table[nx][ny];
    }
    return cost[x][y] = ret;
}

int main(){

    //입력
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&table[i][j]);
        }
    }

    //첫번째꽃
    for(int i=1;i<n-1;i++){
        for(int j=1;j<n-1;j++){

            //두번째꽃
            for(int k=1;k<n-1;k++){
                for(int l=1;l<n-1;l++){
                    
                    //세번째꽃
                    for(int m=1;m<n-1;m++){
                        for(int o=1;o<n-1;o++){
                            
                            if(!is_dead(i,j,k,l) && !is_dead(i,j,m,o) && !is_dead(k,l,m,o)){
                                ans = min(ans,get_cost(i,j)+get_cost(k,l)+get_cost(m,o));
                            }
                    
                        }
                    }
                }
            }
        }
    }

    printf("%d\n",ans);
    return 0;
}