#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>

using namespace std;

int T,M,N,K,now_x,now_y,tmp_x,tmp_y,size;
int result=0;
bool check[51][51];
int arr[51][51];
int dxy[4][2]={{-1,0},{1,0},{0,1},{0,-1}};

bool is_out(int x,int y)
{
    if ((x<0 || x>M)||(y<0||y>N)) return true;
    else return false;
}

int dfs()
{
    for(int i=1;i<=M;i++)
    {
        for(int j=1;j<=N;j++)
        {
            if(check[i][j]==false&&arr[i][j]==1)
            {
                //printf("%d,%d\n",i,j);
                result=result+1;
                stack<pair<int,int>> s;
                s.push(make_pair(i,j));
                check[i][j]=true;
                while(!s.empty())
                {
                    size=s.size();
                    for (int l=0;l<size;l++)
                    {
                        now_x=s.top().first;
                        now_y=s.top().second;
                        s.pop();
                        for(int w=0;w<4;w++)
                        {   
                            tmp_x=now_x+dxy[w][0];
                            tmp_y=now_y+dxy[w][1];
                            if(is_out(tmp_x,tmp_y)) continue;
                            else
                            {
                                if(arr[tmp_x][tmp_y]==1&&check[tmp_x][tmp_y]==false)
                                {
                                    check[tmp_x][tmp_y]=true;
                                    s.push(make_pair(tmp_x,tmp_y));
                                }
                            }
                        }
                    }
                }
            }
            
        }
    }
    return result;
}

int main()
{
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cin>>M>>N>>K;
        for(int p=0;p<51;p++)fill_n(check[p],sizeof(bool)*51,false);
        for(int p=0;p<51;p++)fill_n(arr[p],sizeof(int)*51,0);
        for(int j=0;j<K;j++)
        {
            cin>>tmp_x>>tmp_y;
            arr[tmp_x+1][tmp_y+1]=1;
        }
        printf("%d\n",dfs());
        result=0;
    }
}