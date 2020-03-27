#include <cstdio>

int main()
{
    int n,k,cost[11],ans=0;
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++) scanf("%d",&cost[i]);
    for(int i=n;i>0;i--){
        ans= ans+ (k/cost[i]);
        k=k-(k/cost[i])*cost[i];
        if(k==0) break;
    }
    printf("%d",ans);
    return 0;
}