#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>

using namespace std;

int n,m;
bool visited[2001];
vector<int> adj[2001];
bool ans = false;

void dfs(int node, int depth){

    // printf("node : %d depth : %d \n",node,depth);

    visited[node] = true;

    if(depth==4) {
        ans = true;
        return;
    }

    for(int i=0;i<adj[node].size();i++) {
        if(!visited[adj[node][i]]){
            dfs(adj[node][i],depth+1);
            visited[adj[node][i]] = false;
        } 
    }
}

int main(){

    scanf("%d%d",&n,&m);

    //인접리스트
    int tmp1,tmp2;
    while (m--){
        scanf("%d%d",&tmp1,&tmp2);
        adj[tmp1].push_back(tmp2);
        adj[tmp2].push_back(tmp1);
    }

    //dfs
    for(int i=0;i<n;i++){
        dfs(i,0);
        memset(visited,false,sizeof(visited));
        // printf("----\n");

        if(ans) break;
    }
    
    
    printf("%d\n",ans?1:0);

    return 0;

}

/*

int n,m;
int dist[2001][2001];
int INF = -10000;

void Floyd_Warshall(){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            for(int k=0;k<n;k++){

                //사이클제거
                if(j==k ||j==i ||i==k) continue;

                if(dist[j][i]+dist[i][k] > dist[j][k]) dist[j][k] = dist[j][i]+dist[i][k];
            }
        }
    }
}


int main(){

    scanf("%d%d",&n,&m);

    //초기값
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++) dist[i][j] = INF;
    }
    for(int i=0;i<n;i++) dist[i][i] = 0;
    

    //연결 - 거리는 1로 설정 --> 거리가 5인애가 있으면 관계 존재
    int tmp1,tmp2;
    while (m--){
        scanf("%d%d",&tmp1,&tmp2);
        dist[tmp1][tmp2] = 1;
        dist[tmp2][tmp1] = 1;
    }

    Floyd_Warshall();

    bool ans = false;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++) {
            if(dist[i][j]!= INF &&dist[i][j]>=4) {
                ans = true;
                break;
            }
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++) printf("%d ",dist[i][j]);
        printf("\n");
    }

    printf("%d\n",ans?1:0);

    return 0;
}
*/