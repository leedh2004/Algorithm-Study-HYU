#include <cstdio>

using namespace std;

typedef long long int ll;

ll s[1001];

int main(){

    //전처리
    int idx = 1; bool flag = false;
    for(int i=1;i<1000;i++){
        for(int j=1;j<=i;j++){
            if(idx==1001){
                flag = true;
                break;
            }
            s[idx] = s[idx-1] + i;
            idx++;
        }
        if(flag) break;
    }

    //입력 및 출력
    int st,ed;
    scanf("%d%d",&st,&ed);
    printf("%lld\n",s[ed]-s[st-1]);
    return 0;
}
