import math
import itertools

def solution(numbers):
    answer = 0
    comb = [n for n in numbers]
    for i in range(2,len(numbers)+1):
        tmp = list(map(''.join,itertools.permutations(numbers,i)))
        for j in range(len(tmp)):
            tmp[j] = tmp[j].lstrip('0')
            if tmp[j] != '0' and tmp[j] != '':
                comb.append(tmp[j])
    #comb = list(set(comb))
    print(comb)
    comb = list(map(int,list(set(comb))))
    comb.sort()
    n = max(comb)

    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    prime =  [ i for i in range(2, n+1) if array[i] ]

    for num in comb:
        if num in prime:
            answer += 1

    return answer

numbers = input()
print(solution(numbers))