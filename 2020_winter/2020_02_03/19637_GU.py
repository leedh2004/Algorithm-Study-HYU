import sys


# def check(power):
#     for i in range(length):
#         if power <= powers[i]:
#             return titles[i]

#     return titles[-1]


def check(power):
    l = 0
    r = length
    mid = (l+r)//2

    if power <= powers[0]:
        return titles[0]

    if length == 1:
        return titles[1]

    while l < r:
        mid = (l+r)//2

        if r-l == 1:
            if power <= powers[l]:
                return titles[l]
            else:
                return titles[r]

        if powers[mid] < power:
            l = mid
        elif powers[mid-1] < power <= powers[mid]:
            return titles[mid]
        else:
            r = mid

    return titles[mid]


N, M = map(int, sys.stdin.readline().split())
titles = []
powers = []
before = -1
for i in range(N):
    name, power = sys.stdin.readline().split()
    if i == 0:
        before = int(power)
        titles.append(name)
        powers.append(int(power))
    else:
        if int(power) == int(before):
            continue
        else:
            before = int(power)
            titles.append(name)
            powers.append(int(power))

length = len(powers)-1

for i in range(M):
    print(check(int(sys.stdin.readline())))
