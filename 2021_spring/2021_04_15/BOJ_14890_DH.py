def canGo(v, L):
    n = len(v)
    visited = [False for _ in range(n)]
    for i in range(n):
        if i == n - 1:
            return True
        if v[i] == v[i+1]:
            continue
        # 올라가야 하는 경우
        if v[i] + 1 == v[i+1]:
            st = i + 1 - L
            for j in range(st, i+1):
                if j < 0:
                    return False
                if visited[j]:
                    return False
                if v[j] != v[i]:
                    return False
                visited[j] = True
        # 내려가는 경우
        elif v[i] - 1 == v[i+1]:
            ed = i + L
            for j in range(i+1, ed + 1):
                if j >= n:
                    return False
                if visited[j]:
                    return False
                if v[i+1] != v[j]:
                    return False
                visited[j] = True
        else:
            return False

N, L = map(int, input().split())
board = []

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
ret = 0 
# 가로 방향
for i in range(N):
    if canGo(board[i], L):
        ret += 1

for i in range(N):
    v = [ board[j][i] for j in range(N) ]
    if canGo(v, L):
        ret += 1
print(ret)




