import sys  
#알파벳 전체이다....
n = int(sys.stdin.readline())
words = []
alphabets = []
# 가장 긴 word 길이
longest = 0
for i in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    alphabets.extend(tmp)
    if longest < len(tmp): longest = len(tmp)
    words.append(tmp)
#쓰이는 알파벳 파악 (max 10)
alphabets = list(set(alphabets))
alphabets.sort()
#다 더했을 때 자릿수별 오는 알파벳 모음 (높은 자리순서)
nums = [[] for _ in range(longest)]
for i in range(longest):
    for j in range(len(words)):
        if words[j]:
            nums[i].append(words[j].pop())
nums.reverse()
#알파벳에 대응하는 숫자 테이블 만들어주기
val_num = [str(x) for x in range(len(alphabets))]
table = str.maketrans(str.join("",alphabets),str.join("",val_num))
weight = [0 for _ in range(10)]
for i in range(longest):
    for j in range(len(nums[i])):
        weight[int(nums[i][j].translate(table))] += (10 ** (longest - i - 1))
#내림차순 정렬
weight.sort(reverse = True)
res = 0
#큰 숫자부터 넣기
num = 9
for i in range(10):
    res += (num * weight[i])
    num -= 1
print(res)



        



