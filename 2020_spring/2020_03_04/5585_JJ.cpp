#include <iostream>

using namespace std;

int m[6]={500,100,50,10,5,1};

int main()
{
    int cost,ans=0;cin>>cost;cost=1000-cost;
    for(int i=0;i<6;i++)
    {
        ans=ans+(cost/m[i]);
        cost=cost-(cost/m[i])*m[i];
        if(cost==0) break;
    }
    printf("%d",ans);
    return 0;
}