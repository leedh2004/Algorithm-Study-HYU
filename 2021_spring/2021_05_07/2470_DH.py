import sys 

N = int(input())
S = sorted(list(map(int, input().split())))
start, end = 0, len(S) - 1

minSum = sys.maxsize
minVal, maxVal = S[0], S[end]

while start < end:
    s, e = S[start], S[end]
    val = s + e
    if abs(val) < minSum:
        minSum = abs(val)
        minVal, maxVal = s, e
    if val > 0:
        end -= 1
    else:
        start += 1

print(minVal, maxVal)


