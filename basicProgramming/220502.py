"""

# 1

letters = ['A', 'B', 'C', 'D', 'E', 'F']

l = letters

print(l)

print(letters)

l[3] = 5

print(l)

print(letters)

l2 = letters[:]

print(l2)

l2[0] = 0

print(l2)

print(letters)



# 2

def stack_Main():
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    print(stack)

    while stack :
        print("POP >", stack.pop())

stack_Main()


# 3

def queue_Main():
    queue = []
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    print(queue)

    while queue :
        print("GET >", queue.pop(0))

queue_Main()


# 4

import random

sentence = ['꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.',
            '사람은 사랑할 때 누구나 시인이 된다.',
            '고생 없이 얻을수 있는 진실로 귀중한 것은 하나도 없다.',
            '시작이 반이다.']

print("######################## \n      오늘의 속담     \n########################")

result = random.choice(sentence)

print(result)


"""
# 5

class CCalculator :
    def __init__(self):
        self.result = 0

    def input(self) :
        value = int(input('숫자 : '))
        oper = input('연산자 : ')
        return value, oper

    def calc(self, value, oper) :
        global runStat

        if oper == '+' :
            return cc.add(value)
        elif oper == '-' :
            return cc.substract(value)
        elif oper == '*' :
            return cc.multiply(value)
        elif oper == '/' :
            return cc.division(value)
        else :
            runStat = False

    def add(self, value) :
        self.result += value
        return self.result
    
    def substract(self, value) :
        self.result -= value
        return self.result

    def multiply(self, value) :
        self.result *= value
        return self.result

    def division(self, value) :
        self.result /= value
        return self.result

cc = CCalculator()

runStat = True

while runStat == True :
    data, oper = cc.input()
    result = cc.calc(data, oper)
    print(result)

