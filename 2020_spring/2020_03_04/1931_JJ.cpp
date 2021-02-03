#include <cstdio>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

typedef long long int ll;
vector<pair<ll,ll> > v;

int main()
{
    int n,e=0,ans=0;
    scanf("%d",&n);
    v.resize(n);
    for(int i=0;i<n;i++) scanf("%lld%lld",&v[i].first,&v[i].second);
    sort(v.begin(),v.end());
    for(int i=0;i<n;i++){
        if(v[i].first>=e){
            e=v[i].second;
            ans++;
        }
        else if(v[i].second<e) e=v[i].second;
    }
    printf("%d",ans);
    return 0;
}