import sys

N, K = map(int, sys.stdin.readline().strip().split())
C = list(map(int, sys.stdin.readline().strip().split()))
C = [ (0,i) for i in C ]

ans = 0
while True:
    # 종료 조건
    k = 0
    for r, n in C:
        if n == 0:
            k += 1
    if k >= K:
        break
    
    # 벨트 한 칸 회전
    C = [C[-1]] + C[:-1]
    # 로봇 이동
    for i in range(N, -1, -1):
        r, n = C[i]
        # 로봇 없음
        if r == 0:
            continue
        # 로봇 내려감
        
        if i == N or i == N-1:
            C[i] = (0, n)
            continue
        # 로봇 옆으로 이동, 내구도 증가
        nxt_r, nxt_n = C[i+1]
        if nxt_r == 0 and nxt_n > 0:
            C[i] = (0, n)
            C[i+1] = (1, nxt_n-1)
    
    # 첫번째 칸에 로봇이 없다면 올림
    r, n = C[0]
    if r == 0 and n >= 1:
        C[0] = (1, n-1)

    
    ans += 1
    
print(ans) 