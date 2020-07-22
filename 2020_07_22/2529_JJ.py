import heapq

def topologicalsort(indegree):
    
    indegree_down = indegree[:]
    indegree_up = indegree[:]
    heap_min = []
    heap_max = []

    #초기 indegree가 0인 노드 heap에 삽입
    for i in range(k+1):
        #최소값은 인덱스가 작은 숫자부터 0,1,2,3,배정해줄 예정
        if indegree_down[i] == 0:
            heapq.heappush(heap_min,i)
            indegree_down[i] = -1
        #최대값은 인덱스가 큰 숫자부터 작아지는 순서로 배정 예정
        if indegree_up[i] == 0:
            heapq.heappush(heap_max,-i)
            indegree_up[i] = -1
    
    #최소값
    q_down = [0]*(k+1)
    cnt = 0

    #힙안에 원소가 존재할 때 
    while len(heap_min) > 0:
        # print(heap_min)
        #음수로 넣었기 때문에, -로 양수로 바꿔준다.
        now = heapq.heappop(heap_min)

        #값 대입
        q_down[now] = cnt

        #갑 증가
        cnt = cnt + 1
        
        #인접 노드 indegree 감소 및 0인경우 힙에 삽입
        for i in range(len(adj[now])):
            next = adj[now][i]
            indegree_down[next] = indegree_down[next] - 1
            if indegree_down[next] == 0:
                heapq.heappush(heap_min,next)
                indegree_down[next] = -1
    
    #최댓값
    q_up = [0]*(k+1)
    cnt = 0

    #힙안에 원소가 존재할 때 
    while len(heap_max) > 0:
        now = -heapq.heappop(heap_max)

        #값 대입
        q_up[now] = cnt

        #갑 증가
        cnt = cnt + 1
        
        #인접 노드 indegree 감소 및 0인경우 힙에 삽입
        for i in range(len(adj[now])):
            next = adj[now][i]
            indegree_up[next] = indegree_up[next] - 1
            if indegree_up[next] == 0:
                heapq.heappush(heap_max,-next)
                indegree_up[next] = -1
        
    return q_down,q_up

k = int(input())

adj = [[] for _ in range(k+1)]
indegree = [0 for _ in range(k+1)]

connect = list(input().split())
for i in range(k):
    if connect[i]=='<':
        adj[i].append(i+1)
        indegree[i+1] = indegree[i+1] + 1
    elif connect[i] == '>':
        adj[i+1].append(i)
        indegree[i] = indegree[i] + 1

down_sorted , up_sorted = topologicalsort(indegree)

ans_min = ""
ans_max = ""

for i in range(k+1):
    ans_max = ans_max + str(up_sorted[i]+9-k)
    ans_min = ans_min + str(down_sorted[i])

print(ans_max)
print(ans_min)


