import sys
input = sys.stdin.readline

N = int(input())

ME, OTHER = "me", "other"
DP = [0 for _ in range(1001)]
DP[1],DP[2],DP[3], DP[4] = ME, OTHER, ME, ME
dol = [1,3,4]
turn = 0

class Win(Exception):
    def __init__(self):
        super().__init__('내가 이겼음')

for i in range(N+1):
    try :
        for d in dol :
            if DP[i-d] == OTHER:
                DP[i] = ME
                raise Win
    except Win :
        continue
    
    DP[i] = OTHER
    
if DP[N] == ME:
    print('SK')
else :
    print('CY')


