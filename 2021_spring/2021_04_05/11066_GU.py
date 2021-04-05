import sys

INF = sys.maxsize

T = int(sys.stdin.readline())
for _ in range(T):
    K = int(sys.stdin.readline())
    chapters = list(map(int, sys.stdin.readline().split()))
    prefix_sum = [0 for i in range(K+1)]
    for i in range(1, K+1):
        prefix_sum[i] = prefix_sum[i-1] + chapters[i-1]
    d = [[0 for i in range(K+1)] for j in range(K+1)]
    for dist in range(1, K+1):
        for start in range(1, K+1):
            if start + dist > K:
                break

            end = start + dist
            d[start][end] = INF

            for mid in range(start, end):
                d[start][end] = min(d[start][end], d[start][mid] +
                                    d[mid+1][end] + prefix_sum[end] - prefix_sum[start-1])

    print(d[1][K])
