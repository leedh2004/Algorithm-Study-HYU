#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


int main(){
    int t; scanf("%d",&t);
    while (t--){
        int n;scanf("%d",&n);
        int a,b;
        vector<pair<int,int> > v(n);
        for(int i=0;i<n;i++){
            scanf("%d%d",&a,&b);
            v[i]=make_pair(a,b);
        }
        //앞에있는녀석은 무조건 서류성적을 합격한다.

        //정렬
        sort(v.begin(),v.end());
       
        //초기화
        int ans=n;
        int m = v[0].second;

        //i의 시험성적은 무조건 j보다 우수하다(낮다 -> 정렬을 그렇게 했기 때문에)
        for(int i=1;i<n;i++)
        {
           if(m<v[i].second) ans--;
           m=min(m,v[i].second);
        }
        printf("%d\n",ans);
    }
    return 0;
}