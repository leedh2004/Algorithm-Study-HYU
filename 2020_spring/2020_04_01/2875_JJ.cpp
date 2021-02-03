#include <iostream>

using namespace std;

int main()
{
    int n,m,k;
    cin>>n>>m>>k;
    int max_team=min(n/2,m);
    int left = (n+m)-3*max_team;
    if(k>left)
    {
        int tmp = (k-left)%3? (k-left)/3 +1 : (k-left)/3;
        max_team=max_team-tmp;
    }
    printf("%d", max_team);
    return 0;
}