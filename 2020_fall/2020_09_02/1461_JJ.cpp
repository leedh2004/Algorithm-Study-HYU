#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long int ll;
vector<int> pos;
vector<int> nag;
int n,m;

int main(){

    //입력 및 정렬
    int tmp;
    scanf("%d%d",&n,&m);
    for(int i=0;i<n;i++){
        scanf("%d",&tmp);
        if(tmp>0) pos.push_back(tmp);
        else nag.push_back(tmp);
    }
    sort(pos.begin(),pos.end());
    sort(nag.begin(),nag.end());
    
    //문제 해결
    // 1. 가장 먼 node를 찾고 해당 방향에 m개만큼 왕복이 아닌 경우를 고려
    // 2. m개씩 가장 먼 애들부터 m개씩 처리
    ll ans = 0;
    int n_idx = 0;
    int p_idx = pos.size()-1;

    //1번 처리
    if(( nag.size()==0 && pos.size()>0 ) || (pos.size()>0 &&  nag.size()>0 && pos[p_idx]> -nag[n_idx])){
        ans = ans + pos[p_idx];
        p_idx = p_idx - m;
    }else if((pos.size()==0 && nag.size()>0) || (pos.size()>0 &&  nag.size()>0 && pos[p_idx] < -nag[n_idx]) ){
        ans = ans - nag[n_idx];
        n_idx = n_idx + m;
    }

    // 2-1. 양수처리
    while (1){

        //탈출조건 - 인덱스를 넘어갈때
        if(p_idx < 0 || pos.size()==0) break;
        ans = ans + 2*pos[p_idx];
        p_idx = p_idx - m;
    }
    


    // 2-2. 음수처리
    while (1)
    {
        //탈출조건 - 인덱스를 넘어갈때
        if(n_idx > nag.size()-1 || nag.size()==0) break;
        ans = ans - 2*nag[n_idx];
        n_idx = n_idx + m;
    }
    

    //출력
    printf("%lld\n",ans);

    return 0;
}