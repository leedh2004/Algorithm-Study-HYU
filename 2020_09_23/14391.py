N,M = map(int, input().split())
mat = [ list(map(int, input()))  for _ in range(N)]

result = -1
for case in range(1<<(N*M)): #모든 케이스를 다 볼거임. 만약 N*M이 2by2라면 100이 되어서 00, 01, 10, 11 을 볼거임. 해당 비트가 0이라는것은 해당 자리의 칸이 가로로 자르는 종이에 포함, 1이면 세로에 자리는 종이에 포함
  sum = 0    #가로, 세로로 자른 종이의 총합을 담을 변수
  for i in range(N): #가로로 잘린 경우를 보자
    num = 0   #잘린 종이의 숫자가 들어갈거임.
    for j in range(M): 
      idx = i * M + j  # 2차원 배열을 1차원으로 바꾸었을때의 자리임. case가 1차원으로 표현한 배열이라고 생각 할 수 있으므로 해당 index를 찾아주자
      if (case & (1<<idx)) == 0: #idx로 case의 index를  찾아주어 지금 실행되고 있는 case(경우)에 해당 칸이 가로로 잘린 종이에 포함되는지 확인
        num = num * 10 + mat[i][j] #가로로 잘린 종이에 포함된다면 이전에 만들어둔 수를 왼쪽으로 한칸 밀고 지금 칸의 숫자를 뒤에 붙여줌
      else: #현재 칸이 세로로 잘린 종이에 포함된다는 것이므로 현재까지 만든 숫자를 sum에 더해주고 tmp 값인 num을 0으로 초기화
        sum += num
        num = 0
    sum += num #만약 한 행이 한개의 숫자에 전부 포함된다면 여기서 더해줌. 행의 마지막 칸이 세로로 자른 종이에 들어간다 해도 num(tmp값)이 0일테니 문제 x

  for i in range(M): #이번에는 | (col으로 보며 세로로 잘린 종이 확인하기)
    num = 0
    for j in range(N):
      idx = j * M + i
      if (case & (1<<idx)) != 0:
        num = num * 10 + mat[j][i]
      else:
        sum += num
        num = 0
    sum += num

  result = max(result, sum)

print(result)