import sys

def recur(str_idx,pattern_idx,flag):

    # 재귀가 끝나는 시점
    if str_idx >= len(up_str) :
        return 0

    # 메모제이션 해놓은거 있으면 바로 리턴
    if dp[flag][pattern_idx][str_idx] != -1 :
        return dp[flag][pattern_idx][str_idx]
    
    ret = 0

    # 현재 인덱스부터 마지막 문자열까지
    for idx in range(str_idx,len(up_str)):

        # 위 문자열에서 현재 패턴 순서에 맞는 문자가 나왔을 때
        if flag and up_str[idx] == pattern[pattern_idx]:
            if pattern_idx == len(pattern) - 1 :
                ret = ret + 1
            else :
                ret = ret + recur(idx+1,pattern_idx+1,0)
                

        # 아래 문자열
        elif not flag and down_str[idx] == pattern[pattern_idx] : 
            if pattern_idx == len(pattern) - 1 :
                ret = ret + 1
            else :
                ret = ret + recur(idx+1,pattern_idx+1,1)

    # 메모제이션
    dp[flag][pattern_idx][str_idx] = ret

    return ret


sys.setrecursionlimit(100000)
pattern = sys.stdin.readline().rstrip()
up_str = sys.stdin.readline().rstrip()
down_str = sys.stdin.readline().rstrip()
ans = 0
dp = [[[-1 for col in range(len(up_str)) ] for row in range(len(pattern))] for z in range(2)]
print(recur(0,0,0) + recur(0,0,1))