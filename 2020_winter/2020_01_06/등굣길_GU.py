def solution(m, n, puddles):
    answer = 0
    dx = [0,1]
    dy = [1,0]
    q = [[1,1]]
    visited = [[0]*(m+1) for _ in range(n+1)]
    for i in range(len(puddles)):
        x,y = puddles[i]
        #puddles[i] = [y,x]
        visited[y][x] = -1
    while q:
        y,x = q.pop(0)
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if ny < n+1 and nx < m+1:
                if visited[ny][nx] != -1:
                    visited[ny][nx] = (visited[ny][nx] + 1) % 1000000007
                    q.append([ny,nx])

    return visited[n][m]

m,n = map(int,input().split())
puddles = [[2,2]]
print(solution(m,n,puddles))