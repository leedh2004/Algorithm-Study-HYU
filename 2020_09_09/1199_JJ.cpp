#include <cstdio>
#include <vector>

using namespace std;

int n;
int adj[1001][1001];
int degree[1001];

void dfs(int node){


    for(int i=1;i<=n;i++){

        //연결되어있으면서 차수가 1이상인 경우
        if(adj[node][i]){
            adj[node][i]--;
            adj[i][node]--;
            dfs(i);
        }
    }

    //현재노드출력
    printf("%d ",node);
}

int main(){

    //입력
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            scanf("%d",&adj[i][j]);
            degree[i] = degree[i] + adj[i][j];
        }
    }

    //오일러 회로가 있는지 조사
    bool flag = true;
    for(int i=1;i<=n;i++){
        if(degree[i]%2) flag = false;
    }

    //못만드는경우
    if(!flag) {
        printf("-1\n");
        return 0;
    }

    dfs(1);
    printf("\n");
    
    return 0;
}