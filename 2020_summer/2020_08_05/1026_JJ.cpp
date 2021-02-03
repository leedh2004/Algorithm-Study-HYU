#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int n; scanf("%d",&n);
    int A[50],B[50],ans=0;
    for(int i=0;i<n;i++) scanf("%d",&A[i]);
    for(int i=0;i<n;i++) scanf("%d",&B[i]); 
    sort(&A[0],&A[n]);
    sort(&B[0],&B[n]);
    for(int i=0;i<n;i++) ans = ans + A[i]*B[n-i-1];
    printf("%d\n",ans);
    return 0;
}