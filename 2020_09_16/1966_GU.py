import sys

T = int(sys.stdin.readline())
for i in range(T):
    success = False
    cnt = 1
    N,idx = map(int,sys.stdin.readline().split())
    priority = list(map(int,sys.stdin.readline().split()))
    while True:
        # 찾고자 하는 값이 프린터 큐 맨 앞
        if idx == 0:
            if priority[0] == max(priority):
                print(cnt)
                break
            else:
                tmp = priority.pop(0)
                priority.append(tmp)
                idx = len(priority) - 1 
        # 다른 값이 맨 앞
        # 다른 값 pop
        if priority[0] == max(priority):
            priority.pop(0)
            cnt += 1
        else:
            tmp = priority.pop(0)
            priority.append(tmp)
        #pop or 뒤로 -> idx 앞으로
        idx -= 1
        
