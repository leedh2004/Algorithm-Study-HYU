#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str;
    cin>>str;
    long long int num=stoi(str);
    long long int ans =0;
    long long int tmp = 9;
    long long int now = 9;
    for(int i=1;i<=str.length();i++){
        if(now<=num) ans += tmp*i;
        else{
            now = now-tmp;
            ans += (num - now)*i;
            break;
        }
        tmp=tmp*10;
        now=now+tmp;
    }
    cout<<ans;
    return 0;
}