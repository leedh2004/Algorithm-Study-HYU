import sys
# 낮은건 낮은것끼리 높은건 높은것끼리
# 높은 건 나중에 해야 이기고 올라온 것이랑 하므로 차이가 적다
# 순위 낮은게 나중에한다 -> 더 높은 값이랑 붙는다 -> 차이가 커진다.
# 그러므로 순위 낮은 것부터 greedy
N = int(sys.stdin.readline())
ranks = list(map(int,sys.stdin.readline().split()))

ans = 0
for i in range(N-1):
    low = max(ranks)
    idx = ranks.index(low)
    gap1 = 9999
    gap2 = 9999
    if idx-1 >=0:
        gap1 = low - ranks[idx-1]
    if idx+1 < len(ranks):
        gap2 = low - ranks[idx+1]
    # low가 가장 큰 값이므로 gap1 == gap2가 될 수 없음
    if gap1 < gap2:
        ans += gap1
        ranks.pop(idx)
    else:
        ans += gap2
        ranks.pop(idx)
print(ans)
    
            
###########################
""" 
순위 사이의 gap들을 계산, gap이 가장 작은 것부터 붙도록, 후에 gap 갱신
이렇게 하면 1,2,3 일때 최솟값인 2가 나오지 않고 3이나온다(반례) but 3,2,1 하면 2나옴.
(+ ~~ 4,5,6 ~~ 3,2,1 ~~ 인 경우 등 생각하면 더 복잡해짐)
import sys

N = int(sys.stdin.readline())
ranks = list(map(int,sys.stdin.readline().split()))
gaps = []
for i in range(len(ranks)-1):
    gaps.append(abs(ranks[i+1]-ranks[i]))
ans = 0
for i in range(N-1):
    minimum = min(gaps)
    ans += minimum
    min_idx = gaps.index(minimum)

    if ranks[min_idx] < ranks[min_idx+1]: 
        higher = min_idx +1
        lower = min_idx
    else: 
        higher = min_idx
        lower = min_idx + 1

    if min_idx-1 >=0 :
        gaps[min_idx-1] = abs(ranks[min_idx-1] - ranks[lower])
    if min_idx+2 < len(ranks):
        gaps[min_idx] = abs(ranks[lower] - ranks[min_idx+2])
    
    if min_idx + 1 < len(gaps):
        gaps.pop(min_idx+1)
    else:
        gaps.pop(min_idx)

    #탈락
    ranks.pop(higher)
    print('ranks= ' + str(ranks))
    print('gaps= ' + str(gaps))
print(ans)"""