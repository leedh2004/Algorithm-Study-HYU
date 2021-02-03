import sys

input = sys.stdin.readline
T = int(input())
K = int(input())
DP = [[0 for i in range(T+1)] for j in range(K+1)]
coins = []

for i in range(K):
    cost, count = map(int, input().split())
    coins.append([cost, count])

coins.sort()

for k in range(1, T+1, 1):
    for i in range(1, K+1, 1):
        tmp_cost, tmp_count = coins[i-1][0], coins[i-1][1]
        DP[i][k] = DP[i-1][k]
        for j in range(1,tmp_count+1,1):
            now_cost = j*tmp_cost
            if now_cost > k :
                break
            if k-now_cost == 0 :
                DP[i][k] += 1
            if k-now_cost > 0 :
                DP[i][k] += DP[i-1][k-now_cost]

# for line in DP :
#     print(line)
print(DP[K][T])