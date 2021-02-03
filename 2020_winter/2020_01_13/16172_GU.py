import sys

# 실패함수 https://baeharam.github.io/posts/algorithm/kmp/
def failure_func(P):
    # 접두사, 접미사 일치하는 부분 길이 값들 저장해서 반환
    length = len(P)
    failure = [0] * length
    begin = 1 # 접두사, 접미사 일치하는 부분 찾아야 하므로
    m = 0 # 비교 인덱스

    while begin + m < length:
        if P[begin+m] == P[m]:
            m += 1
            failure[begin+m-1] = m
        else:
            # 하나도 일치 X
            if m==0:
                begin += 1
            else:
                begin += (m - failure[m-1])
                m = failure[m-1]

    return failure

S = sys.stdin.readline().rstrip()
K = sys.stdin.readline().rstrip()

f = failure_func(K)
indices = []
S_len, K_len = len(S), len(K)
begin = 0
m = 0

while begin <= S_len - K_len:
    # begin+m index 확인 안해주면 터진다
    if begin+m < S_len and S[begin+m].isdigit():
        begin += 1
        continue
    # 아직 pattern 못찾음 and m번째 문자 일치
    if m < K_len and S[begin+m] == K[m]:
        m += 1
        # begin 은 0부터, 문제의 i번째 문자는 1부터 indexing
        if m == K_len: 
            print(1)
            exit(0)
    # 패턴 찾음 or m번째 문자 불일치
    else:
        if m==0: # 한번도 찾은적 없다 -> begin + 1 
            begin += 1
        # begin failure 이용해서 옮겨주기
        # 접두사 접미사 같은만큼에서 시작하면 m이 0보다 큰 값에서부터 비교가능
        else:
            begin += (m - f[m-1])
            m = f[m-1]

print(0)