import sys
from collections import deque
input = sys.stdin.readline

def check(start):
    global dis, visit, ec
    visit[start] = True
    if start == ec :
        return True

    for c,e in dis[start]:
        if visit[e] == False and check(e) :
            return True
    return False
        
# def check(start):
#     global dis, visit, ec
#     visit[start] = True
#     q = deque()
#     q.append(start)

#     while q :
#         for i in range(len(q)):
#             t = q.popleft()
#             if t == ec :
#                 return True
#             for c,e in dis[t]:
#                 if visit[e] == False :
#                     q.append(e)
#                     visit[e] = True
#     return False


N, sc, ec, M = map(int, input().split())
dis = { i:[] for i in range(N) }
for i in range(M):
    s,e,c = map(int,input().split())
    dis[s].append([-c,e])
money = list(map(int, input().split()))
INF = -10e20
result = [INF for i in range(N)] 
result[sc] = money[sc]
gee_flag = False
visit = [False for i in range(N)]

for i in range(N):
    for j in range(N):
        if result[j] != INF :
            for c,e in dis[j] :
                if result[e] < result[j] + c + money[e] :
                    if i == N-1 :
                        if not gee_flag :
                            gee_flag = check(e)
                        else :
                            break
                    else :
                        result[e] = result[j]+c+money[e]


if result[ec] == INF :
    print('gg')
elif gee_flag :
    print('Gee')
else :
    print(result[ec])



# 4 0 3 4
# 0 1 0
# 0 3 5
# 1 2 0
# 2 1 0
# 0 5 5 10