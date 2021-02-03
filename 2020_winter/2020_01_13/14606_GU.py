import sys

N = int(sys.stdin.readline())
tops = [N]
ans = 0

while tops:
    top = tops.pop()
    if top == 1: continue
    B,C = (top//2), (top - (top//2))
    tops.extend([B,C])
    ans += B*C
print(ans)

