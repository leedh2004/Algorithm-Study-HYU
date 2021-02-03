import sys

def find(x):
    if x==parent[x]: return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x!=y:
        # 둘 다 발전소일 때 연결 X
        if x in power_plant and y in power_plant:
            return False
        else:
            # 둘 중 하나 발전소 -> parent = 발전소
            if y in power_plant:
                parent[x] = y
            else:
                parent[y] = x
            return True

input = sys.stdin.readline
N,M,K = map(int,input().split())
parent = [_ for _ in range(N+1)]
power_plant = list(map(int,input().split()))
cables = []
for i in range(M):
    u,v,w = map(int,input().split())
    cables.append([w,u,v])
#Kruskal
cables.sort()
res = 0
cnt = 0
for i in range(M):
    if cnt == N-1:
        break
    w,u,v = cables[i]
    # parent 발전소에 우선순위
    # 둘 다 발전소 -> 함수에서 걸러짐
    # 하나 발전소, 하나 발전소랑 연결된 것 -> 우선순위에 의해 둘 다 parent 발전소 -> 걸러짐
    if find(u)==find(v): continue
    else:
        if(union(u,v)):
            res += w
            cnt += 1
print(res)

    