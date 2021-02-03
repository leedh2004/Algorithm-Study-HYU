import sys
input = sys.stdin.readline

N, M = map(int,input().split())
criteria = list()
check = set()

for i in range(N):
    n, p = input().split()
    if p not in check :
        check.add(p)
        criteria.append([n, int(p)])
last_index = len(criteria)-1

for i in range(M):
    t = int(input())
    left,right = 0, last_index

    while left <= right :
        mid = (left+right)//2
        if criteria[mid][1] < t :
            left = mid+1
        else :
            right = mid-1
    print(criteria[right+1][0])