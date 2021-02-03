import collections

N, M = map(int,input().split())
indegree = [0 for _ in range(N)]
edge = [[] for _ in range(N)]
result = list()


for i in range(M):
    s,t = map(int,input().split())
    indegree[s-1] += 1     #indegree는 해당 node로 들어오는 (해당 사람보다 뒤에 서야하는) 수
    edge[t-1].append(s-1)  #edge는 index의 노드에서 어느 노드로 갈 수 있는지 번호 저장

q = collections.deque()

for i in range(N):
    if( indegree[i] == 0 ):
        indegree[i] = -1
        q.append(i)

while q :
    node = q.popleft()
    result.insert(0,(node+1))
    for i in edge[node]:
        indegree[i] -= 1
    for i in range(N):
        if( indegree[i] == 0 ):
            indegree[i] = -1
            q.append(i)

result = map(str,result)
print(" ".join(result))