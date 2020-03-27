import sys
from collections import deque

time = [0] * 100001
def bfs(a,b):   
    q = deque()
    q.append(a)

    while q:
        cur = q.popleft()
        if cur == b:
            print(time[cur])
            break
        next_ = cur +1
        if 0 <= next_ < 100001 and time[next_] == 0:
            time[next_] = time[cur] +1
            q.append(next_)
        next_ = 2 * cur
        if 0 <= next_ < 100001 and time[next_] == 0:
            time[next_] = time[cur] +1
            q.append(next_)
        next_ = cur -1
        if 0 <= next_ < 100001 and time[next_] == 0:
            time[next_] = time[cur] +1
            q.append(next_)

    
a,b = map(int,sys.stdin.readline().split())
bfs(a,b)