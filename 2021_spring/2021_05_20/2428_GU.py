import sys


def get_idx(start, left, right):

    while left < right:
        mid = (left+right) // 2
        if Fs[mid]*0.9 <= Fs[start]:
            left = mid + 1
        else:
            right = mid
    return right - 1


N = int(sys.stdin.readline())
Fs = sorted(list(map(int, sys.stdin.readline().split())))
ans = 0
for i in range(N-1):
    ans += get_idx(i, i, N) - i
print(ans)


# import sys
# from bisect import bisect_right

# N = int(sys.stdin.readline())
# Fs = sorted(list(map(int, sys.stdin.readline().split())))
# Fs2 = [0.9*i for i in Fs]
# ans = 0
# for i in range(N-1):
#     ans += bisect_right(Fs[i+1:], Fs[i])
# print(ans)

# s, e = 0, 1
# res = 0
# while True:
#     if s == N-1:
#         break
#     if s == e and e < N-1:
#         e += 1
#     if Fs[e]*0.9 <= Fs[s] and e < N-1:
#         e += 1
#     else:
#         res += (e-s)
#         s += 1
# print(res)
