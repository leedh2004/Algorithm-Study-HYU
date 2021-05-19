import sys


def sol(flag, left, right):

    if left > right:
        return 0

    if d[left][right] != -1:
        return d[left][right]

    if flag:
        d[left][right] = max(cards[left] + sol(False, left+1, right),
                             cards[right]+sol(False, left, right-1))
        return d[left][right]
    # 근우 기준이므로 카드 더해주긴 안하고 그냥 넘겨줌 다음 함수로
    else:
        d[left][right] = min(sol(True, left+1, right),
                             sol(True, left, right-1))
        return d[left][right]


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    d = [[-1 for _ in range(N)] for _ in range(N)]
    print(sol(True, 0, N-1))
