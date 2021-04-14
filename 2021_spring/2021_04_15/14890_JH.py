N,L = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
result = 0


for i in range(N):
    road = mat[i]
    can = 1
    visit = [False] * N
    for idx in range(N-1):
        if abs(road[idx] - road[idx+1]) >=2 : #높이가 2이상 차이나면 절대 길이 될수 없음
            can = 0
            break
        
        if abs(road[idx]-road[idx+1]) == 1 :
            if road[idx] < road[idx+1]:
                if L == 1 :
                    if visit[idx] == True :
                        can = 0
                        break
                for j in range(L-1):
                    if idx-j-1<0 or visit[idx] == True or visit[idx-j-1] == True or road[idx-j-1] != road[idx]:
                        can = 0
                        break
            if road[idx] > road[idx+1]:
                if L == 1 :
                    visit[idx+1] = True

                for j in range(L-1):
                    if idx+j+2 >=N or road[idx+j+2] != road[idx+1]:
                        can = 0
                        break
                    visit[idx+1] = True
                    visit[idx+j+2] = True

            if can == 0 :
                break

    if can == 1 :
        result += 1

for i in range(N) :
    road = list()
    can = 1
    for j in range(N):
        road.append(mat[j][i])
    visit = [False]*N
    for idx in range(N-1):
        if abs(road[idx] - road[idx+1]) >=2 : #높이가 2이상 차이나면 절대 길이 될수 없음
            can = 0
            break
        
        if abs(road[idx]-road[idx+1]) == 1 :
            if road[idx] < road[idx+1]:
                if L == 1 :
                    if visit[idx] == True :
                        can = 0
                        break
                for j in range(L-1):
                    if idx-j-1<0 or visit[idx] == True or visit[idx-j-1] == True or road[idx-j-1] != road[idx]:
                        can = 0
                        break
            if road[idx] > road[idx+1]:
                if L == 1 :
                    visit[idx+1] = True

                for j in range(L-1):
                    if idx+j+2 >=N or road[idx+j+2] != road[idx+1]:
                        can = 0
                        break
                    visit[idx+1] = True
                    visit[idx+j+2] = True

            if can == 0 :
                break

    if can == 1 :
        result += 1
        
print(result)