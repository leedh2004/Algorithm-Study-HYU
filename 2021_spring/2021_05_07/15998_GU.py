import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N = int(sys.stdin.readline())
logs = [[0, 0]]
M = 0
# 충전 필요 금액(a 음수 기준) b - (a + rest)
for i in range(1, N+1):
    a, b = map(int, sys.stdin.readline().split())
    logs.append([a, b])
    M = gcd(M, b-(a+logs[i-1][1]))
flag = False
for i in range(1, N+1):
    if logs[i][0] > 0:
        if logs[i][0] + logs[i-1][1] == logs[i][1]:
            continue
        else:
            flag = True
            break
    # a < 0
    else:
        # 충전하면 안됨
        if logs[i-1][1] + logs[i][0] >= 0:
            if logs[i-1][1] + logs[i][0] == logs[i][1]:
                continue
            else:
                flag = True
                break
        # 충전하는 경우
        else:
            # 최소(!!) 충전단위인데 충전 후 출금 후 잔액이 더 크면 모순
            if M != 0 and M <= logs[i][1]:
                flag = True
                break
if flag:
    print(-1)
elif M == 1 or M == 0:
    print(1)
else:
    print(M)
"""
def get_divisor(n):
    n = int(n)
    divisors = []

    for i in range(1, n + 1):
        if (n % i == 0):
            divisors.append(i)

    return divisors


N = int(sys.stdin.readline())
logs = []
for _ in range(N):
    logs.append(list(map(int, sys.stdin.readline().split())))
rest = 0
not_exist = False
not_charge = True
first = True
candidate = []
for a, b in logs:
    if a > 0:
        if rest + a == b:
            rest = b
            continue
        else:
            not_exist = True
            break
    else:
        if rest + a >= 0:
            if rest + a != b:
                not_exist = True
                break
            else:
                rest = b
                continue
        else:
            not_charge = False
            if first:
                candidate = get_divisor(b-(rest+a))
                first = False
                rest = b
                continue
            for c in candidate[:]:
                cur = c
                while True:
                    if cur >= abs(rest + a):
                        break
                    else:
                        cur += c
                if cur + rest + a != b:
                    candidate.remove(c)

            if candidate:
                rest = b
            else:
                not_exist = True
                break
if not_charge:
    print(1)
elif not candidate or not_exist:
    print(-1)
else:
    for i in range(len(candidate)):
        if candidate[i] <= 9*(10**18):
            print(candidate[i])
            break
        if i == len(candidate)-1:
            print(-1)

"""
