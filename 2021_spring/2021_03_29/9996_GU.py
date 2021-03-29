import sys

# 1
# a*a  -> a (NA)...


def check(name):
    for i in range(len(front)):
        if name[i] != front[i]:
            return False

    j = len(name) - 1
    for i in range(len(back)):
        if name[j] != back[i]:
            return False
        j -= 1

    return True


N = int(sys.stdin.readline())
pattern = sys.stdin.readline().rstrip()
min_len = len(pattern) - 1
star_idx = pattern.index('*')
front = list(pattern[:star_idx])
back = list(pattern[star_idx+1:])
back.reverse()

for i in range(N):
    file_name = sys.stdin.readline().rstrip()
    if len(file_name) < min_len:
        print("NE")
    else:
        if check(file_name):
            print("DA")
        else:
            print("NE")
