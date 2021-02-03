#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> v;

int main()
{
    string n;cin>>n;
    int total = 0;
    for(int i=0;i<n.length();i++) {
        v.push_back(n[i]-'0');
        total=total +(n[i]-'0');
    }
    sort(v.begin(),v.end());
    if(v[0]==0 && total%3==0)
    {
        for(int i=v.size()-1;i>=0;i--) cout<<v[i];
    }
    else
    {
        cout<<"-1";
    }
    return 0;
}