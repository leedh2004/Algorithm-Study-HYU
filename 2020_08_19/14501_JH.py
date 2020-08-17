#Using python
'''
    하루에 상담은 1개만
    N+1일에 퇴사라면 N+1일에 상담할 수 없음, N일에는 1일짜리 상담만 가능
    첫번째 줄에는 N이 주어지고 그다음줄부터 상담일수, 가격이 주어질거임
'''

'''
    상담일수가 N+1 - n 보다 크다면 상담 할 수 없음
    상담이 끝나는 날짜는 상담시작일 + 상담일수 - 1 
    최대가격 넣을 변수, 현재 탐색하는 가격을 넣을 변수
'''

if __name__ == '__main__' :
    consult = list()
    dp = list()

    max_money = 0

    N = int(input())

    for i in range(N) : # (일자, 소요시간, 돈)으로 저장
        day_consult = tuple((i+1,*tuple(map(int,input().split()))))
        consult.append(day_consult)
        dp.append(day_consult)
    dp.append((N+1,0,0))

    for j in range(N-1,-1,-1) :
        if consult[j][1] >= (N+1-j) : #애초에 불가능한 상담은 그냥 넘어가기
            dp[j] = (j+1,0,max(0,dp[j+1][2]))
            continue
        max_money = max(consult[j][2]+dp[j+consult[j][1]][2],max_money)
        dp[j] = (j+1,0,max_money)
    
    print(max_money)
    


