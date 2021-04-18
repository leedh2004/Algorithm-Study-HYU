import sys
input = sys.stdin.readline

N1, N2 = map(int, input().strip().split())
L1, L2 = [
    {'group': 1, 'name': ant} for ant in input().strip()][::-1], 
    [{'group': 2, 'name': ant} for ant in input().strip()]
print(L1)
ants = L1+L2
T = int(input())

for _ in range(T):
    i = 0
    while i < len(ants) -1 :
        if ants[i]['group'] < ants[i+1]['group']:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 1
        i += 1

print("".join([ant['name'] for ant in ants]))