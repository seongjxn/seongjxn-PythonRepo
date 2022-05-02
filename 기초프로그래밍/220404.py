'''

# 1
def prints():
    print('hello world')

prints()



"""
자료형(Datatypes)
정수형      : int
실수형      : float
문자, 문자열 : char, str
참, 거짓    : bool
"""



# 2
def calculate_area(radius) :
    area = 3.14 * radius ** 2
    return area

c_area = calculate_area(5.0)
print(c_area)



# 3
def noReturnFn() :
    return

print(noReturnFn)

'''

# 4
import random

def userInput() :
    user =  int(input('input    dice : '))
    return user

def comInput() :
    global user
    com = random.randint(1, 6)
    return com

def diceRule(user, com) :
    # global userWinCount, userLoseCount
    # global comWinCount, comLoseCount
    # global drawCount
    
    global gameCount

    if user != -1 :
        print('computer dice :', com)
        if user > com :
            # userWinCount += 1
            # comLoseCount += 1
            gameCount[0] += 1
            gameCount[3] += 1
 
            print('user success!')
            # print('user    ', userWinCount, 'win!')
            # print('computer', comLoseCount, 'lose!')

            print('user    ', gameCount[0], 'win!')
            # print('computer', gameCount[3], 'lose!')
            print()
        elif user < com : 
            # userLoseCount += 1r
            # comWinCount += 1
            gameCount[1] += 1
            gameCount[2] += 1

            print('com success!')
            # print('user    ', userLoseCount, 'lose!')
            # print('computer', comWinCount, 'win!')

            # print('user    ', gameCount[1], 'lose!')
            print('computer', gameCount[2], 'win!')
            print()
        elif user == com :
            # drawCount += 1
            gameCount[4] += 1

            print('draw\n')
            
    return

u = 0
c = 0

# userWinCount = 0
# userLoseCount = 0
# comWinCount = 0
# comLoseCount = 0
# drawCount = 0

gameCount = [0, 0, 0, 0, 0]

runStat = True

while runStat == True :
    u = userInput()
    c = comInput()
    diceRule(u, c)

    if u == -1 :
        runStat = False
        print('\n-----result-----')
        # print('userWin  :', userWinCount)
        # print('userLose :', userLoseCount)
        # print('comWin   :', comWinCount)
        # print('comLose  :', comLoseCount)
        # print('draw     :', drawCount)

        print('userWin  :', gameCount[0])
        # print('userLose :', gameCount[1])
        print('comWin   :', gameCount[2])
        # print('comLose  :', gameCount[3])
        print('draw     :', gameCount[4])
        

'''

# 5
def max(num1, num2) :
    if num1 > num2:
        result = num1
    else :
        result = num2
    return result

def main():
    i, j = input().split()
    i = int(i)
    j = int(j)
    k = max(i, j)
    print(i, '와/과', j, '중 큰 수는', k, '입니다.')

main()

'''

# 6
