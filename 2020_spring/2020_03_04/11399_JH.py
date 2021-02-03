#지금 계산해야 하는 값은 앞에 값 + 내가 걸리는 시간임 -> 따라서 반복되는 앞의 값이 작으면 작을수록 유리
N = int(input())
L = list(map(int,input().split()))
L.sort() #오름차순으로 정렬하여 먼저 실행해야 하는 값일수록 앞으로
result = 0
for i in range(N):
    result += L[i]*(N-i) #i번째 값은 총 계산에서 (N-i)번 계산 됨
print(result)