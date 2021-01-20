import sys
import math

def vector_length(vector):
    return math.sqrt(vector[0]**2 +vector[1]**2 + vector[2]**2)
def vector_substract(v1,v2):
    return [v1[0]-v2[0],v1[1]-v2[1],v1[2]-v2[2]]


Ax,Ay,Az,Bx,By,Bz,Cx,Cy,Cz = map(int,sys.stdin.readline().split())
point = [Cx,Cy,Cz]
left = [Ax,Ay,Az]
right = [Bx,By,Bz]
mid = [(Ax+Bx)/2,(Ay+By)/2,(Az+Bz)/2]
gap = abs(vector_length(vector_substract(point,left)) - vector_length(vector_substract(point,right)))
ans = min(vector_length(vector_substract(point,left)),vector_length(vector_substract(point,right)))
# True -> left쪽이 짧다 
#flag = True
if vector_length(vector_substract(point,left)) >= vector_length(vector_substract(point,right)):
    #flag = False
    left = mid
else:
    right = mid

while True:
    if gap < 10e-7:
        break

    mid = [(left[0]+right[0])/2,(left[1]+right[1])/2,(left[2]+right[2])/2]
    #ans = min(vector_length(vector_substract(point,left)),vector_length(vector_substract(point,right)))
    gap = abs(vector_length(vector_substract(point,left)) - vector_length(vector_substract(point,right)))
    if vector_length(vector_substract(point,left)) >= vector_length(vector_substract(point,right)):
        left = mid
    else:
        right = mid
    
print('%.10f'% vector_length(vector_substract(point,mid)))

"""
아래코드는 정답은 맞는데 왜틀린지 모르겠다
"""
AB = [Bx-Ax,By-Ay,Bz-Az]
AC = [Cx-Ax,Cy-Ay,Cz-Az]
BC = [Cx-Bx,Cy-By,Cz-Bz]
tmp = [AB[1],AB[2],AB[0],AB[1]]
tmp2 = [AC[1],AC[2],AC[0],AC[1]]
outer_product = [0,0,0]

# 외적
outer_product[0] = tmp[0]*tmp2[1] - tmp[1]*tmp2[0]
outer_product[1] = tmp[1]*tmp2[2] - tmp[2]*tmp2[1]
outer_product[2] = tmp[2]*tmp2[3] - tmp[3]*tmp2[2]

# case
# 점이 vector 상에 존재 - 1. 선분 안에 존재(길이 0) 2. 선분 밖에 존재
# 점이 vector 상에 존재X - 1. 수선의 발이 선분 안에 존재 2. 수선의 발이 선분 밖(vector 안)에 존재

OA = vector_length([Ax,Ay,Az])
OB = vector_length([Bx,By,Bz])
OC = vector_length([Cx,Cy,Cz])

# print("outer",vector_length(outer_product))
# print("AB", vector_length(AB))


if vector_length(AB) == 0:
    print(vector_length(AC))
elif vector_length(AC) == 0:
    print(0.0000000000)
# 점이 vector상에 존재 
elif vector_length(outer_product) == 0:
    if (OA <= OC and OC <= OB) or (OB <= OC and OC <= OA):
        print(0.0000000000)
    else:
        print("%.10f" % min(vector_length(AC),vector_length(BC)))
# 점이 vector 상에 존재X
else:
    if vector_length(AB)**2 + vector_length(BC)**2 > vector_length(AC)**2:
        if AB[0] == 0 and AB[1] == 0 and AB[2] == 0:
            print("%.10f" % vector_length(AC))
        else:
            print("%.10f" % (vector_length(outer_product) / vector_length(AB)))
    else:
        print("%.10f" % min(vector_length(AC),vector_length(BC)))