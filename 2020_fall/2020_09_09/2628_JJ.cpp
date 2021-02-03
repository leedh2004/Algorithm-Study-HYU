#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

int h,w,t;
int val,num;

vector<int> wv;
vector<int> hv;


int main(){

    wv.push_back(0);
    hv.push_back(0);

    scanf("%d%d",&w,&h);
    scanf("%d",&t);

    wv.push_back(w);
    hv.push_back(h);

    while (t--){
        scanf("%d%d",&val,&num);
        if(val==0) hv.push_back(num);
        else wv.push_back(num);  
    }

    sort(hv.begin(),hv.end());
    sort(wv.begin(),wv.end());

    int maxw=0,maxh=0;
    for(int i=1;i<hv.size();i++) maxh = max(maxh,hv[i]-hv[i-1]);
    for(int i=1;i<wv.size();i++) maxw = max(maxw,wv[i]-wv[i-1]);

    printf("%d\n",maxh*maxw);

    return 0;
}