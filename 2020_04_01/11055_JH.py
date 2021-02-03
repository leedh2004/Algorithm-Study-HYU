N = int(input())
A = list(map(int,input().split()))
dp = list() #dp테이블, 예제꺼는 [1,101,3,53,113,6....] 이렇게 들어갈꺼임
L = len(A)
result = -1
for i in range(L) :
    tmp = 0
    for j in range(i,-1,-1): #dp 테이블을 왼쪽으로 읽어가면서 A[j]가 본인보다 작은거(내가 그 부분에 이어 붙일 수 있는거) 찾음, 그중 가장 큰거 찾으면 성공
        if A[j]<A[i]:
            tmp = max(tmp,dp[j])
    dp.append(tmp+A[i])   #지금 내 숫자를 포함 하는 부분 순열의 모든 원소 합
    result = max(result,tmp+A[i]) #나중에 dp 테이블 다시 읽으면 손해니까 최대값 항상 저장하고 있기

print(result)