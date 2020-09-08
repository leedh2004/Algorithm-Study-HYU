#include <cstdio>

using namespace std;

int n;
char table[102][102];
bool visited1[101][101];
bool visited2[101][101];
int dir[4][2] = {{-1,0},{1,0},{0,1},{0,-1}};
int ans1=0;
int ans2=0;

bool is_in(int x,int y){
    return ( 0<x && x<=n ) && ( 0<y && y<=n);
}


void dfs1(int x,int y){

    // printf("dfs1 - %d %d %c\n",x,y,table[x][y]);

    //이미 방문했다면 return
    if(visited1[x][y]) return;

    visited1[x][y] = true;

    //4방향 조사
    for(int i=0;i<4;i++){
        int nx = x + dir[i][0];
        int ny = y + dir[i][1];
        if( is_in(nx,ny)&& !visited1[nx][ny] && table[x][y] == table[nx][ny] ) dfs1(nx,ny);
    }
}

void dfs2(int x,int y){

    // printf("dfs2 - %d %d %c\n",x,y,table[x][y]);

    //이미 방문했다면 return
    if(visited2[x][y]) return;

    visited2[x][y] = true;

    //4방향 조사
    for(int i=0;i<4;i++){
        int nx = x + dir[i][0];
        int ny = y + dir[i][1];
        if( is_in(nx,ny)&& !visited2[nx][ny]){
            
            //기존로직
            if( table[x][y] == table[nx][ny]) dfs2(nx,ny);

            //적록색약
            else if( (table[x][y]=='G'&&table[nx][ny]=='R') || (table[x][y]=='R'&&table[nx][ny]=='G') ) dfs2(nx,ny);
        
        } 
    }
}



int main(){

    //입력
    scanf("%d",&n);
    for(int i=1;i<=n;i++)scanf("%s",&table[i][1]);

    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){

            //정상인
            if(!visited1[i][j]){
                ans1++;
                dfs1(i,j);
            }

            //적록색약
            if(!visited2[i][j]){
                ans2++;
                dfs2(i,j);
            }

        }
    }

    printf("%d %d\n",ans1,ans2);

    return 0;
}