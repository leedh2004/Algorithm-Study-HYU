import sys

N = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))
L.insert(0,0)
J = list(map(int,sys.stdin.readline().split()))
J.insert(0,0)

d = [[0]*100 for _ in range(N+1)]
# i 로 N명 순회하며 선택할지 안할지 
for i in range(1,N+1):
    for j in range(1,100):
        # 체력 제한보다 i번째 아이의 체력 소모양이 클 경우 -> i번째 아이 선택 X 경우 받음
        if L[i] > j:
            d[i][j] = d[i-1][j]
        # i번째 아이 안녕하는게 나을지 안하는게 나을지 (선택은 가능하나)
        else:
            d[i][j] = max(d[i-1][j],d[i-1][j-L[i]] + J[i])

# j = 100 이면 체력 다소모
print(d[N][99])
