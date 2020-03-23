#include <cstdio>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int N,K,now,size,val;
bool check[100001];
int tmp[3];
int result=0;

int bfs()
{
    queue<int> q;
    q.push(N);
    check[N]=true;
    if(N==K) return 0;
    while(!q.empty())
    {
        size=q.size();
        result=result+1;
        for(int j=0;j<size;j++)
        {
            now=q.front();
            q.pop();
            tmp[0]=now-1;
            tmp[1]=now+1;
            tmp[2]=now*2;
            for(int i=0;i<3;i++)
            {
                if (tmp[i]<0||tmp[i]>100000) continue;
                if(tmp[i]==K) return result;
                val=tmp[i];
                if(check[val]==false)
                {
                    check[val]=true;
                    q.push(val);
                }
            }
        }
    }
}

int main()
{
    cin>>N>>K;
    fill_n(check,sizeof(bool)*100001,false);
    printf("%d",bfs());
}