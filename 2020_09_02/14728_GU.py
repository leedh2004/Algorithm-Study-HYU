import sys

def knapsack():
    d = d = [[0] * (T+1) for _ in range(N+1)]
    # d[i][j] -> 시간 최대 j일 때 i개 선택시 최대 score 
    for i in range(1,N+1):
        for j in range(1,T+1):
            if chapters[i][0] > j: # 시간 최대 j이므로
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = max(d[i-1][j],d[i-1][j-chapters[i][0]] + chapters[i][1])
    return d[N][T]


N,T = map(int,sys.stdin.readline().split())
chapters = [[0,0]]
for i in range(N):
    K,S = list(map(int,sys.stdin.readline().split()))
    chapters.append([K,S])
print(knapsack())



# 한 단원 하나만 넣을 수 있는 것을 간과했다
#####################################
"""
반례 : 2 30 / 5 10 / 10 14 -> 42 (답: 60)
N,T = map(int,sys.stdin.readline().split())
d = [0] * (T+1)
chapters = []
for i in range(N):
    K,S = list(map(int,sys.stdin.readline().split()))
    chapters.append([K,S])
    #d[K] = S
#print(chapters)
chapters.sort()
d[chapters[0][0]] = chapters[0][1]
for i in range(chapters[0][0]+1,T+1):
    for j in range(len(chapters)):
        if i-chapters[j][0] >= 0:
            d[i] = max(d[i-1], d[i-chapters[j][0]] + chapters[j][1])
#print(d)
print(d[T])
"""