#include <iostream> 

using namespace std;
typedef long long int ll;
ll n,m;
int five,two;

int func_5(ll num)
{
    ll tmp=1;
    int cnt=0;
    for(int i=1;i<14;i++)
    {
        tmp=tmp*5;
        if(tmp>tmp) break;
        cnt=cnt+num/tmp;
    }
    return cnt;
}

int func_2(ll num)
{
    ll tmp=1;
    int cnt=0;
    for(int i=1;i<31;i++)
    {
        tmp=tmp*2;
        if(tmp>tmp) break;
        cnt=cnt+num/tmp;
    }
    return cnt;
}


int main()
{
    cin>>n>>m;
    five=func_5(n)-func_5(m)-func_5(n-m);
    two=func_2(n)-func_2(m)-func_2(n-m);
    cout<<min(five,two);
    return 0;
}