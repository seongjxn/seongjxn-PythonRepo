'''

# 1
def greet(name, msg='별일없지?') :
    print('안녕', name + ',' + msg)

greet('영희')
greet('영희', '잘 있니?')



# 2
def range() :
    global min, max
    min, max = input('시작 단과 끝 단을 입력하세요 : ').split()
    min = int(min)
    max = int(max)

    return min, max

def run(min, max) :
    dan = min
    while dan <= max :
        a = 1
        while a < 10 :
            print("%d * %d = %d" %(dan, a, dan*a))
            a += 1
        dan += 1
        print('\n')

    return

range()
run(min, max)

'''

# 3
import turtle
t = turtle.Pen()
t.shape = turtle

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)