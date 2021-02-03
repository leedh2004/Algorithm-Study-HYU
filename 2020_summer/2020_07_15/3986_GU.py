import sys

N = int(sys.stdin.readline())
stack = []
cnt = 0
for i in range(N):
    string = list(sys.stdin.readline().rstrip())
    for j in range(len(string)):
        if len(stack) == 0:
            stack.append(string[j])
        else:
            if stack[-1] == string[j]:
                stack.pop()
            else:
                stack.append(string[j])
    if len(stack) == 0: cnt += 1
    stack.clear()
print(cnt)
    