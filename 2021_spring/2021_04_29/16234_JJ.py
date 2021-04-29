import sys
import collections

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0] 

def bfs(a,b):
  q = [[a,b]] 
  q = collections.deque(q)
  ret = []

  while q:
    x,y = q.popleft()
    ret.append([x,y])

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위
      if (0<=nx<n) and (0<=ny<n)  and (not visited[nx][ny]) and check(table[x][y],table[nx][ny]):
        q.append([nx,ny])
        visited[nx][ny] = True

  return ret

def check(a,b):
  return l <= abs(b-a) <= r

def sumTable(arr):
  ret = 0
  for x,y in arr:
    ret = ret + table[x][y]
  val = ret//len(arr)
  for x,y in arr:
    table[x][y] = val

n,l,r = map(int,input().split())
table = []

for i in range(n):
  table.append(list(map(int,input().split())))

ans = 0
visited = None
while True:
  visited = [[False for _ in range(n)] for _ in range(n)]
  flag = False
  for i in range(n):
    for j in range(n):

        if not visited[i][j]:
          arr = bfs(i,j)

          if len(arr) > 1:
            print(ans,i,j,arr)
            sumTable(arr)
            flag = True
  if not flag :
    break
  else : 
    ans = ans + 1

print(ans)
