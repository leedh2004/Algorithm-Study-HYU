#include <iostream>
#include <string>

using namespace std;

int rev(int a)
{
    string tmp=to_string(a);
    string tmp2="";
    for(int i=tmp.length()-1;i>=0;i--) tmp2=tmp2+tmp[i];
    return stoi(tmp2);
}

int main()
{
    int a,b;
    cin>>a>>b;
    cout<<rev(rev(a)+rev(b));
    return 0;
}