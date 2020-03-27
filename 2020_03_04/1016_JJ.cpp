#include <cstdio>
#include <vector>

using namespace  std;

typedef long long int ll;
bool ck[1000001];
ll m,M,total,cnt=0;


int main()
{
    scanf("%lld%lld",&m,&M);
    for(ll i=2;i*i<=M;i++)
    {
        ll tmp=i*i; 
        for(ll j=(m-1)/tmp;(j*tmp)<=M;j++)
        {
            if( j*tmp<m || j*tmp>M) continue;
            if(!ck[j*tmp-m])
            {
                ck[j*tmp-m]=true;
                cnt++;
            }
        }
    }
    printf("%lld",M-m+1-cnt);
    return 0;
}