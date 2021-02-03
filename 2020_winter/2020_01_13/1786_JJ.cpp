#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> fail(string T)
{
    int n = T.length();

    //T의 크기만큼의 0으로 초기화된 벡터 배열 선언
    vector<int> f(n, 0);
    int j = 0;
    for (int i = 1; i < n; i++)
    {
        //일치하지 않을 때 현재까지의 접미사와 접두사가 동일한 갯수만큼 이동
        while (j > 0 && T[i] != T[j])
            j = f[j - 1];

        //일치할 때
        if (T[i] == T[j])
            f[i] = ++j;
    }
    return f;
}

vector<int> kmp(string T, string P)
{
    vector<int> ans;
    vector<int> f = fail(P);
    int n = T.length();
    int m = P.length();
    int j = 0;
    for (int i = 0; i < n; i++)
    {
        while (j > 0 && T[i] != P[j])
            j = f[j - 1];
        if (T[i] == P[j])
        {
            //모두 일치하는경우
            if (j == m - 1)
            {
                //정답벡터에 삽입
                ans.push_back(i - m + 1);
                j = f[j];
            }
            //해당 문자열 일치
            else
            {
                j++;
            }
        }
    }
    return ans;
}

int main()
{
    string t, p;
    getline(cin, t);
    getline(cin, p);
    vector<int> ans = kmp(t, p);
    cout << ans.size() << "\n";
    for (int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] + 1 << " ";
    }
    cout << "\n";
    return 0;
}