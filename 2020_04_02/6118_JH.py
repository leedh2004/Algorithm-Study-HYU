import collections   #출력초과 떴었는데, 디버깅 코드 안지우고 올렸었음 ㅋ;; ㅋㅋㅋ!!!!
N, M = map(int,input().split())
g = dict()
for i in range(N):               #4~10 그래프 dict구조로 만들기
    g[i+1] = list()

for j in range(M):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

def bfs():
    global N
    global M
    q = collections.deque()
    q.append(1)
    visit = [False]*(N+1)
    visit[1] = True
    result1 = 20001  #헛간들 중 가장 작은 수
    result2 = -1 #헛간까지의 거리는 ?
    result3 = 0 #같은 헛간이 몇개 ?
    while q:
        result1 = 20001
        result2 += 1
        result3 = len(q)
        for i in range(result3): 
            t = q.popleft()
            result1 = min(result1,t)  #해당 단계 헛간의 가장 작은 수를 저장
            for j in g[t]:
                if visit[j] == False:
                    q.append(j)
                    visit[j] = True
    print(result1,result2,result3)

bfs()