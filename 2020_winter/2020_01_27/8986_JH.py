import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int,input().split()))

def solution(now_x):
    global X
    
    result = 0
    for i, x in enumerate(X) :
        result += abs(i*now_x-x)

    return result

lw, hi = X[0], X[-1]

while hi-lw > 3 :
    p, q = (2*lw+hi)//3, (lw+2*hi)//3
    fp, fq = solution(p), solution(q)
    if fp > fq :
        lw = p
    else :
        hi = q

result = 1e20   # 이거 최대한 큰 수 넣어줘야 함
for i in range(lw,hi+1):
    result = min(result, solution(i))
print(result)