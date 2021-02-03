import sys

def swap(nums,A,B):
    temp = nums[A]
    nums[A] = nums[B]
    nums[B] = temp

def find(cnt,nums):
    nums_ = map(str,nums)
    nums_ = int(''.join(nums_))
    if cnt == K:
        return nums_
    #check에다가 기록해둬서 접근한 부분 다시 계산 X하도록
    if check[nums_][cnt] != 0:
        return check[nums_][cnt]
    ans = 0
    for i in range(M):
        for j in range(i+1,M):
            swap(nums,i,j)
            ans = max(ans,find(cnt+1,nums))
            swap(nums,i,j)
    check[nums_][cnt] = ans
    return ans

N,K = map(int,sys.stdin.readline().split())
nums = list(map(int,list(str(N))))
M = len(nums)
# 10 -> 최대 K번 100,0000 최대숫자
check = [[0] * 10 for _ in range(1000001)]

nums_ = map(str,nums)
nums_ = int(''.join(nums_))
#한자리 or 10,20 ... 90 안됨 
if M == 1 or nums_ == 10 or nums_ == 20 or nums_ == 30 or nums_ == 40 or nums_ == 50 : print(-1)
elif nums_ == 60 or nums_ == 70 or nums_ == 80 or nums_ == 90: print(-1)
else: print(find(0,nums))
        

#greedy로 풀었을 경우.. 
#반례 1220 2  ans:2210 but 2201
#반례 2133 2  ans:3321 but 3312 + (2133 3 -> 3321)
#maximum = nums[:]
#maximum.sort(reverse = True)
"""for i in range(K):
    if M == 1: break #한자리수
    check()
    #print(same)
    if same.count(False) > 0:
        next_idx = same.index(False)
        temp = maximum[next_idx]
        nums_idx = 0
        for j in range(M-1,-1,-1):
            if nums[j] == temp:
                nums_idx = j
                break
        swap(next_idx,nums_idx)
    else:
        swap(M-1,M-2)
    if nums[0] == 0: break"""