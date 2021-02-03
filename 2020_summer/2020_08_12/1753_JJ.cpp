#include <cstdio>
#include <queue>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int dist[20001];
vector<pair<int,int> > adj[20001];
int v,e,start_node;

void Dijkstra(){

    //초기화
    priority_queue<pair<int,int> > pq;  
    for(int i=1;i<=v;i++) dist[i] = 987654321;
    dist[start_node] = 0;

    //pq
    pq.push(make_pair(0,start_node));
    while (!pq.empty())
    {
        int cost = -pq.top().first;
        int now = pq.top().second;
        pq.pop();
        for(int i=0;i<adj[now].size();i++){
            int next = adj[now][i].second;
            int n_cost = cost + adj[now][i].first;
            if(n_cost<dist[next]){
                dist[next] = n_cost;
                pq.push(make_pair(-n_cost,next));
            }
        }
    }
}

int main(){
    scanf("%d%d%d",&v,&e,&start_node);
    int st,ed,cost;
    for(int i=0;i<e;i++)
    {
        //연결관계
        scanf("%d%d%d",&st,&ed,&cost);
        adj[st].push_back(make_pair(cost,ed));
    }
    Dijkstra();

   

    //출력
    for(int i=1;i<=v;i++){
        //도달가능할 때
        if(dist[i]!=987654321) printf("%d\n",dist[i]);
        else printf("INF\n");
    }
      
    return 0;
}