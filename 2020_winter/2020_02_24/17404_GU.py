import sys

INF = sys.maxsize
N = int(sys.stdin.readline())
price = []
for i in range(N):
    price.append(list(map(int, sys.stdin.readline().split())))
# d[i][j][k]
# i - i번째 집 색칠할 때
# j - R,G,B 선택(0,1,2)
# k - 첫번째 집 R,G,B(0,1,2)
d = [[[INF for _ in range(3)] for _ in range(3)] for _ in range(N)]

d[0][0][0] = price[0][0]
d[0][1][1] = price[0][1]
d[0][2][2] = price[0][2]

for i in range(1, N):
    if i != N-1:
        for j in range(3):
            d[i][0][j] = min(d[i-1][1][j]+price[i][0],
                             d[i-1][2][j]+price[i][0])
            d[i][1][j] = min(d[i-1][0][j]+price[i][1],
                             d[i-1][2][j]+price[i][1])
            d[i][2][j] = min(d[i-1][0][j]+price[i][2],
                             d[i-1][1][j]+price[i][2])
    else:
        d[i][0][1] = min(d[i-1][1][1]+price[i][0], d[i-1][2][1]+price[i][0])
        d[i][0][2] = min(d[i-1][1][2]+price[i][0], d[i-1][2][2]+price[i][0])
        d[i][1][0] = min(d[i-1][0][0]+price[i][1], d[i-1][2][0]+price[i][1])
        d[i][1][2] = min(d[i-1][0][2]+price[i][1], d[i-1][2][2]+price[i][1])
        d[i][2][0] = min(d[i-1][0][0]+price[i][2], d[i-1][1][0]+price[i][2])
        d[i][2][1] = min(d[i-1][0][1]+price[i][2], d[i-1][1][1]+price[i][2])

tmp = d[N-1]
ans = []
for i in range(3):
    ans.extend(tmp[i])
print(min(ans))
