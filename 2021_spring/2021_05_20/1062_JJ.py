import sys
from itertools import combinations

input = sys.stdin.readline

n,k = map(int,input().split())


arr = [ 0 for _ in range(n)]

alphaToBi = {}
val = 1

# 각 알파벳의 비트값 저장
for i in range(26):
    alphaToBi[chr(ord('a')+i)] = val
    val = val << 1

# 전체 알파벳 목록
totalAlpha = set([]);

for i in range(n):
    tmp = input().strip()
    for char in tmp:
        arr[i] = arr[i]|alphaToBi[char]
        totalAlpha.add(char)

if k<5:
    print(0)

else :
    base = ['a','n','t','i','c']

    # 기본 앞뒤 글자 비트값
    baseBit = 0
    for i in base:
        baseBit = baseBit | alphaToBi[i]


    selected = set(base)
    left = list(totalAlpha - selected)
    

    checklist = [['a','n','t','i','c']] if k==5 else ([left] if k-5 >len(left) else list(combinations(left,k-5)))
    ans = 0
    for check in checklist:
        bitSum = baseBit
        for char in check:
            bitSum = bitSum | alphaToBi[char]
        
        nowAns = 0
        for wordBit in arr:
            if bitSum & wordBit == wordBit:
                nowAns = nowAns + 1
        ans = max(ans,nowAns)
    print(ans)

