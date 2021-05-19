ans = 0
N = int(input())
P = list(map(int, input().split()))
C = [ [] for _ in range(N)]
D = int(input())

for i in range(N):
    if i == D:
        continue
    if P[i] != -1:
        C[P[i]].append(i)

rootIdx = P.index(-1)

def dfs(here):
    # global ans, D
    # 왜 global 없으면 안댐?
    if len(C[here]) == 0:
        ans += 1
        return
    for c in C[here]:
        dfs(c)

if __name__ == '__main__':
    if D == rootIdx:
        print(0)
    else:
        dfs(rootIdx)
        print(ans)