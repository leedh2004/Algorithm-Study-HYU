T = int(input())

for i in range(T) :
    N = int(input())
    dp = [ [0 for _ in range(N+1)] for i in range(2)]
    mat = list()
    result = -1

    for j in range(2):
        tmp_l =  list(map(int, input().split()))
        mat.append(tmp_l)
    
    dp[0][1] = mat[0][0]
    dp[1][1] = mat[1][0]

    for j in range(2,N+1,1):
        dp[0][j] = max( dp[1][j-1], dp[1][j-2]  ) + mat[0][j-1]
        dp[1][j] = max( dp[0][j-1], dp[0][j-2]  ) + mat[1][j-1]
        result  = max(dp[0][j], dp[1][j], result)

    print(result)