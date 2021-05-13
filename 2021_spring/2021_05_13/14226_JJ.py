import sys
from collections import deque

input = sys.stdin.readline

def bfs(s):
    q = deque([(1,0,0)])
    visited = [[False for _ in range(1001)] for _ in range(1001)]
    visited[1][0] = True
    while q:
        now,clip,time = q.popleft()
        if now == s :
            return time
        
        # 화면에서 클립으로 복사
        if not visited[now][now]:
            q.append((now,now,time+1))
            visited[now][now] = True
               
        # 클립을 화면에 복사
        pasted = now + clip
        # print(pasted,clip)
        if pasted <= 1000 and not visited[pasted][clip]:
            q.append((pasted,clip,time+1))
            visited[pasted][clip] = True
        
        # 화면에서 하나 제거
        if not visited[now-1][clip] and now>1:
            q.append((now-1,clip,time+1))
            visited[now-1][clip] = True


s = int(input())
size = 1001
dp = [0 for _ in range(size)]

print(bfs(s))

