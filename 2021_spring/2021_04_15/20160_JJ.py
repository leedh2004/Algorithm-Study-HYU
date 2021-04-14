import sys
import heapq
input = sys.stdin.readline

INF = 100000000001

# 다이스트라
def dijkstra(start):
  h = []
  d = [INF for _ in range(V)]
  d[start] = 0
  heapq.heappush(h,[d[start],start])
  
  while h:
    time,node = heapq.heappop(h)

    # 이부분 없으면 시간초과
    if d[node] < time:
      continue

    for i in range(len(adjList[node])):
      nextTime, nextNode = adjList[node][i][0]+time,adjList[node][i][1]
      if nextTime < d[nextNode]:
        d[nextNode] = nextTime
        heapq.heappush(h,[nextTime,nextNode])

  return d


V,E = map(int,input().split())

# 인접 행렬
adjMetrix = [[INF for _ in range(V)] for _ in range(V) ]
for _ in range(E):
  u,v,w = map(int,input().split())
  adjMetrix [u-1][v-1] = min(adjMetrix [u-1][v-1], w) # 정점사이에 간선이 여러개 있을 수도 있으니 min 으로 받는다.
  adjMetrix [v-1][u-1] = min(adjMetrix [v-1][u-1], w) # 도로 == 양방향

# 인접행렬 -> 인접리스트
adjList = [[] for _ in range(V)]
for i in range(V):
  for j in range(V):
    if i!=j and adjMetrix[i][j] != INF:
      adjList[i].append([adjMetrix[i][j],j])

visited = [False for _ in range(V)] # 해당 node에서 다이스트라를 돌렸는지
dist = [[INF for _ in range(V)] for _ in range(V) ] # 전체 거리
timetable = [-INF for _ in range(V)] # 요구르트 아주머니 방문 시간

route =  list(map(int,input().split()))
route = [ x-1 for x in route ]

# 요구르트 아주머니 방문 경로에 포함되는 node들 다이스트라 수행
for i in range(len(route)-1):
  if not visited[route[i]]:
    dist[route[i]] = dijkstra(route[i])
    visited[route[i]] = True

# 요구르트 아주머니 예상 방문 시간
nowTime = 0
timetable [route[0]] = nowTime
Now,Next = 0,1
while Next<10:
  # 연결되어 있을 때
  if dist[route[Now]][route[Next]] != INF:
    nowTime = nowTime + dist[route[Now]][route[Next]]
    timetable[route[Next]] = max( timetable[route[Next]],nowTime)
    Now = Next
  Next = Next + 1

# 나의 위치에서 다이스트라 수행
myPos = int(input()) - 1
if not visited[myPos]:
  dist[myPos] = dijkstra(myPos)

ans = -1
for i in range(V):
  # 갈수 있는 곳이고, 내가 도착할 수 있는 시간이 요구르트 아주머니보다 같거나 빠른 경우 
  if dist[myPos][i] != INF and dist[myPos][i] <= timetable[i]:
    ans = i+1
    break

print(ans)