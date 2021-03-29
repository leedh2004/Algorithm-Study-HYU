import sys

# 2개 묶을 수 있다 최대?
# 음수 / 0 / 양수
# 음수 * 음수 = 양수

# 1과 2는 곱하는 것보다 더하는게 크다 !!!!!!!!!!

N = int(sys.stdin.readline())
num_list = []
positive = 0
zeros = 0
negative = 0

for _ in range(N):
    tmp = int(sys.stdin.readline())
    if tmp > 0:
        positive += 1
    elif tmp < 0:
        negative += 1
    num_list.append(tmp)

num_list.sort()
zeros = N - negative - positive
ans = 0

if negative > 0:
    if negative > 1:
        # 두 쌍 씩
        for i in range(0, negative-1, 2):
            ans += (num_list[i] * num_list[i+1])
        # 하나 남은 경우
        if negative % 2 != 0:
            if zeros == 0:
                ans += num_list[negative-1]
    # 음수 1개
    else:
        if zeros == 0:
            ans += num_list[0]


if positive > 0:
    if positive % 2 != 0:
        ans += num_list[negative+zeros]
        for i in range(negative+zeros+1, N-1, 2):
            # 1과 2는 곱하는 것보다 더하는게 더 크다
            # 1, x는 곱하는 것보다 더하는게 더 크다
            if num_list[i] == 1:
                ans += (num_list[i]+num_list[i+1])
            else:
                ans += (num_list[i] * num_list[i+1])
    else:
        for i in range(negative+zeros, N-1, 2):
            # 1과 2는 곱하는 것보다 더하는게 더 크다
            # 1, x는 곱하는 것보다 더하는게 더 크다
            if num_list[i] == 1:
                ans += (num_list[i]+num_list[i+1])
            else:
                ans += (num_list[i] * num_list[i+1])

print(ans)
