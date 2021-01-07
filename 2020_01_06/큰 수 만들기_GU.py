def solution(number, k):
    # k개 빼도 자리수는 언제나 같다. 앞쪽 자리수가 커지게 greedy
    answer = ''
    nums = list(map(int,str(number)))
    success = len(nums) - k # 성공 자리수
    while k > 0:
        if len(answer) == success: return answer
        front_max_idx = nums[:k+1].index(max(nums[:k+1]))
        if front_max_idx == 0:
            answer += str(nums.pop(0))
        else:
            for i in range(front_max_idx):
                nums.pop(0)
                k -= 1
            answer += str(nums.pop(0))
    if nums:
        answer += "".join(map(str,nums))
    return answer

number,k = map(int,input().split())
print(solution(number,k))