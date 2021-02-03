import sys

N = int(sys.stdin.readline())
cur_x, cur_y = -(10**9), -(10**9)
next_x, next_y = -(10**9), -(10**9)
cur_x, cur_y = map(int, sys.stdin.readline().split())
ans = abs(cur_y - cur_x)
for _ in range(N-1):
    next_x, next_y = map(int, sys.stdin.readline().split())
    if cur_y <= next_x:
        ans += abs(next_y - next_x)
        cur_x, cur_y = next_x, next_y
    else:
        if next_y > cur_y:
            ans += abs(cur_y - next_y)
            cur_x, cur_y = next_x, next_y
        else:
            cur_x = next_x
print(ans)
