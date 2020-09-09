import sys     #왜 런타임 오류 나는지 모르겠습니다...
sys.setrecursionlimit(25000)
def dfs(t):
    global result
    for i in range(N):
        while adj[t][i] :
            adj[t][i] -= 1
            adj[i][t] -= 1
            dfs(i)
    print(t+1, end = " ")
    # result.append(t+1)


N = int(input())
adj = [ list(map(int,input().split())) for _ in range(N) ]
flag = False
s = [0 for _ in range(N)]
result = []

# for i in range(N):
#     if(sum(adj[i])%2 == 1 ):
#         flag = True
#         break


for i in range(N):
    for j in range(N):
        s[i] += adj[i][j]
    if s[i]%2 == 1 :
        flag = True
        break
        


if flag :
    print(-1)
else :
    dfs(0)
    # print(*result[::-1])
    # for i in result[::-1]:
    #     print(i, end = " ")
    # result.reverse()
    # print(*result)