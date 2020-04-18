#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


vector<string> str;

bool compare(string a, string b)
{
    if(a.length()!=b.length()) return a.length()<b.length();
    int na=0;
    int nb=0;
    for(int i=0;i<a.length();i++)
    {
        if( 0<a[i]-'0'&& a[i]-'0'<10) na+=a[i]-'0';
        if( 0<b[i]-'0'&& b[i]-'0'<10) nb+=b[i]-'0';
    }
    if(na!=nb)return na<nb;
    return a<b;
}


int main()
{
    int n;scanf("%d",&n);
    str.resize(n);
    for(int i=0;i<n;i++) cin>>str[i];
    sort(str.begin(),str.end(),compare);
    for(int i=0;i<n;i++) cout<<str[i]<<"\n";
    return 0;
}
