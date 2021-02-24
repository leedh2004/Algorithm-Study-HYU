import sys
from string import ascii_uppercase


def get_col(idx):
    ans = []

    while idx > 0:
        idx -= 1
        ans.append(num_to_alpha(idx % 26))
        idx //= 26

    return ans

 
def num_to_alpha(n):
    alpha_list = list(ascii_uppercase)
    return alpha_list[n]


while True:
    excel = sys.stdin.readline().rstrip()
    if excel == 'R0C0':
        break
    col_idx = excel.index('C')
    r = int(excel[1:col_idx])
    c = int(excel[col_idx+1:])

    ans = get_col(c)
    ans.reverse()
    print(''.join(ans)+str(r))
