import sys
import itertools

N = int(sys.stdin.readline())
player =[0]*N
for i in range(N):
    player[i] = i
player = set(player)
S = [[0]*(N) for _ in range(N)]

for i in range(N):
    S[i] = list(map(int,sys.stdin.readline().split()))
team = list(itertools.combinations(player,N//2))

minimum = 20000000

for i in range(len(team)):
    score_1 = 0
    score_2 = 0
    case = team[i]
    opponent = player.difference(case)
    #team = list(set(team) - opponent)
    comb = list(itertools.combinations(case,2))
    for j in range(len(comb)):
        score_1 += S[comb[j][0]][comb[j][1]]
        score_1 += S[comb[j][1]][comb[j][0]]
    comb_2 = list(itertools.combinations(opponent,2))
    for j in range(len(comb_2)):
        score_2 += S[comb_2[j][0]][comb_2[j][1]]
        score_2 += S[comb_2[j][1]][comb_2[j][0]]
    if score_2 > score_1:
        tmp = score_2 - score_1
    else:
        tmp = score_1 - score_2

    if minimum > tmp:
        minimum = tmp

print(minimum)

    
    
    
