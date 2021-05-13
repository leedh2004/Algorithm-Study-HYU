from collections import deque
S = int(input())
# dp[S] 는 S 개의 이모티콘을 만드는데 걸리는 시간
dp = [ [-1 for _ in range(S+1) ] for _ in range(S+1) ]
q = deque()
# 현재 화면의 이모티콘 수, 현재 count, 클립보드에 복사된 수
q.append((1, 0, 0))
while q:
    s, cnt, copy = q.popleft()
    if s == S:
        print(cnt)
        break
    if s <= 0 or s > S or dp[s][copy] != -1:
        continue
    dp[s][copy] = cnt
    # 클립보드에 복사
    q.append((s, cnt+1, s))
    # 클립보드에 있는걸 복사함
    q.append((s+copy, cnt+1, copy))
    # 하나를 삭제함
    q.append((s-1, cnt+1, copy))



