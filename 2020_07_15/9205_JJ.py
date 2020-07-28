def get_dis(now_i,next_i):
    return abs(now_i[0] - next_i[0]) + abs(now_i[1]-next_i[1])



def DFS(now_i, visited):
    global positions,n,flag
    
    #도착
    if now_i == n + 1:
        flag = True
    
    #도착했으니 DFS 재귀 전부 중지
    if flag :
        return

    for i in range(n+2):
        #방문되지 않았고 맥주 20병 즉 1000m이내에 있을때
        if visited[i] == 0 and get_dis(positions[now_i],positions[i]) <= 1000:
            visited[i] = 1
            DFS(i,visited)


positions=[]
n = None
flag = False

t = int(input())
while t>0:
    t = t-1
    n = int(input()) 
    flag = False
    positions = []
    visited = [0 for _ in range(n+2)]
    visited[0] = 1
    for i in range(n+2):
        x,y = map(int, input().split())
        positions.append([x,y])

    #print(visited,positions)
    DFS(0,visited)
    if flag:
        print("happy")
    else :
        print("sad")
