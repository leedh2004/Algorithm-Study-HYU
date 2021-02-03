import sys
input = sys.stdin.readline
N = int(input())
left, right = map(int, input().split())
result = right-left

for i in range(N-1):
    x,y = map(int,input().split())
    if x >=left :
        if x <= right :
            if y <= right :
                continue
            elif y > right :
                result += (y-right)
                right = y
        if x > right :
            result += (y-x)
            left, right = x, y

print(result)