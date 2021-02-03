from heapq import heappush, heappop
import sys

INF = sys.maxsize
input = sys.stdin.readline

def dij():
    dist, q = [INF] * (n+1), []
    heappush(q, [0,c])
    dist[c] = 0
    # 감염된 컴퓨터 세아리기(중복 없이)
    computers = []
    while q:
        t, cur = heappop(q)
        computers.append(cur)
        if dist[cur] < t: continue
        cur_link = dependence[cur]
        for i in range(len(cur_link)):
            s,a = cur_link[i]
            if dist[a] > t + s:
                dist[a] = t + s
                heappush(q,[dist[a],a])
    computers = list(set(computers))
    maximum = 0
    #INF -> 감염 X, maximum -> 마지막 컴퓨터 감염
    for i in range(1,n+1):
        if dist[i] != INF and dist[i] > maximum:
            maximum = dist[i]
    print(len(computers),maximum)

T = int(input())
for i in range(T):
    n,d,c = map(int,input().split())
    dependence = [[] for _ in range(n+1)]
    for j in range(d):
        a,b,s = map(int,input().split())
        dependence[b].append([s,a])
    dij()

""" 시간 초과
from heapq import heappush, heappop
import sys

INF = sys.maxsize
input = sys.stdin.readline

def dij():
    dist, q = [INF] * (n+1), []
    heappush(q, [0,c])
    dist[c] = 0
    computers = []
    while q:
        t, cur = heappop(q)
        computers.append(cur)
        if dist[cur] < t: continue
        cur_link = []
        for i in range(d):
            if dependence[i][1] == cur:
                cur_link.append(dependence[i])
            elif dependence[i][1] > cur:
                break
        for i in range(len(cur_link)):
            A,B,C = cur_link[i]
            #if dist[A] > dist[B] + C:
            #    dist[A] = dist[B] + C
            #    heappush(q,[dist[A],A])
            if dist[A] > t + C:
                dist[A] = t + C
                heappush(q,[dist[A],A])
    computers = list(set(computers))
    maximum = 0
    for i in range(1,n+1):
        if dist[i] != INF and dist[i] > maximum:
            maximum = dist[i]
    print(len(computers),maximum)

T = int(input())
for i in range(T):
    n,d,c = map(int,input().split())
    dependence = [list(map(int,input().split())) for _ in range(d)]
    dependence.sort(key = lambda x:x[1])
    dij()
"""
