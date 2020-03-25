import queue

N,M,V = map(int, input().split())
node = [[0]*(N+1) for _ in range(N+1)]
print(node)
for i in range(M):
    x,y = map(int, input().split())
    node[x][y] = 1
    node[y][x] = 1
visit = [False]*(N+1)
visit2 = [False]*(N+1)

def dfs(start):
    visit[start] = True
    print(start, end = ' ')
    for i in range(1,N+1,1) : 
        if node[start][i] == 1 and visit[i] == False:
            dfs(i)

def bfs(start):
    q = queue.Queue()
    q.put(start)
    visit2[start] = True

    while not q.empty():
        target = q.get()
        print(target, end = ' ')

        for i in range(1,N+1,1):
            if node[target][i] == 1 and visit2[i] == False:
                visit2[i] = True
                q.put(i)

dfs(V)
print()
bfs(V)
















# 왜 런타임 에러 뜨는지 모르겠음, 검색도 많이 해보고 백준에 있는 질문탭에서 반례도 많이 해봤는데 다 됌 ;;
# import queue         
# import sys
# sys.setrecursionlimit(100000)
# result = list()
# result2 = list()

# def dfs(start, T, visit):
#     global result
#     visit[start-1] = True
#     result.append(start)
#     if not T.get(start) :
#         return
#     for i in T.get(start):
#         if visit[i-1] == False:
#             dfs(i,T,visit)

# def bfs(T,N,start):
#     global result2
#     visit = [False] * N
#     visit[start-1] = True
#     q = queue.Queue()
#     q.put(start)

#     while not q.empty():
#         target = q.get()
#         result2.append(target)

#         for i in T.get(target):
#             if visit[i-1] == False :
#                 visit[i-1] = True
#                 q.put(i)




# if __name__ == '__main__' :
#     N, M, V = map(int,input().split()) #정점, 간선, 시작점
#     T = {}
#     T[V] = []  #시작점에 연결된 노드가 없을 때를 대비해서
#     for _ in range(M) :
#         x, y = map(int, input().split())
#         if x not in T :
#             T[x] = []
#         if y not in T :
#             T[y] = []
#         T[x].append(y)
#         T[y].append(x)
            
#     for i in T.keys() :
#         T[i].sort()
#     visit  = [False] * N
#     dfs(V,T,visit)
#     bfs(T,N,V)
    
#     if not T.get(V) :
#         print(V)
#         print(V)
#     else :
#         for _ in range(N) :
#             print(result[_], end = ' ')
#         print()
#         for _ in range(N) :
#             print(result2[_], end = ' ')
    