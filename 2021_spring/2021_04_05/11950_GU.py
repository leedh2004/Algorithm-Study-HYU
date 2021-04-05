import sys
# W B R
N, M = map(int, sys.stdin.readline().split())
S = [[[0, 0, 0] for _ in range(M)] for _ in range(N)]
color = {'W': 0, 'B': 1, 'R': 2}
grid = []
top_bottom = 0
for i in range(N):
    line = list(sys.stdin.readline().rstrip())
    # grid.append(line)
    if i == 0:
        top_bottom += (line.count('B') + line.count('R'))
    elif i == N-1:
        top_bottom += (line.count('W') + line.count('B'))
    else:
        for j in range(M):
            if j == 0:
                S[i][j][color[line[j]]] += 1
            else:
                S[i][j][0] = S[i][j-1][0]
                S[i][j][1] = S[i][j-1][1]
                S[i][j][2] = S[i][j-1][2]
                S[i][j][color[line[j]]] += 1

INF = sys.maxsize

blue_line = [INF for _ in range(N)]
for i in range(1, N-1):
    blue_line[i] = S[i][M-1][0] + S[i][M-1][2]

for j in range(M):
    for i in range(1, N-1):
        S[i][j][0] += S[i-1][j][0]
        S[i][j][1] += S[i-1][j][1]
        S[i][j][2] += S[i-1][j][2]
        # S[i][j][color[grid[i][j]]] += 1

wdp = [0 for _ in range(N)]
wdp[1] = S[1][M-1][1] + S[1][M-1][2] - (S[0][M-1][1] + S[0][M-1][2])
for i in range(1, N):
    tmp_S1 = S[i-1][M-1][1] + S[i-1][M-1][2]
    tmp_S2 = S[i][M-1][1] + S[i][M-1][2]

    wdp[i] = wdp[i-1] + tmp_S2 - tmp_S1

rdp = [0 for _ in range(N)]
rdp[N-2] = S[N-2][M-1][0] + S[N-2][M-1][1] - (S[N-3][M-1][0] + S[N-3][M-1][1])
for i in range(N-3, 0, -1):
    tmp_S1 = S[i-1][M-1][0] + S[i-1][M-1][1]
    tmp_S2 = S[i][M-1][0] + S[i][M-1][1]

    rdp[i] = rdp[i+1] + tmp_S2 - tmp_S1

upper = [0 for _ in range(N)]
if blue_line[1] < wdp[1]:
    upper[1] = blue_line[1]
else:
    upper[1] = wdp[1]

for i in range(2, N-2):
    if upper[i-1] + blue_line[i] < wdp[i]:
        upper[i] = upper[i-1] + blue_line[i]
    else:
        upper[i] = wdp[i]

lower = [0 for _ in range(N)]
if blue_line[N-2] < rdp[N-2]:
    lower[N-2] = blue_line[N-2]
else:
    lower[N-2] = rdp[N-2]

for i in range(N-3, 0, -1):
    if lower[i+1] + blue_line[i] < rdp[i]:
        lower[i] = lower[i+1] + blue_line[i]
    else:
        lower[i] = rdp[i]

ans = INF

for i in range(1, N-1):
    ans = min(ans, top_bottom + (upper[i-1] + blue_line[i] + lower[i+1]))
print(ans)
