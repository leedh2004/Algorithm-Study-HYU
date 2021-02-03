import sys
import itertools

N = int(sys.stdin.readline())

num = list(map(int,sys.stdin.readline().split()))

plus, minus, multiple, divide = map(int,sys.stdin.readline().split())
operator= []
for i in range(plus):
    operator.append('+')
for i in range(minus):
    operator.append('-')
for i in range(multiple):
    operator.append('*')
for i in range(divide):
    operator.append('/')
comb = list(itertools.permutations(operator))
comb = list(set(comb))
case = []

maximum = -1000000000
minimum = 1000000000

for i in range(len(comb)):
    result = num[0]
    for j in range(N-1):
        if comb[i][j] == '+':
            result += num[j+1]
        elif comb[i][j] == '-':
            result -= num[j+1]
        elif comb[i][j] == '*':
            result *= num[j+1]
        elif comb[i][j] == '/':
            if result < 0 and num[j+1] > 0:
                result = -((-result)//num[j+1])
            else:
                result //= num[j+1]
    if result >= maximum:
        maximum = result
    if result <= minimum:
        minimum = result

print(maximum)
print(minimum)
