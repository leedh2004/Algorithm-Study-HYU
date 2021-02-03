from itertools import permutations
from itertools import combinations



# 소수 판단 함수
def is_prime(num):
    
    # 0,1 예외 처리
    if num == 1 or num == 0 :
        return False
    
    # 2부터 sqrt(num) 까지 돌면서 수행
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
        
    return True

def solution(numbers):
    
    lis = list(numbers)
    
    # 중복이 없어야 하기 때문에 set 사용
    answer = set()
    
    # 뽑는 갯수
    for i in range(1,len(numbers)+1):
        
        # i개만큼 뽑는 조합
        combs = combinations(lis,i)
        
        # 뽑은 조합들 순회
        for comb in combs:
            
            # 뽑은 조합으로 순열
            perms = permutations(comb)
            # print(comb)
            for perm in perms:
                num = int("".join(perm))
                # print(num)
                if is_prime(num):
                    
                    answer.add(num)
    
    return len(answer)