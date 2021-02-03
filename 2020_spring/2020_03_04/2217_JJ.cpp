#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> v;

int main()
{
    int n,ans=0;
    
    scanf("%d",&n);
    v.resize(n);

    for(int i=0;i<n;i++)
    {
        scanf("%d",&v[i]);
        v[i]=-v[i];
    }

    sort(v.begin(),v.end());

    for(int i=0;i<n;i++) ans=max(ans,-v[i]*(i+1));
    
    printf("%d",ans);
    return 0;
}