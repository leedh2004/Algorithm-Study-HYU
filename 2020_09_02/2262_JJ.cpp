#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

typedef long long int ll;

int n,now_n;
int lank[257];
ll ans=0;

int main(){

    //입력
    scanf("%d",&n);
    now_n = n;
    for(int i=1;i<=n;i++) scanf("%d",&lank[i]);

    for(int j=1;j<n;j++){
        int min_index = 0;
        int min_lank = -1;

        //랭크 낮은애 찾기
        for(int i=1;i<=now_n;i++){
            if(min_lank < lank[i]){
                min_index = i;
                min_lank =lank[i];
            }
        }

        //합
        if (min_index==1) ans = ans + lank[min_index] - lank[min_index+1] ;
        else if (min_index==now_n) ans = ans + lank[min_index] - lank[min_index-1] ;
        else ans = ans + min(lank[min_index] - lank[min_index-1],lank[min_index] - lank[min_index+1]);
       
        for(int i=min_index;i<now_n;i++) lank[i] = lank[i+1];
        now_n--;

    }
    
    printf("%lld\n",ans);
    
    return 0;

}



/*
ll ans=0;
bool visited[257];


priority_queue <pair<int, pair<int,int> > > pq;

int main(){

    //입력
    scanf("%d",&n);
    for(int i=1;i<=n;i++) scanf("%d",&lank[i]);

    //우선순위큐 자료구조 생성
    for(int i=2;i<=n;i++){
        //우선순위가 높은것부터 뽑히기 때문에, -값으로 넣어준다.
        pq.push(make_pair( - abs(lank[i-1] - lank[i]),make_pair(i-1,i)));
    }

    //그리디 알고리즘
    while (!pq.empty()){
      
        //이미 방문하였을 때
        if( visited[pq.top().second.first] || visited[pq.top().second.second] ) {
            pq.pop();
            continue;
        }

        //차이합
        ans = ans - pq.top().first;


        int l = pq.top().second.first;
        int r = pq.top().second.second;

        pq.pop();


        //왼쪽이 클 때 -> 오른쪽이 진출함
        if(lank[l] > lank[r] ) {
            visited[l] = true;
            for(int i = l - 1;i>0;i--){
                if(!visited[i]){
                    //printf("push : %d %d\n",i,r);
                    pq.push( make_pair( -abs(lank[i] - lank[r]),make_pair(i,r)));
                    break;
                }
            }
        }
        //오른쪽이 클 때 -> 왼쪽이 진출함
        else{
            visited[r] = true;
            for(int i = r + 1;i<=n;i++){
                if(!visited[i]){
                    //printf("push : %d %d\n",l,i);
                    pq.push( make_pair( -abs(lank[i] - lank[l]),make_pair(l,i)));
                    break;
                }
            }
        }

    }

    printf("%lld\n",ans);
    

    return 0;
}
*/
