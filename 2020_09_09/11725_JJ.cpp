#include <cstdio>
#include <vector>

using namespace std;

int n;
vector<int> adj[100001];
int p[100001];
bool visited[100001];

void dfs(int st){
    
    visited[st] = true;

    //인접애들조사
    for(int i=0;i<adj[st].size();i++){

        //방문안한노드 -> 하위노드
        if(!visited[adj[st][i]]){
            p[adj[st][i]] = st;
            dfs(adj[st][i]);
        }
    }

}


int main(){
    int tmp1,tmp2;
    scanf("%d",&n);
    for(int i=1;i<n;i++){
        scanf("%d %d",&tmp1,&tmp2);
        adj[tmp1].push_back(tmp2);
        adj[tmp2].push_back(tmp1);
    }
    dfs(1);

    for(int i=2;i<=n;i++) printf("%d\n",p[i]);

    return 0;
}