import sys
import itertools

N,M = map(int,sys.stdin.readline().split())

city = [[0]*51 for _ in range(51)]
house= []
ck =[]
for i in range(N):
    city[i] = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if(city[i][j] == 1):
            house.append((i+1,j+1))
        elif(city[i][j] == 2):
            ck.append((i+1,j+1))

comb = list(itertools.combinations(ck,M))

minimum = 99999
for i in range(len(comb)):
    city_score = 0
    for j in range(len(house)):
        case = []
        for k in range(M):
            chicken = comb[i][k]
            case.append(abs(chicken[0]-house[j][0])+abs(chicken[1]-house[j][1]))
        score = min(case)
        city_score += score
    if minimum > city_score:
        minimum = city_score

print(minimum)
        

