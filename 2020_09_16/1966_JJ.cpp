#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>

using namespace std;

int t,n,m;
// first - 중요도 
// second - 원래인덱스(M값 찾을때 사용)
pair<int,int> arr[101];


//스왑함수
void swap(pair<int,int>* a,pair<int,int>* b){
    int tmp1 = a->first;
    int tmp2 = a->second;
    a->first = b->first;
    a->second = b->second;
    b->first = tmp1;
    b->second = tmp2;
}

void solve(){
    int left = n;

    while (1){

        //우선순위 높은애 찾기
        int p = 0;
        int p_index = 0;
        for(int i=0;i<left;i++){
            if(p<arr[i].first){
                p = arr[i].first;
                p_index = i;
            }
        }

        int target_index;


        //비교
        if(p_index == 0) {
            //남은 원소--
            left--;
            target_index = 0;

            //종료조건
            if(arr[target_index].second == m) break;

            //밀어주기
            for(int i=0;i<left;i++){
                arr[i].first = arr[i+1].first;
                arr[i].second = arr[i+1].second;
            }
        }
        else {
        
            //맨 앞 값 저장
            int tmp1 = arr[0].first;
            int tmp2 = arr[0].second;

            //앞에서 부터 밀어주기
            for(int i=0;i<left;i++){
                arr[i].first = arr[i+1].first;
                arr[i].second = arr[i+1].second;
            }
            
            arr[left-1].first = tmp1;
            arr[left-1].second = tmp2; 
        }
    }
    printf("%d\n",n-left);
}

int main(){

    //입력
    scanf("%d",&t);
    while (t--){
        scanf("%d %d",&n,&m);
        //인덱스값넣기
        for(int i=0;i<n;i++) arr[i].second = i;
        for(int i=0;i<n;i++) scanf("%d",&arr[i].first);
        solve();
    }
    
}