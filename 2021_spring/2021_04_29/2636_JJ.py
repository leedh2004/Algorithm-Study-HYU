import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def is_in(x,y):
  return 0<=x<n+2 and 0<=y<m+2

def dfs(x,y):
  # 이미 방문한 경우
  if visited[x][y]:
    return
  # 방문 표시
  visited[x][y]=True

  # 만약 치즈일때
  if table[x][y] == 1:
    # 녹은 것을 표시하고 내부 치즈들까지 탐색안되도록 바로 return
    table[x][y] = 0
    return
  
  # 공기일때
  for i in range(4):
    nx,ny = x+dx[i] , y+dy[i]

    # x,y 범위 체크하면서 dfs
    if is_in(nx,ny):
      dfs(nx,ny)

# 치즈 갯수 
def countCheese():
  ret = 0
  for i in range(n):
    for j in range(m):
      if table[i][j] == 1:
        ret = ret + 1
  return ret

n,m = map(int,input().split())
table = []
table.append([0 for _ in range(m+2)])
for i in range(n):
  table.append( [0]+list(map(int,input().split()))+[0] )
table.append([0 for _ in range(m+2)])


dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 전역변수로 사용
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



