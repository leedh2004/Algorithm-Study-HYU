#include <cstdio>

using namespace std;
typedef long long int ll;

int main(){
    ll p[100];
    int t,num;
    p[1] = 1; p[2] = 1; p[3]=1; p[4]=2; p[5]=2; 
    for(int i=6;i<=100;i++) p[i] = p[i-1] + p[i-5];
    scanf("%d",&t);
    while (t--){
        scanf("%d",&num);
        printf("%lld\n",p[num]);
    }
    return 0;
}