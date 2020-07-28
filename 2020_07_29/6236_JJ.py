import sys

#재귀
def get_ans(start , end):
    
    # 정답찾은경우
    if start == end:
        return start

    #중간값
    mid = (start+end) // 2

    #현재 금액
    now_money = 0

    #뽑기횟수
    now_m = 0


    for c in cost:
        #뽑는 값이 cost값보다 낮은경우 - 절대성립불가
        if c>mid:
            return get_ans(mid+1,end)

        if now_money < c:
            now_money = mid
            now_m = now_m + 1

            #뽑는횟수가 더 많이 필요한경우 - 더 높은 금액을 뽑아야 한다.
            if now_m>m:
                return get_ans(mid+1,end)
        
        now_money = now_money - c

    # 뽑는 횟수는 만족하는 경우 - 더 낮은 금액을 찾아야한다.
    return get_ans(start,mid)

n,m = map(int,sys.stdin.readline().split())
cost = []
for i in range(n):
    cost.append(int(sys.stdin.readline()))

print(get_ans(0,100000))

