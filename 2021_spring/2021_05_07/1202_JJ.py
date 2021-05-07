import sys 
import heapq

input = sys.stdin.readline

n,k = map(int,input().split())

bosuks = []
bag = []

# 보석 정보
for idx in range(n):
    m,v = map(int,input().split())
    heapq.heappush(bosuks,[m,v])

# 가방 정보
for _ in range(k):
    bag.append(int(input()))

# 큰 작은 부터
bag = sorted(bag)

ans = 0
pq = []

for c in bag:

    # 가능한 보석들
    while bosuks:

        # top 확인
        if bosuks[0][0] > c:
            break

        m,v =  heapq.heappop(bosuks)
        heapq.heappush(pq,-v)
    

    if pq:
        v =  - heapq.heappop(pq)
        ans = ans + v

print(ans)


