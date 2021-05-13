import sys

input = sys.stdin.readline

n = None
card = None
dp = None
def recur(lIdx, rIdx, turn):

    if lIdx==rIdx:
        if turn:
            return card[lIdx]
        else :
            return 0
    if dp[int(turn)][lIdx][rIdx] != -1:
        return dp[int(turn)][lIdx][rIdx]
    
    ret = None
    if turn:
        ret = max(recur(lIdx+1,rIdx,not turn)+card[lIdx], recur(lIdx,rIdx-1,not turn)+card[rIdx])
    else :
        ret = min(recur(lIdx+1,rIdx,not turn), recur(lIdx,rIdx-1,not turn) )
    
    dp[int(turn)][lIdx][rIdx] = ret
    return ret


t = int(input())
for _ in range(t):
    n = int(input())
    card = list(map(int,input().split()))
    dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(2)]
    print(recur(0,n-1,True))
