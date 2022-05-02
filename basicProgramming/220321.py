"""
#1
dict = {"apple" : "사과",
        "student" : "학생",
        "factory" : "공장"
        }

a = input()

print(dict[a])



#2
score = int(input("성적을 입력하시오: "))
if score >= 60:
	print("합격입니다.")
else:
	print("불합격입니다.")



#3
age = int(input("나이를 입력하시오 : "))

if age >= 15 :
    print("이 영화를 보실 수 있습니다.")
else :
    print("이 영화를 보실 수 없습니다.")



#4
num1 = 0
num2 = 0
oper = '+'

if oper == '+' :
    print("덧셈 입니다.")
elif oper == '-' :
    print("뺄셈 입니다.")
elif oper == '*' :
    print("곱셈 입니다.")
elif oper == '/' :
    print("나눗셈 입니다.")
else :
    print("해당하는 연산자가 없습니다.")



#4
num1, num2 = input("숫자를 입력하세요 : ").split()
num1 = int(num1)
num2 = int(num2)
oper = input("연산자를 입력하세요 : ")

if oper == '+' :
    print("덧셈 입니다.")
    print(num1, oper, num2, '=', num1+num2)
elif oper == '-' :
    print("뺄셈 입니다.")
    print(num1, oper, num2, '=', num1-num2)
elif oper == '*' :
    print("곱셈 입니다.")
    print(num1, oper, num2, '=', num1*num2)
elif oper == '/' :
    print("나눗셈 입니다.")
    print(num1, oper, num2, '=', num1/num2)
else :
    print("해당하는 연산자가 없습니다.")



#5
import random

print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 0 :
    print("앞면입니다.")
else :
    print("뒷면입니다.")
print("게임이 종료되었습니다.")



#6
num = int(input("숫자를 입력하세요 : "))

if num > 0 :
    print("양수입니다.")
elif num < 0 :
    print("음수 입니다.")
else :
    print("0 입니다.")
"""


#7
import random

time = random.randint(1, 24)

print("지금 시각은", str(time)+"시 입니다.")

sunny = random.choice([True, False])

if sunny :
    print("현재 날씨가 화창합니다.")
else :
    print("현재 날씨가 화창하지 않습니다.")

if time >= 6 and time < 9 and sunny :
    print("종달새가 노래를 한다.")
else :
    print("종달새가 노래를 하지 않는다.")