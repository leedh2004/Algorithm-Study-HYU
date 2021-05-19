from bisect import bisect_right

N = int(input())
A = list(map(int, input().split()))
A = sorted(A)
B = list(map(lambda x: 10 / 9 * x, A))
ans = 0
for idx, a in enumerate(B):
    v = bisect_right(A, a) - (idx + 1)
    if v > 0:
        ans += v
print(ans)
