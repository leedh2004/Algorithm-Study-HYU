import sys
N = int(sys.stdin.readline())
sols = list(map(int, sys.stdin.readline().split()))
sols.sort()
start = 0
end = N-1
_min = sys.maxsize
ans1, ans2 = 0, 0

while start < end:
    S = sols[start] + sols[end]
    if abs(S) < _min:
        ans1, ans2 = sols[start], sols[end]
        _min = abs(S)

    if S <= 0:
        start += 1
    else:
        end -= 1
print(ans1, ans2)

"""
import sys
from heapq import heappush, heappop

# N개의 용액들의 특성값은 모두 다르고
N = int(sys.stdin.readline())
sols = list(map(int, sys.stdin.readline().split()))
A, B = [], []
zeros = 0
for i in range(N):
    if sols[i] > 0:
        heappush(A, sols[i])
    elif sols[i] < 0:
        heappush(B, -sols[i])
    else:
        zeros += 1

INF = sys.maxsize
ans1, ans2 = -INF, INF
ans = INF
if not A and B:
    if zeros == 0:
        print(-B[1], -B[0])
    elif zeros == 1:
        print(-B[0], 0)
elif A and not B:
    if zeros == 0:
        print(A[0], A[1])
    elif zeros == 1:
        print(0, A[0])
else:
    if zeros == 1:
        tmp = [A[0], B[0], abs(A[0]-B[0])]
        if tmp[0] == min(tmp):
            print(0, A[0])
        elif tmp[1] == min(tmp):
            print(-B[0], 0)
        else:
            print(-B[0], A[0])
    else:
        for i in range(len(A)):
            right = heappop(A)
            if ans1 != -INF and abs(right + ans1) <= abs(ans):
                ans2 = right
                ans = ans1 + ans2
            if A and ans1 != -INF and abs(A[0] + ans1) <= abs(ans):
                continue
            while B:
                if abs(right - B[0]) <= abs(ans):
                    ans1, ans2 = -heappop(B), right
                    ans = ans1 + ans2
                else:
                    break
        print(ans1, ans2)
"""
