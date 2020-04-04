#include <iostream>
#include <string>

using namespace std;

string a,b;
int ans=987654321;

int cal (int ans2_idx)
{
    int idx=ans2_idx;
    int count = 0;
    for(int i=0;i<a.length();i++)
    {
        if(b[idx]!=a[i]) count++;
        idx++;
    }
    return count;
}

int main()
{
    cin>>a>>b;
    if(a.length()==b.length()){
        printf("%d",cal(0));
        return 0;
    }
    for(int i=0;i<=(b.length()-a.length());i++) ans=min(ans,cal(i));
    printf("%d",ans);
    return 0;
}