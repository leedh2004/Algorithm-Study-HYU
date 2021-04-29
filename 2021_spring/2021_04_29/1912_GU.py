import sys

_max = -1001
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
d = [0 for _ in range(N+1)]
for i in range(1, N+1):
    # nums i번째보다 누적합이 작으면 고려할 필요 없음
    d[i] = max(d[i-1]+nums[i-1], nums[i-1])
    # 현재까지 누적합 중 최대
    _max = max(_max, d[i])
print(_max)

"""
INF = sys.maxsize
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.insert(0, 0)
prefix_sum = [[0, INF] for _ in range(N+1)]
prefix_sum[1][0], prefix_sum[1][1] = nums[1], nums[1]
_min = INF
for i in range(2, N+1):
    prefix_sum[i][0] = prefix_sum[i-1][0] + nums[i]
    _min = min(_min, prefix_sum[i][0])
    prefix_sum[i][1] = _min
_max = nums[1]
for i in range(2, N+1):
    _max = max(_max, prefix_sum[i][0] - prefix_sum[i-1][1])
print(_max)
"""

"""
INF = sys.maxsize
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums.insert(0, 0)
prefix_sum = [0 for _ in range(N+1)]
prefix_sum[1] = nums[1]
for i in range(2, N+1):
    prefix_sum[i] = prefix_sum[i-1] + nums[i]
d = [-INF for _ in range(N+1)]
d[1] = nums[1]
for i in range(2, N+1):
    d[i] = prefix_sum[i] - min(prefix_sum[:i])
print(max(d))
"""
