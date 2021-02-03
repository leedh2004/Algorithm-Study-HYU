import sys

# 입력
n,start,end,m = map(int,sys.stdin.readline().split())
edges = []
for i in range(m):
  st,ed, cost = map(int,sys.stdin.readline().split())
  edges.append([st,ed,-cost])
money = list(map(int,sys.stdin.readline().split()))

# 거리 배열
MIN_INF = -1000000001
dist = [MIN_INF for _ in range(n)]
MAX_INF = 1000000001

# 벨만포드 알고리즘
dist[start] = money[start]

# 노드 최대 갯수가 100개 이기 때문에 + 100
for i in range(n+100):
  for edge in edges:
    st,ed,cost = edge[0],edge[1],edge[2]

    # 연결이 안되어 있다면 갱신 할 수 없으니깐 건너뜀
    if dist[st] == MIN_INF:
      continue
    
    # 무한대로 증가하는 경우
    elif dist[st] == MAX_INF:
      dist[ed] = MAX_INF
    
    # 갱신
    elif dist[ed] < dist[st] + cost + money[ed]:
      dist[ed] = dist[st] + cost + money[ed]

      # + 무한대 사이클이랑 연결된 노드랑 연결된 노드는 전부 무한대가 된다.
      if i>n:
        dist[ed] = MAX_INF

if dist[end] ==  MAX_INF:
  print('Gee')
elif dist[end] == MIN_INF:
  print('gg')
else :
  print(dist[end])