import sys

# unionfind - 소속 찾기
def getParent(x):
  if p[x]==x:
    return x
  else :
    p[x] = getParent(p[x])
    return getParent(p[x])

# unionfind - 소속 결합
def merge(a,b):
  pA = getParent(a)
  pB = getParent(b)

  # 연결 안하는 경우
  if pA==pB:
    return False

  # 연결하는 경우
  else :
    p[pA] = p[pB]
    return True

n,m = map(int,sys.stdin.readline().split())
kinds = sys.stdin.readline().split()

# 엣지 입력
edges = []
for i in range(m):
  u,v,d = map(int,sys.stdin.readline().split())
  edges.append([u-1,v-1,d])

# 엣지 정렬
edges.sort(key=lambda x:(x[2]))

# Union-Find 배열 선언
p = list(range(n))

edgeNum = 0
ans = 0
flag = False

for i in range(m):
  u,v,d = edges[i][0],edges[i][1],edges[i][2]

  # 다른 성별의 학교끼리 연결
  if kinds[u]!= kinds[v] and merge(u,v):
    edgeNum = edgeNum + 1
    ans = ans + d

  if edgeNum == n-1:
    flag = True
    break

if flag:
  print(ans)
else :
  print(-1)