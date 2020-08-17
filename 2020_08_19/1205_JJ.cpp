#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

typedef long long int ll;

int n,p;
ll ns;
vector<ll> v;


int main(){
    scanf("%d%lld%d",&n,&ns,&p);
    v.resize(p+1);
    v[0] = -2000000001;
    for(int i=1;i<=n;i++){
        scanf("%lld",&v[i]);
        v[i] = -v[i];
    }
    
    sort(v.begin(),v.end());


    for(int i=1;i<=p;i++){
        if( i>n || ns> -v[i] ||(ns == -v[i] && (ns > -v[n]|| (ns == -v[n] && p>n) ))) {
            printf("%d\n",i);
            return 0;
        }
        if(i>n) break;
    }
    printf("-1\n");
    return 0;
}