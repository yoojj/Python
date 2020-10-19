# int 타입 객체를 생성하고 그 객체의 id 값을 변수에 할당
num = 1
print(id(num))
print(type(num))

# str 타입 객체를 생성하고 그 객체의 id 값을 변수에 할당
num = '일'
print(id(num))
print(type(num))



# 체인 할당  
a = b = c = 0
print(a, b, c)

d, e, f = 1, 1.0, '일'
print(d, e, f)



# 언더스코어
n1, *_ , n5 = (1, 2, 3, 4, 5)
print(n1, _, n5)
