#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

void solve()
{
    /* 메모리 할당 */
    int N = 0;
    int x, y, d, g;
    cin >> N;

    int** pattern = new int* [4];
    bool check[101][101];
    memset(check, false, sizeof(check));

    for (int i = 0; i < 4; ++i) {
        pattern[i] = new int[1024];
        memset(pattern[i], 0, sizeof(int) * 1024);   // 메모리 공간을 0으로 초기화
    }

    pattern[0][0] = 0;
    pattern[1][0] = 1;
    pattern[2][0] = 2;
    pattern[3][0] = 3;

    for (int i = 0; i < 4; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            int start = (int)pow(2, j - 1);
            int end = (int)pow(2, j);
            for (int k = start, l = 1; k < end; k++, l +=2)
            {
                if (pattern[i][k - l] + 1 == 4) {
                    pattern[i][k] = 0;
                }
                else
                    pattern[i][k] = pattern[i][k - l] + 1;
            }
        }
    }

    for (int i = 0; i < N; i++)
    {
        cin >> x >> y >> d >> g;
        int end = (int)pow(2, g);

        int cur_x = x;
        int cur_y = y;
        check[cur_y][cur_x] = true;

        for (int j = 0; j < end; j++)
        {
            if (pattern[d][j] == 0) {
                cur_x++;
            }
            else if (pattern[d][j] == 1) {
                cur_y--;
            }
            else if (pattern[d][j] == 2) {
                cur_x--;
            }
            else if (pattern[d][j] == 3) {
                cur_y++;
            }
            check[cur_y][cur_x] = true;
        }

    }

    int res = 0;

    for (int i = 0; i < 100; i++)
    {
        for (int j = 0; j < 100; j++)
        {
            if (check[i][j] && check[i + 1][j] && check[i][j + 1] && check[i + 1][j + 1])
                res++;
        }
    }
    cout << res << '\n';

    /* 메모리 해제 */
    for (int i = 0; i < 4; ++i) {
        delete[] pattern[i];
    }
    delete[] pattern;

}

int main(void)
{
    solve();
	return 0;
}