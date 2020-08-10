A_numer, A_deno = map(int, input().split())
B_numer, B_deno = map(int, input().split())

sum_numer, sum_deno = (A_numer*B_deno+B_numer*A_deno), A_deno*B_deno

target = max(sum_numer,sum_deno)
other = min(sum_numer,sum_deno)

while True :
    quotient = target // other
    remainder = target % other
    if remainder == 0 :
        break
    target = other
    other = remainder

print(sum_numer//other, sum_deno//other)