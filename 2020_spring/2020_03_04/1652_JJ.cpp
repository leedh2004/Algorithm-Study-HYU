#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;

int n,ans1,ans2;
string tmp;
vector <int> v[101];
vector <int> vv[101];

void solve()
{
    for(int i=1;i<=n;i++)
    {
        if(v[i].size()==0) 
        {
            ans1++;
            continue;
        }
        //양옆
        if( (v[i][0]-1) >= 2) ans1++;
        if( (n-v[i][v[i].size()-1]) >= 2 ) ans1++;
        for(int j=0;j<v[i].size()-1;j++)
        {
            if(v[i][j+1]-v[i][j]>=3) ans1++;
        }
    }
    for(int i=1;i<=n;i++)
    {
        if(vv[i].size()==0) 
        {
            ans2++;
            continue;
        }
        //양옆
        if( vv[i][0] >= 3) ans2++;
        if( (n-vv[i][vv[i].size()-1]) >= 2 ) ans2++;
        for(int j=0;j<vv[i].size()-1;j++)
        {
            if(vv[i][j+1]-vv[i][j]>=3) ans2++;
        }
    }
}

int main()
{
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>tmp;
        for(int j=0;j<n;j++)
        {
            if(tmp[j]=='X') 
            {
                v[i].push_back(j+1);
                vv[j+1].push_back(i);
            }
        }
    }
    if(n==1) 
    {
        cout<<"0 0";
        return 0;
    }
    solve();
    printf("%d %d",ans1,ans2);
    return 0;
}