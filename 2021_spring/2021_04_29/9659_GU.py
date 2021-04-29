import sys
from collections import deque

N = int(sys.stdin.readline())

# d = deque([1, 0, 1, 0])
# i = 5
# if N < 5:
#     if d[N-1]:
#         print("SK")
#     else:
#         print("CY")
# else:
#     while True:
#         if d[1] and d[3]:
#             cur = 0
#         else:
#             cur = 1
#         if i == N:
#             if cur:
#                 print("SK")
#             else:
#                 print("CY")
#             break
#         else:
#             d.popleft()
#             d.append(cur)
if N % 2 == 0:
    print("CY")
else:
    print("SK")
