#include <cstdio>
#include <queue>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

int dist[10001];
vector<pair<int,int> > adj[10001];
int n,d,c;

void Dijkstra(){

    //초기화
    priority_queue<pair<int,int> > pq;  
    for(int i=1;i<=n;i++) dist[i] = 987654321;
    dist[c] = 0;

    //pq
    pq.push(make_pair(0,c));
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
    int t; scanf("%d",&t);
    int st,ed,cost;
    while (t--)
    {
        scanf("%d%d%d",&n,&d,&c);
        while (d--)
        {
            //의존관계
            scanf("%d%d%d",&ed,&st,&cost);
            adj[st].push_back(make_pair(cost,ed));
        }
        Dijkstra();

        //출력
        int ans1=0,ans2=0;
        for(int i=1;i<=n;i++){
            //도달가능할 때
            if(dist[i]!=987654321){
                ans1++;
                ans2 = max(ans2,dist[i]);
            }
        }
        printf("%d %d\n",ans1,ans2);
        for(int i=1;i<=n;i++){
            adj[i].clear();
        }
    }
    return 0;
}