#include<cstdio>
#include<cstring>
#include<queue>
#include<vector>

using namespace std;

struct Coord{
    //Coord(int x,int y,int z):X(x),Y(y),Z(z){}
    int X,Y,Z;
};

queue <Coord> q;


int l,r,c;
char map[30][30][30];
Coord start,End;


//움직이는 방향 - 위 아래, 사방
int dir[6][3] = {{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};


bool is_in(int x,int y,int z){
    return 0<=x && x<l && 0<=y && y< r && 0<=z && z<c ;
}

int main()
{
    bool visited[30][30][30];
    char tmp;
    while(1){
        scanf("%d%d%d",&l,&r,&c);
        
        //쓰레기제거
        scanf("%c",&tmp);

        //종료조건
        if((l || r || c)==0) break;

        //입력
        for(int i=0;i<l;i++){
            for(int j=0;j<r;j++){
                for(int k=0;k<c;k++){
                    scanf("%c",&map[i][j][k]);
                    if(map[i][j][k]=='S'){
                        start.X=i;
                        start.Y=j;
                        start.Z=k;
                    }
                    else if(map[i][j][k]=='E'){
                        End.X=i;
                        End.Y=j;
                        End.Z=k;
                    }
                }
                scanf("%c",&tmp);
            }
            scanf("%c",&tmp);
        }

        //초기화
        int ans = 0;
        bool flag = false;
        memset(visited,false,sizeof(visited));
        visited[start.X][start.Y][start.Z] = true;
        while (!q.empty()) q.pop();
    
        //bfs
        q.push(start);
        while (!q.empty())
        {
            int sz = q.size();
            ans++;
            for(int i=0;i<sz;i++){
                //현재위치
                Coord now = q.front();
                q.pop();
                for(int i=0;i<6;i++){
                    Coord next;
                    next.X = now.X + dir[i][0];
                    next.Y = now.Y + dir[i][1];
                    next.Z = now.Z + dir[i][2];
                    //정육면체 내부이면서, 방문하지 않았고, 지나갈수 있는 경로가 있을때
                    if(is_in(next.X,next.Y,next.Z)&& !visited[next.X][next.Y][next.Z] &&(map[next.X][next.Y][next.Z]=='.'||map[next.X][next.Y][next.Z]=='E')){
                        visited[next.X][next.Y][next.Z] = true;
                        if(map[next.X][next.Y][next.Z]=='E'){
                            flag = true;
                            break;
                        }
                        q.push(next);
                    }
                }
                if(flag) break;
            }
            if(flag) break;
        }
        if(!flag) printf("Trapped!\n");
        else printf("Escaped in %d minute(s).\n",ans);
    }
    return 0;
}