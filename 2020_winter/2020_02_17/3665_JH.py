import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

tmp_result = []

def topologicalSort():
    global next_node, indegree, result, N
    q = deque()

    for i in range(N) :
        if indegree[i] == 0 :
            indegree[i] = -1
            q.append(i)

    for _ in range(N):
        if not q :
            return 0
        if len(q) > 1 :
            return 2
        t = q.popleft()
        result.append(t+1)
        for i in next_node[t] :
            indegree[i] -=1 
            if indegree[i] == 0 :
                indegree[i] = -1 
                q.append(i)

    return True

for t in range(T):
    N = int(input())
    last_year = list(map(int, input().split()))
    next_node = [[] for _ in range(N)]
    indegree = [0 for _ in range(N)]
    result = []

    for i in range(N):
        indegree[last_year[i]-1] = i
        for j in range(i+1,N,1):
            next_node[last_year[i]-1].append(last_year[j]-1)
    # print(indegree, next_node)

    M = int(input())
    impossible_flag = False
    for i in range(M):
        a,b = map(int,input().split())
        a,b = a-1, b-1
        
        flag = True
        for i in next_node[a] :
            if i == b :  # a b 로 들어왔으면 원래 b가 a보다 앞의 등수이다 따라서 b의 인접노드에 a가 있으면 모순
                flag = False
                indegree[a], indegree[b] = indegree[a]+1, indegree[b]-1
                next_node[a].remove(b)
                next_node[b].append(a)
        if flag :
            # print(a,b)
            indegree[a], indegree[b] = indegree[a]-1, indegree[b]+1
            next_node[b].remove(a)
            next_node[a].append(b)

    # print(indegree, next_node)
    ret = topologicalSort()
    if ret == 0 :
        print('IMPOSSIBLE')
    elif ret == 2 :
        print('?')
        # tmp_result.append('?')
    else :
        print(*result)
        # tmp_result.append(result)

        
# print(tmp_result)
