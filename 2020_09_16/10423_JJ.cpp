#include <cstdio>
#include <queue>

using namespace std;

typedef long long int ll;

int n,m,k;
int p[1001];
bool on[1001];
priority_queue<pair<int,pair<int,int> > > edges;

int get_p(int x){
    if(p[x]==x) return x;
    return p[x] = get_p(p[x]);
}

bool is_on(int x){
    int px = get_p(x);
    return on[px];
}

bool merge(int a, int b){

    // 이거 때문에 삽질했네
    if(a==b) return false;

    bool a_on = is_on(a);
    bool b_on = is_on(b);

    //둘다 이미 전기가 들어와 있다면
    if(a_on&&b_on) return false;

    //합치기
    int pa = get_p(a);
    int pb = get_p(b);

    p[pa] = pb;

    //하나라도 전기 들어와있다면 
    if(a_on || b_on){
        on[pa] = true;
        on[pb] = true;
    }
    return true;
}

int main(){

    //입력
    int tmp,st,ed,cost;
    scanf("%d %d %d",&n,&m,&k);
    for (int i = 0; i < k; i++){
        scanf("%d",&tmp);
        on[tmp] = true;
    }

    //우선순위큐
    while (m--){
        scanf("%d %d %d",&st,&ed,&cost);
        edges.push(make_pair(-cost,make_pair(st,ed)));
    }

    //유니온 파인드 세팅
    for(int i=1;i<=n;i++) p[i] = i;

    int num_edge = 0;
    ll ans = 0;

    //연결된 엣지가 n - k 일때 전부 연결된다.
    while(num_edge!=n-k){
        //printf("%d\n",num_edge);
        if(merge( edges.top().second.first, edges.top().second.second) ){
            num_edge++;
            ans = ans - edges.top().first;
        }
        edges.pop();
    }
    
    printf("%lld\n",ans);
    
    return 0;
}
