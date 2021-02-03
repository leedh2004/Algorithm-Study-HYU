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

int kmp(string T, string P)
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
                return 1;
            }
            //해당 문자열 일치
            else
            {
                j++;
            }
        }
    }
    return 0;
}

int main()
{
    string t, p, newt;
    getline(cin, t);
    getline(cin, p);
    for (int i = 0; i < t.length(); i++)
    {
        bool flag = true;
        for (int j = 0; j < 9; j++)
        {
            if (t[i] - '0' == j)
                flag = false;
        }
        if (flag)
            newt = newt + t[i];
    }
    cout << kmp(newt, p);
    return 0;
}