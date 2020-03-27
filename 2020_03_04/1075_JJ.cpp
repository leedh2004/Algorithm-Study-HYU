#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n,k,f;cin>>n>>f;
    string ans;
    n=(n/100)*100;
    k=(n/f)*f;
    if(n!=k) k=k+f;
    ans=to_string(k);
    cout<<ans[ans.length()-2]<<ans[ans.length()-1];
    return 0;
}