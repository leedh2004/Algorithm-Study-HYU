#include<iostream>
#include<cstdio>
#include<set>


using namespace std;

int c;
int adj[6000][6000];
int n_arr[6000];
int coord[6000][20][3];

void full_search(){
    for(int i=0;i<c;i++){
        for(int j=0;j<c;j++){
            for(int k=0;k<c;k++){
                if(adj[i][k] + adj[k][j] < adj[i][j]) adj[i][j] = adj[i][k] + adj[k][j];
            }
        }
    }
}

int main()
{
    int check = 0;
    int q,start,end;

    scanf("%d",&c);
    for(int i=0;i<c;i++){
        scanf("%d",&n_arr[i]);
        //printf("narr = %d\n",n_arr[i]  ); 
        for(int j=0;j<n_arr[i];j++){
            for(int k=0;k<3;k++) {
                //printf("%d %d %d \n",i,j,k); 
                scanf("%d",&coord[i][j][k]);
            }
        }
    }

    //printf("check1\n");

    for(int i=0;i<c;i++){
        for(int j=0;j<c;j++){
            if(i==j) adj[i][j] = 0;
            else adj[i][j] = 10000;
        }
    }

    //기준
    for(int i=0;i<c;i++){
        //대상
        for(int j=i+1;j<c;j++){
            //기준 배열
            check = 0;
            for(int k=0;k<n_arr[i];k++){
                //대상 배열
                for(int l=0;l<n_arr[j];j++){
                    if(coord[i][k][0] == coord[j][l][0] && coord[i][k][1] == coord[j][l][1] && coord[i][k][2] == coord[j][l][2]) check++;
                }
            }
            if (check>1){
                adj[i][j] = 1;
                adj[j][i] = 1;
            }
        }
    }

    for(int i=0;i<c;i++){
        for(int j=0;j<c;j++){
           printf("%d ",adj[i][j]);
        }
        printf("\n");
    }



    //printf("check1\n");

    full_search();

    scanf("%d",&q);
    for(int i=0;i<q;i++){
        scanf("%d%d",&start,&end);
        printf("%d\n",adj[start-1][end-1]);
    }
    return 0;
}