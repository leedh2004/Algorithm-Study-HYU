from itertools import combinations

def dis(home, chi):
    x1,y1 = home[0], home[1]
    x2, y2 = chi[0], chi[1]
    ret = abs(x1-x2) + abs(y1-y2)
    return ret

N, M = map(int,input().split())
mat = [ list(map(int,input().split())) for _ in range(N) ]
home = []
chi = []
result = 1e9

for i in range(N): #mat을 돌며 집과 치킨집 위치 저장하기
    for j in range(N):
        if mat[i][j] == 1 :
            home.append([i,j])
        elif mat[i][j] == 2 :
            chi.append([i,j])

com_chi = list(combinations(chi,M))
home_len = len(home)
for i in range(len(com_chi)): #치킨집을 M개로 묶은 조합의 경우의 수만큼
    tmp = [ 1e9 for _ in range(home_len) ]
    for j in range(M): #M개로 묶인 치킨집 중에서 각각마다 거리를 계산해줌
        for k in range(home_len): #각 치킨집마다 모든 집에서의 거리를 구하기 위해
            tmp[k] = min(tmp[k],dis(home[k],com_chi[i][j]))
    result = min(result, sum(tmp))
print(result)