#include <queue>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>

using namespace std;

int N,M;

int way[4][2]={{-1,0},{1,0},{0,1},{0,-1}};

int bfs(char table[][110], bool check[][110])
{
    queue<int> q_x;
    queue<int> q_y;
    q_x.push(1);
    q_y.push(1);
    int result = 1;
    while(!q_x.empty())
    {
        int tmp = q_x.size();
        for(int i=0;i<tmp;i++)
        {
            int now_x=q_x.front();
            int now_y=q_y.front();
            
            q_x.pop();
            q_y.pop();
            
            for(int j=0;j<4;j++)
            {
                int tmp_x=now_x+way[j][0];
                int tmp_y=now_y+way[j][1];
                if ((tmp_x==N)&&(tmp_y==M)) return (result+1);
                if(table[tmp_x][tmp_y]=='1'&&check[tmp_x][tmp_y]==false)
                {
                    q_x.push(tmp_x);
                    q_y.push(tmp_y);
                    check[tmp_x][tmp_y]=true;
                }
            }
            
        }
        result=result+1;
    }
}


int main()
{
    cin >>N>>M;
    bool check[110][110];
    char arr[110][110];
    long long num;
    for(int i=0;i<N+2;i++) fill_n(arr[i],sizeof(char)*(M+1),'b');
    for(int i=0;i<N+1;i++) fill_n(check[i],sizeof(bool)*M,false);
    for(int j=1;j<=N;j++) scanf("%s",&arr[j][1]);
    //for(int i=0;i<N+2;i++) printf("%s\n",arr[i]);
    printf("%d",bfs(arr,check));
}