#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int n,tmp=0,ans=0;
vector<int> cost;

int main()
{
    scanf("%d",&n);
    cost.resize(n);
    for(int i=0;i<n;i++) scanf("%d",&cost[i]);
    sort(cost.begin(),cost.end());
    for(int i=0;i<n;i++){
        tmp=tmp+cost[i];
        ans=ans+tmp;
    }
    printf("%d",ans);
    return 0;
}