import sys

N,M= map(int,sys.stdin.readline().split())
days =[]
for i in range(N):
    days.append(int(sys.stdin.readline()))

#sort를 해서 계속 틀렸었다
#days.sort()
#print(days)

#left - K원 충전하고 하루치 못내는건 말이 안됨 -> max
left = max(days)
#right - M이 1인 경우 모든 돈을 한번 뽑은 상태로 낼 수 있어야함
right = sum(days)
res = right
#mid가 K를 의미, 조건을 만족하는 최소의 mid 탐색(이분탐색)
while(left <= right):
    #처음 한번 인출 cnt = 1
    cnt = 1
    mid = (left + right) // 2
    money = mid
    for i in range(N):
        # 가지고 있는 돈 > 오늘 쓸 돈
        if money >= days[i]:
            money -= days[i]
        # 새로 인출
        else:
            cnt += 1
            money = mid
            money -= days[i]
    if cnt <= M:
        res = min(res,mid)
        right = mid - 1
    else:
        left = mid + 1
print(res)
