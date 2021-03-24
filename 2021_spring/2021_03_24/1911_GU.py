import sys

# 문제를 1~6 을 1,2,3,4,5,6 점이 아니라 1~ 6사이 공간이라 봐야한다.

N, L = map(int, sys.stdin.readline().split())
puddles = []
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp.append(True)
    puddles.append(tmp)
puddles.sort()

if N == 1:
    if (puddles[0][1] - puddles[0][0]) % L == 0:
        print((puddles[0][1] - puddles[0][0])//L)
    else:
        print((puddles[0][1] - puddles[0][0])//L + 1)
else:
    for i in range(1, N):
        # 겹쳐진 구간 있음
        if puddles[i-1][1] >= puddles[i][0]:
            # 안읽어도 됨(합쳐짐)
            puddles[i-1][2] = False
            puddles[i][0] = puddles[i-1][0]
        # 떨어진 경우
        elif (puddles[i-1][1] - puddles[i-1][0]) % L > 0:
            if puddles[i-1][0] + (L * (((puddles[i-1][1]-puddles[i-1][0])//L)+1)) >= puddles[i][0]:
                puddles[i-1][2] = False
                puddles[i][0] = puddles[i-1][0]
    # print(puddles)
    ans = 0
    for i in range(N):
        if puddles[i][2]:
            if (puddles[i][1]-puddles[i][0]) % L == 0:
                ans += ((puddles[i][1]-puddles[i][0]) // L)
                # print(ans)
            else:
                ans += (((puddles[i][1]-puddles[i][0]) // L) + 1)
                # print(ans)
    print(ans)
