#include <cstdio>

int gcd(int a,int b){
    if(b==0) return a;
    return gcd(b,a%b);
}

int lcm(int a,int b){
    return (a*b)/gcd(a,b);
}


int main(){
    int a,b,c,d,bottom,top,tmp;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    bottom = lcm(b,d);
    top = a*(bottom/b)+c*(bottom/d);
    tmp = gcd(bottom,top);
    printf("%d %d\n",top/tmp,bottom/tmp);
}