Min, Max = map(int, input().split())
visit = [False] * (Max-Min+1) # Max와 Min 둘 다 들어가니까 +1
N=1
count = 0

while N*N<=Max : #제곱수가 Max보다 커지면 제곱수*1이 되는 수가 없으니까 더 이상 조사할 필요 없음
    N+=1
    i = Min//(N*N)   #i는 (N의 제곱수)의 배수 중 범위에 들어가는 가장 작은 수 이거나 그 범위에 가장 근접한 수   에 가기 위한 몫

    while (N*N)*i <= Max  : #(N의 제곱수)의 배수 중 범위에 들어가는 가장 작은 수 이거나 그 범위에 가장 근접한 수가 초기 (N*N)*i이고 i를 하나 씩 늘려가면서 그 범위 안에 들어가는 제곱수 ㅇㅇ 를 찾음
        idx = N*N*i - Min  #visit을 0~Max까지 할당한게 아니라 Min과 Max범위에서 짰으니까 vist의 인덱스는 지금 (조사한 수) - (Min)
        if idx>=0 and visit[idx] == False: #idx가 0보다 작아 질 수 있으니까 해주고(N의 제곱수의 배수인데 범위 안에 안들어가는 수, 보통 초기 값), visit은 조사 한 곳 또 할 필요 없으니까
            visit[idx] = True
            count += 1
        i+=1

print(len(visit)-count)