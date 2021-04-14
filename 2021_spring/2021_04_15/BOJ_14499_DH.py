
class Dice:
    up, down, east, west, north, south = 0, 0, 0, 0, 0, 0
    def setValue(self, u, d, e, w, n, s):
        self.up = u
        self.down = d
        self.east = e
        self.west = w
        self.north = n
        self.south = s 
    def roll_east(self):
        self.setValue(self.west, self.east, self.up, self.down, self.north, self.south)
    
    def roll_west(self):
        self.setValue(self.east, self.west, self.down, self.up, self.north, self.south) 
    
    def roll_north(self):
        self.setValue(self.south, self.north, self.east, self.west, self.up, self.down)
    
    def roll_south(self):
        self.setValue(self.north, self.south, self.east, self.west , self.down, self.up)

N, M, y, x, _ = map(int, input().split(' '))
board = []
for i in range(N):
    row = list(map(int, input().split(' ')))
    board.append(row)

dice = Dice()
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
I = list(map(int, input().split()))

for K in I:
    ny, nx = (y + d[K-1][0], x + d[K-1][1])
    if ny >= N or nx >= M or ny < 0 or nx < 0:
        continue
    if K == 1:
        dice.roll_east()
    elif K == 2:
        dice.roll_west()
    elif K == 3:
        dice.roll_north()
    elif K == 4:
        dice.roll_south()

    if board[ny][nx] == 0:
        board[ny][nx] = dice.down
    else:
        dice.down = board[ny][nx]
        board[ny][nx] = 0
    y, x = ny, nx
    print(dice.up) 

