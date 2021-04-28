import sys
input = sys.stdin.readline
from collections import defaultdict, deque
from math import floor

N, M, K = map(int,input().strip().split())
fire_balls = deque()
direction = { 0:[-1,0], 1:[-1,1], 2:[0,1], 3:[1,1], 4:[1,0], 5:[1,-1], 6:[0,-1], 7:[-1,-1] }
even_dir = [0,2,4,6]
odd_dir = [1,3,5,7]

# r, c, m, s, d

def move(mat, ball):
    global N, direction
    
    dx, dy = direction[ball[4]]
    nx,ny = (ball[0]+dx*ball[3])%N+1, (ball[1]+dy*ball[3])%N+1

    mat[(nx,ny)].append([ball[2], ball[3], ball[4]])

def merge(mat):
    global fire_balls, even_dir, odd_dir
    
    for (x,y) in mat:
        if len(mat[(x,y)]) >= 2 :
            m,s,e_d, o_d =0,0, True, True
            count = 0
            for tmp_m, tmp_s, tmp_d in mat[(x,y)]:
                count += 1
                m, s = m+tmp_m, s+tmp_s
                if tmp_d%2 == 0 :
                    o_d = False
                else :
                    e_d = False

            m, s = floor(m/5), floor(s/count)
            if m != 0 :
                if e_d or o_d :
                    for d in even_dir :
                        fire_balls.append([x,y,m,s,d])

                else :
                    for d in odd_dir :
                        fire_balls.append([x,y,m,s,d])

            
        else :
            fire_balls.append([x,y,*mat[(x,y)][0]])
        


for _ in range(M):
    fire_balls.append(list(map(int,input().strip().split())))

for _ in range(K) :
    mat = defaultdict(list)
    while fire_balls :
        ball = fire_balls.popleft()
        move(mat,ball)
    merge(mat)

result = 0
for ball in fire_balls :
    result += ball[2]
print(result)