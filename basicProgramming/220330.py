import random

user = 0
computer = 0

runStat = True

while runStat == True :
    user = input("주사위 굴리기 (1 ~ 6) : ")

    if eval(user) > 0 and eval(user) < 7 :
        computer = random.randint(1, 6)

        print("사용자는 %d 입니다." % user)
        print("컴퓨터는 %d 입니다." % computer)

    elif user == 9 :
        runStat = False

    else :
        print("1 ~ 6 사이의 값을 입력해 주세요.")