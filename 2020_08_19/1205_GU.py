import sys

N,S,P = map(int,sys.stdin.readline().split())
#둘째 줄은 N>0일 때만 주어진다
if N == 0: print(1)
else:
    #S 넣고 다시 sort역순
    scores = list(map(int,sys.stdin.readline().split()))
    scores.append(S)
    scores.sort(reverse = True)
    idx = scores.index(S)
    cnt = scores.count(S)
    #같은 점수 시에 가장 낮은 점수로 채택 되므로 +cnt
    if idx + cnt > P: print(-1)
    else: print(idx+1)

            