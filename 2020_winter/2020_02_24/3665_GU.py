import sys


def topological_sort(ranking, changed):
    adj = [[] for _ in range(n+1)]
    in_degrees = [0 for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        adj[ranking[i]].extend(ranking[:i])
        in_degrees[ranking[i]] = n-1 - i
    # print(adj)
    # print(in_degrees)
    for i in range(m):
        # a가 b보다 순위가 높아졌다인줄 (아니다! 둘의 관계가 역전 되었다는것뿐)
        a, b = changed[i]
        if b in adj[a]:
            adj[a].remove(b)
            adj[b].append(a)
            in_degrees[a] += 1
            in_degrees[b] -= 1
        else:
            adj[b].remove(a)
            adj[a].append(b)
            in_degrees[a] -= 1
            in_degrees[b] += 1

    q = []
    result = []

    for i in range(1, n+1):
        if in_degrees[i] == 0:
            q.append(i)

    for i in range(n):
        if not q:
            print("IMPOSSIBLE")
            return []
        if len(q) > 1:
            print("?")
            return []

        cur = q.pop(0)
        result.append(cur)
        for j in range(len(adj[cur])):
            in_degrees[adj[cur][j]] -= 1
            if in_degrees[adj[cur][j]] == 0:
                q.append(adj[cur][j])

        # print(q)

    return result


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    ranking = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    changed = []
    for i in range(m):
        changed.append(list(map(int, sys.stdin.readline().split())))
    res = topological_sort(ranking, changed)

    if res:
        res.reverse()
        for i in range(n):
            if i == n-1:
                print(res[i])
            else:
                print(res[i], end=' ')
