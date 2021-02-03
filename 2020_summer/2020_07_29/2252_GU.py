import sys
#topological sort
N,M = map(int,sys.stdin.readline().split())
#진입차수
indegree = [0 for _ in range(N+1)]
#dict로 order[i] = j -> i가 j보다 작다
order = dict()
#dictionary 초기화
for i in range(1,N+1):
    order[i] = []
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    indegree[b] += 1
    order[a].append(b)
queue = []
#진입차수 0인 것 queue에 넣기
for i in range(1,N+1):
    if indegree[i] == 0:
        queue.append(i)
while len(queue) != 0:
    k = len(queue)
    for i in range(k):
        q = queue[i]
        connected = order[q]
        #연결 간선 끊기
        for j in range(len(connected)):
            indegree[connected[j]] -= 1
        #한 번 선택된 node 다시 선택 안되도록 -1
        indegree[q] = -1
    while len(queue) != 0:
        print(queue.pop(0), end = " ")
    #indegree 업데이트 후 indegree 0인 것 queue
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)
    

