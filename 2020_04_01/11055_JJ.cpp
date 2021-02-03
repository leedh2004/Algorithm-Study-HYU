#include <iostream>
#include <cstdio>

using namespace std;

int n;
int a[1001];
int ans[1001];
int num=0;

int main()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++) scanf("%d",&a[i]);
    for(int i=1;i<=n;i++)
    {
        ans[i]=a[i];
        for(int j=1;j<i;j++)
        {
            if(a[i]>a[j] && ans[i]<ans[j]+a[i])
            {
                ans[i]=ans[j]+a[i];
            }
        }
        num=max(num,ans[i]);
    }
    printf("%d\n",num);
    return 0;
}