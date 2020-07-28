t = int(input())

while t>0:
    t=t-1

    n = int(input())
    # 선택안함 /위스티커선택 / 아래스티커선택
    dp = [[0]*3 for _ in range(n)]
    data = []

    row1 = list(map(int , input().split()))
    row2 = list(map(int , input().split()))
    
    for i in range(n):
        data.append([row1[i],row2[i]])

    #print(data,dp)

    #초기값 설정
    dp[0] = [0,data[0][0],data[0][1]]

    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
        dp[i][1] = max(dp[i-1][0],dp[i-1][2]) + data[i][0]
        dp[i][2] = max(dp[i-1][0],dp[i-1][1]) + data[i][1]
    print(max(dp[n-1]))