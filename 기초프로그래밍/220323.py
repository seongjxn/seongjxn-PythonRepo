""" """
#1
num = int(input("정수를 입력하세요 : "))

if num >= 0 :
    if num == 0 :
        print("0 입니다.")
    else :
        print("양수 입니다.")
else:
    print("음수 입니다.")



#2
id = "ilovepython"
s = input("아이디를 입력하세요 : ")
if s == id:
    print("환영합니다.")
else :
    print("아이디를 찾을 수 없습니다.")



#3
for i in [1, 2, 3, 4, 5] :
    print('방문을 환영합니다.')
