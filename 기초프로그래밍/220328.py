"""
# 1
response = '아니'

while response == '아니' :
    response = input('엄마, 다 됐어?')

print('먹자')



# 2
print('1. 실행')
print('2. 도움말')
print('3. 종료')

run = True

while run == True :
    select = int(input('메뉴 선택 : '))

    if select == 1 :
        print('실행')
    elif select == 2 :
        print('도움말')
    elif select == 3 :
        print('종료')
        run = False
    else :
        print('다시 입력하세요')



# 3
password = ''
while password != 'pythonisfun' :
    password = input('암호를 입력하세요 : ')
print('로그인 성공!')



# 4
count = 1
sum = 0
while count <= 10 :
    sum = sum + count
    count = count + 1
print('sum is', sum)



# 5
print('1. 사칙연산')
print('2. 도움말')
print('3. 종료')

run = True
num1 = 0
num2 = 0
opr = '+'

while run == True :
    select = int(input('메뉴 선택 : '))

    if select == 1 :
        print('사칙연산')
        num1 = int(input("Num 1 : "))
        num2 = int(input("Num 2 : "))
        opr = input('Opr : ')
        
        if opr == '+' :
            print(num1 + num2)
        elif opr == '-' :
            print(num1 - num2)
        elif opr == '*' :
            print(num1 * num2)
        elif opr == '/' :
            print(num1 / num2)
        else :
            print('다시 입력하세요')

    elif select == 2 :
        print('도움말')
    elif select == 3 :
        print('종료')
        run = False
    else :
        print('다시 입력하세요')



# 6
dan = int(input("원하는 단은: "))

i = 2
while i <= dan :
    j = 1
    while j < 10 :
        print("%d * %d = %d" % (i, j, i*j))
        j = j + 1
    i = i + 1
    print('\n')
"""


# 7
"""
투입 금액 : myMoney
제품 금액 ; xxCost
제품 개수 : xxFlag
"""

myMoney = 0

coffeeCost = 1000
orangeCost = 1500
cokeCost = 2000

coffeeFlag = 0
orangeFlag = 0
cokeFlag = 0

runStat = True
end = 1000

myMoney = int(input('안녕하세요, 자판기를 이용하시려면 돈을 투입하세요 : '))
print('%d원을 투입하셨습니다.' %myMoney)
print('\n----메뉴-----',
      '\n1. 커피 :', coffeeCost,
      '\n2. 콜라 :', cokeCost,
      '\n3. 오렌지 쥬스 :', orangeCost,
      '\n0. 종료')

while myMoney >= end or runStat == True :
    selMenu = int(input('\n메뉴 번호를 입력하세요 : '))

    if selMenu == 1 :
        if myMoney >= coffeeCost :
            myMoney = myMoney - coffeeCost
            coffeeFlag += 1
            print("커피를 구매하였습니다. 잔액은 %d원 입니다." %myMoney)
        else :
            print("잔액이 부족합니다.")
            runStat = False
    
    elif selMenu == 2 :
        if myMoney >= cokeCost :
            myMoney = myMoney - cokeCost
            cokeFlag += 1
            print("콜라를 구매하였습니다. 잔액은 %d원 입니다." %myMoney)
        else :
            print("잔액이 부족합니다.")
            runStat = False

    elif selMenu == 3 :
        if myMoney >= orangeCost :
            myMoney = myMoney - orangeCost
            orangeFlag += 1
            print("오렌지 쥬스를 구매하였습니다. 잔액은 %d원 입니다." %myMoney)
        else :
            print("잔액이 부족합니다.")
            runStat = False

    elif selMenu == 0 :
        runStat = False

    else :
        print("다시 입력해 주세요.")

print("구매하신 물품은 ")


print("이용해 주셔서 감사합니다.")