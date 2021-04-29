import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def is_in(x,y):
  return 0<=x<n+2 and 0<=y<m+2

def dfs(x,y):
  if visited[x][y]:
    return

  visited[x][y]=True

  if table[x][y] == 1:
    table[x][y] = 0
    return
  
  for i in range(4):
    nx,ny = x+dx[i] , y+dy[i]
    if is_in(nx,ny):
      dfs(nx,ny)

def countCheese():
  ret = 0
  for i in range(n):
    for j in range(m):
      if table[i][j] == 1:
        ret = ret + 1
  return ret


def p():
  for i in range(n+2):
    print(table[i])


n,m = map(int,input().split())
table = []
table.append([0 for _ in range(m+2)])
for i in range(n):
  table.append( [0]+list(map(int,input().split()))+[0] )
table.append([0 for _ in range(m+2)])


dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = None

day = 0
cnt = countCheese()
ret = cnt

while True:
  visited = [[ False for _ in range(m+2)] for _ in range(n+2)]
  dfs(0,0)
  cnt = countCheese()
  if cnt == 0:
    break
  ret = cnt
  day = day +1

print(day+1)
print(ret)



