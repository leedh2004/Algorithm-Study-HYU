#include <iostream>
#include <cstdio>

int n;
int table[65][65];

void divide_conquer(int s_x , int s_y , int b_x, int b_y ){
    //printf("x size : %d y size : %d\n",b_x-s_x+1,b_y-s_y+1);
    if(s_x==b_x && s_y==b_y)
    {
        printf("%d",table[s_x][s_y]);
        return ;
    }
    bool flag=true;
    int val = table[s_x][s_y];
    for(int i=s_x;i<=b_x;i++){
        for(int j=s_y;j<=b_y;j++){
            if(table[i][j]!=val) flag=false;
        }
    }
    if(flag){
        printf("%d",val);
        return ;
    }
    printf("(");
    divide_conquer(s_x          ,s_y,(s_x+b_x)/2 , (s_y+b_y)/2 );
    divide_conquer(s_x          ,(s_y+b_y)/2 +1 , (s_x+b_x)/2,b_y);
    divide_conquer((s_x+b_x)/2+1,s_y            , b_x, (s_y+b_y)/2 );
    divide_conquer((s_x+b_x)/2+1,(s_y+b_y)/2 +1 ,b_x , b_y);
    printf(")");
    return ;
}
int main(){
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++) scanf("%1d",&table[i][j]);
    }
    divide_conquer(1,1,n,n);
    return 0;
}