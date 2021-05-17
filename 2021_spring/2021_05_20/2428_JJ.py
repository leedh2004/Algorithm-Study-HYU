import sys

input = sys.stdin.readline

def slide(nowIdx):
    global slideIdx
    if slideIdx == n:
        return
    while solution[nowIdx]>=solu90[slideIdx]:
        slideIdx = slideIdx + 1
        if slideIdx==n:
            break

n = int(input())
solution = list(map(int,input().split()))
solution = sorted(solution)
solu90 = [ num*0.9 for num in solution ]

slideIdx = 0
ans = 0
for i in range(n):
    slide(i)
    ans = ans + (slideIdx-i-1)
print(ans)


