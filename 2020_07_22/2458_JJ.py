n,m = map(int,input().split())
d = [[False]*n for _ in range(n)]
#print(d)
for _ in range(m):
    a,b =  map(int,input().split())
    d[a-1][b-1] = True

for i in range(n):
    for j in range(n):
        for k in range(n):
            if d[j][i] and d[i][k] :
                d[j][k] = True

ans = 0

#거리가 정립이 안된 노드가 하나라도 있으면 위치를 모름
for i in range(n):
    flag = True
    for j in range(n):
        if i==j:
            continue
        #정립안된경우
        if  not (d[i][j]  or d[j][i]) :
            flag = False
            break
    if flag:
        ans = ans+1
print(ans)



