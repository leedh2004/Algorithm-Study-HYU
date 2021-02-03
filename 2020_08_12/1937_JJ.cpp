#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int n;
int dp[501][501];
int daenamu[501][501];
int dir[4][2] = {{-1,0},{1,0},{0,1},{0,-1}};

vector <pair<int ,pair<int,int> > > v;


bool is_in(int x,int y){
    return 0<x && x<=n && 0<y && y<=n;
}

int lis(){
    int ans = 1;
    
    for(int i=0;i<v.size();i++){
        for(int k=0;k<4;k++){
            int nx = v[i].second.first + dir[k][0];
            int ny = v[i].second.second + dir[k][1];
            if(is_in(nx,ny)&& daenamu[nx][ny]>daenamu[v[i].second.first][v[i].second.second] && dp[nx][ny] < dp[ v[i].second.first][v[i].second.second] + 1){
                //printf("%d %d %d %d \n", i ,k,nx,ny);
                dp[nx][ny] = dp[v[i].second.first][v[i].second.second] + 1;
                ans = max(ans,dp[nx][ny]);
            }
        }
        
    }

    return ans;
}

int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            dp[i][j] = 1;
            scanf("%d",&daenamu[i][j]);
            v.push_back(make_pair(daenamu[i][j],make_pair(i,j)));
        }
    }
    sort(v.begin(),v.end());
    printf("%d\n",lis());
    return 0;
}