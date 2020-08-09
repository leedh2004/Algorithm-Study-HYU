import sys

def find(a,b):
    while b!=0:
        n = a%b
        a = b
        b = n
    return a

a,b = map(int,sys.stdin.readline().split())
c,d = map(int,sys.stdin.readline().split())
gcd = 0
if b > d: gcd = find(b,d)
else: gcd = find(d,b)
lcm = (b//gcd)*(d//gcd)*gcd
a *= lcm // b
c *= lcm // d
upper = a+c
if lcm > upper: gcd = find(lcm,upper)
else: gcd = find(upper,lcm)
print(upper//gcd,lcm//gcd)