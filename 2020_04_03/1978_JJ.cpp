#include <cstdio>
#include <cmath>
#include <cstring>


bool sosu[1001];

void make_sosu()
{
    sosu[1]=false;
    for(int i=2;i<=sqrt(1000);i++)
    {
        for(int j=2;i*j<=1000;j++)
        {
            sosu[i*j]=false;
        }
    }
}


int main()
{
    memset(sosu,true,sizeof(sosu));
    make_sosu();
    int n;scanf("%d",&n);
    int now,ans=0;
    for(int i=0;i<n;i++)
    {
        scanf("%d",&now);
        if(sosu[now]) ans++;
    }
    printf("%d\n",ans);
    return 0;
}