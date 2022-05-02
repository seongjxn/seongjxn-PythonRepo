# 1. 2개의 리스트를 선언하여 같은 값을 찾는 프로그램을 작성하시오.

list1 = [5, 6, 9, 1, 4]
list2 = [7, 8, 6, 2, 3]

result = set(list1) & set(list2)                            # 조건1 : 하나의 리스트는 같은 값을 가져서는 안된다.
result = list(result)

print('리스트(1)에 저장된 값 :', end = ' ')
for i in range(len(list1)) :
    print(list1[i], end = ' ')
    if i+1 == len(list1) :
        print()

print('리스트(2)에 저장된 값 :', end = ' ')
for i in range(len(list2)) :
    print(list2[i], end = ' ')
    if i+1 == len(list2) :
        print()

print('두 리스트의 동일한 값은 %d 입니다.' %result[0])      # 조건2 : 동일한 값 한 개만 찾을 수 있도록 한다.



# 2. 자판기 프로그램 모듈화

def incertCoin() :          # 동전 투입 함수
    print('----- 동전을 투입하세요 -----')

    while True:
        coin500 = int(input('500원 개수 : '))
        coin100 = int(input('100원 개수 : '))
        
        coin = coin500 * 500 + coin100 * 100
        
        if coin >= 2000 :
            print('2000원 이하로 투입해 주세요.')
            continue

        else :
            print('%d 원을 투입하셨습니다.' %coin)
            return coin

    return


def showMenu() :            # 제품 출력 함수
    global menu, cost, flag

    menu = ['커피', '콜라', '사이다', '오렌지 쥬스']
    cost = [300, 500, 500, 400]
    flag = [0, 0, 0, 0]

    print('\n---------- 메뉴 ----------')
    for i in range(len(menu)) :
        print('[%d] %s : %d' %(i+1, menu[i], cost[i]))
    print('[0] 종료')

    return


def sellMenu(money) :       # 제품 선택 후 금액이 차감되는 함수
    global menu, cost, flag

    runStat = True

    while runStat == True :
        if money < min(cost):
            runStat = False
        else :
            pass
        selectMenu = int(input('\n메뉴를 선택하세요 : '))
        if selectMenu == 0 :
            runStat = False
        else :
            selectMenu -= 1
            if money < min(cost):
                runStat = False
            else :
                pass

            if money >= cost[selectMenu] :
                money -= cost[selectMenu]
                flag[selectMenu] += 1
                print('%s를 구매하셨습니다.' %menu[selectMenu], end = ' ')
            else :
                print('잔액이 부족합니다.', end = ' ')
            print('잔액은 %d원 입니다.' %money)
  
    return


def result() :              # 최종적으로 제품을 구매한 갯수를 출력하는 함수
    global menu, flag

    print('\n------ 구매하신 물품 ------')
    for i in range(len(menu)) :
        print('[%d] %s : %d개' %(i+1, menu[i], flag[i]))
    

myMoney = incertCoin()
showMenu()
sellMenu(myMoney)
result()



# 3. 지역변수와 전역변수의 차이점
"""
지역변수는 전역변수와 달리 함수 안에서만 사용가능하다.

전역변수는 함수 밖 어디에서나 사용 가능하다.
단, 함수 내에서 사용하려면 global을 통해 전역변수를 함수에서 사용한다고 선언하면 된다.
"""