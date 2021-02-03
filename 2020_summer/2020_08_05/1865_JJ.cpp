#include <cstdio>
#include <queue>
#include <vector>
#include <climits>

using namespace std;

int n,m,w;
long long int dist[502];
bool flag=false;

struct edge
{
    int s;
    int e;
    int c;

    edge(int st,int ed,int cost) : s(st),e(ed),c(cost){};
};

vector<edge> v;

void initailizing(){
    for(int i=1;i<=n;i++) dist[i]=0;
    v.clear();
    flag = false;
}

void solv(){
    dist[1]=0;
    //최소거리 찾기
    for(int i=1;i<=n;i++)
    {
       for(int j=0;j<v.size();j++)
       {

           if(dist[v[j].s]+v[j].c<dist[v[j].e]) {
               //사이클찾기
               if(i==n) flag = true;

               //갱신
               dist[v[j].e]=dist[v[j].s]+v[j].c;
           }
       }
    }
    printf("%s\n",flag?"YES":"NO");  
}

int main()
{
    int t,a,b,c;
    scanf("%d\n",&t);
    while (t--){
        initailizing();
        scanf("%d%d%d",&n,&m,&w);
        for(int i=0;i<m;i++){
            scanf("%d%d%d",&a,&b,&c);
            edge tmp1(a,b,c);
            edge tmp2(b,a,c);
            v.push_back(tmp1);
            v.push_back(tmp2);
        }
        for(int i=0;i<w;i++){
            scanf("%d%d%d",&a,&b,&c);
            edge tmp3(a,b,-c);
            v.push_back(tmp3);
        }
        solv();
    }
    return 0;
}
