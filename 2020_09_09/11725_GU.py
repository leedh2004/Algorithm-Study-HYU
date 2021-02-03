import sys
# 재귀를 엄청 많이 써야한다..
sys.setrecursionlimit(10 ** 9)
def dfs(s,check):
    for i in range(len(relation[s])):
        next_ = relation[s][i]
        if not check[next_]:
            parent[next_] = s
            check[next_] = True
            dfs(next_,check)

N = int(sys.stdin.readline())
relation = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)
parent = [0] * (N+1)
check = [False] * (N+1)
check[1] = True
dfs(1,check)
for i in range(2,N+1):
    print(parent[i])

