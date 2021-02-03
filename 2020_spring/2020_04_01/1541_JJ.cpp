#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> v;
vector<char> oper;


int main()
{
    string s;cin>>s;
    char now_sybol = '+';
    int now_idx = 0;
    int end_idx = 0;
    int first_minus_idx;
    int flag = false;
    int count = 0;
    for(int i=0;i<s.size();i++)
    {
       if(s[i]!='+'&&s[i]!='-') 
       {
           end_idx++;
           continue;
       }
       else
       {
           count++;
           v.push_back( stoi(s.substr(now_idx,end_idx) ) );
           if(s[i]=='-' && !flag) 
           {
               flag=true;
               first_minus_idx = count;
           }
           now_idx=i+1;
           end_idx=1;
       }
    }
    v.push_back( stoi(s.substr(now_idx,end_idx) ) );
    //for(int i=0;i<v.size();i++) cout<<v[i]<<" ";

    int sum = v[0];
    for(int i=1;i<v.size();i++)
    {
        if(flag&& first_minus_idx<=i ) sum-=v[i];
        else sum+=v[i];
    }
    printf("%d\n",sum);
    return 0;
}