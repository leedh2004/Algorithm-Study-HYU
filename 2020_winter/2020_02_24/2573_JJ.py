import sys
sys.setrecursionlimit(100000)

d = [[-1,0],[1,0],[0,-1],[0,1]]

def is_in(r,c):
  return 0<=r<n and 0<=c<m

def dfs(r,c,visited):
  visited[r][c] = True
  for i in range(4):
    nr = r + d[i][0]
    nc = c + d[i][1]
    if is_in(nr,nc) and not visited[nr][nc] and table[nr][nc]:
      dfs(nr,nc,visited)

def getNum():
  visited = [[ False for _ in range(m) ] for _ in range(n)]
  ret = 0
  for i in range(n):
    for j in range(m):
      if table[i][j] and not visited[i][j]:
        dfs(i,j,visited)
        ret = ret + 1
  return ret


def calMelt(r,c):
  ret = 0
  for i in range(4):
    nr = r + d[i][0]
    nc = c + d[i][1]
    if is_in(nr,nc) and not table[nr][nc]:
      ret = ret + 1
  return ret

def tableChage(table,queue):
  # print(queue)
  newTable = [[ 0 for _ in range(m) ] for _ in range(n)]
  newQueue = []
  for i in range(len(queue)):
    r,c,val = queue[i][0],queue[i][1],queue[i][2]
    nextVal = val - calMelt(r,c)
    if nextVal>0:
      newQueue.append([r,c,nextVal])
      newTable[r][c]= nextVal
  return newTable,newQueue

n,m = map(int,sys.stdin.readline().split())
table = []
queue = []

for i in range(n):
  row = list(map(int,sys.stdin.readline().split()))
  for j in range(m):
    # 바다가 아니라면 큐에 넣음
    if row[j] :
      queue.append([i,j,row[j]])
  table.append(row)

iceNum,queueNum = getNum(),len(queue)
ans = 0
flag = False
while True:
  # 1년 지남
  table,queue = tableChage(table,queue)
  ans = ans + 1
  iceNum,queueNum = getNum(),len(queue)
  # 성공
  if iceNum>=2:
    flag=True
    break
  
  if queueNum == 0:
    break

if flag:
  print(ans)
else :
  print(0)




