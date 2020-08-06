/*
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

int n,m;
//int dp[101][101];
int dir[4][2] = {{-1,0},{1,0},{0,1},{0,-1}};
bool visited[101][101];
int map[101][101];
int ans = 999999;

bool is_in(int x,int y){
    return 0<x && x<=m && 0<y && y<=n;  
}

void dfs(int x, int y,bool visited[101][101], int now){
    if(x==m && y==n) ans = min(ans,now);
    visited[x][y] = true;
    bool now_visited[101][101];
    memcpy(now_visited,visited,sizeof(now_visited));

    for(int i=0;i<4;i++){
        int nx = x + dir[i][0];
        int ny = y + dir[i][1];
        if(!visited[nx][ny] && is_in(nx,ny)) {
            if(map[nx][ny]==1) dfs(nx,ny,now_visited,now+1);
            else dfs(nx,ny,now_visited,now);
        }
    }
}

int main()
{
    //memset(dp,-1,sizeof(dp));
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++){
        for(int j=1;j<=n;j++) scanf("%1d",&map[i][j]);
    }
    dfs(1,1,visited,0);
    printf("%d\n",ans);
    return 0;
}
*/

#include <cstdio>
#include <queue>

using namespace std;

int n,m;
int dist[101][101];
int map[101][101];
int dir[4][2] = {{-1,0},{1,0},{0,1},{0,-1}};


bool is_in(int x,int y){
    return 0<x && x<=m && 0<y && y<=n;  
}

void Dijkstra(){
    priority_queue<pair<int,pair<int,int> > > pq;
    dist[1][1] = 0;
    pq.push(make_pair(0,make_pair(1,1)));
    while (!pq.empty())
    {
        //음수로 넣었기 때문에 - 처리
        int cost = -pq.top().first;

        //현재 좌표
        int now_x = pq.top().second.first;
        int now_y = pq.top().second.second;
        pq.pop();
        for(int i=0;i<4;i++){
            int next_x = now_x + dir[i][0];
            int next_y = now_y + dir[i][1];
            if(is_in(next_x,next_y) && dist[next_x][next_y] > dist[now_x][now_y] + map[next_x][next_y]){
                dist[next_x][next_y] = dist[now_x][now_y] + map[next_x][next_y];
                pq.push(make_pair(-dist[next_x][next_y],make_pair(next_x,next_y)));
            }
        }
    }
}

int main()
{
    scanf("%d%d",&n,&m);
    for(int i=1;i<=m;i++){
        for(int j=1;j<=n;j++) {
            scanf("%1d",&map[i][j]);
            //초기값
            dist[i][j] = 987654321;
        }
    }
    Dijkstra();
    printf("%d\n",dist[m][n]);
    return 0;
}