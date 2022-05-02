"""
# 1
x = 100
y = 50

print(x)
print(y)



# 2
x = 100
y = 200
result = x + y

print(x)
print(y)
print(result)



#3
x = 100
y = 50

a = x + y
b = x - y
c = x * y
d = x / y
print(x, y)
print('x + y =', a)
print('x - y =', b)
print('x * y =', c)
print('x / y =', d)



#4
school = "금오공과대학교"
name = "장성진"
sid = "20220997"

print(school, name, sid)



#5
num = input()
print(num)


#5-1
num = input()
num1 = 5

print(num)
print(num + num1)



#6
a, b, c, d = input().split()
print(a+b, c, d)


#6-2
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
print('합산결과는', a+b+c, '입니다')


#6-2-1
a = float(input())
b = float(input())
c = float(input())
print('합산결과는', a+b+c, '입니다.')



#7
sch = input('학교를 입력하세요 : ')
print(sch+'에 오신 것을 환영합니다.')
nam = input('학생이름을 입력하시오 : ')
print(sch+'에는'+nam+'학생이 재학중입니다.')
num1 = input('첫 번째 자연수를 입력하시오 : ')
num2 = input('두 번째 자연수를 입력하시오 : ')
result = int(num1) * int(num2)
print('두 피연산자를 곱하면', result, '입니다.')
"""


#8
a = 10
b = 1.34
c = "hello"
d = True
print(type(a), type(b), type(c), type(d))



