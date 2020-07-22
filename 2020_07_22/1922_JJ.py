from heapq import *

#집합 대표 찾기
def find(a):
    if parent[a] == a:
        return a
    else :
        return find(parent[a])

def merge(a,b):
    a_p = find(a)
    b_p = find(b)
    parent[a_p] = b_p

#입력
n = int(input())
m = int(input())
valid_edge = 0
parent = [ i for i in range(n)]
edge = []
total_cost = 0
for _ in range(m):
    a,b,c = map(int, input().split())
    heappush(edge, (c, a-1,b-1))


while valid_edge!=n-1:
    tmp = heappop(edge)
    a_p = find(tmp[1])
    b_p = find(tmp[2])
    if a_p!=b_p:
        merge(a_p,b_p)
        valid_edge = valid_edge + 1
        total_cost = total_cost + tmp[0]

print(total_cost)



