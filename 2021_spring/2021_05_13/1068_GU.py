import sys
sys.setrecursionlimit(100000)


def dfs(visited, start):
    visited[start] = True
    if d[start]:
        tmp = 0
        for i in d[start]:
            if i != R and not visited[i]:
                tmp += dfs(visited, i)
            # 이부분 없으면 78퍼에서 틀렸습니다
            # 일직선 case
            if i == R and d[Ps[i]] == [R]:
                return 1
        return tmp
    else:
        return 1


N = int(sys.stdin.readline())
visited = [False for _ in range(N)]
Ps = list(map(int, sys.stdin.readline().split()))
d = {i: [] for i in range(N)}
root = -1
for i in range(N):
    if Ps[i] == -1:
        root = i
        continue
    d[Ps[i]].append(i)
R = int(sys.stdin.readline())
d[R] = []
# 루트 지운 경우
if root == R:
    print(0)
    exit(0)
visited[root] = True
print(dfs(visited, root))
