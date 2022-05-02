import turtle as t
import random

t.up()
t.hideturtle()
t.title("* 두개의 거북이 자동 랜덤 게임 *")
t.goto(-200,300)
t.write("* 두개의 거북이 자동 랜덤 게임 *", False, "left", ("arial", 25, "bold"))

time = int(t.textinput("반복 횟수 입력","반복 횟수를 입력하세요"))

t1 = t.Turtle()
t2 = t.Turtle()

t1.shape('turtle')
t1.color('blue')
t1.up()
t1.goto(-200,100)
t1.down()

t2.shape('turtle')
t2.color('green')
t2.up()
t2.goto(-200, 0)
t2.down()

t1_num = list()
t2_num = list()
t1_cnt = 0
t2_cnt = 0

for i in range(time) :
    t1_ran = random.randint(60, 90)
    t2_ran = random.randint(60, 90)

    t1.fd(t1_ran)
    t2.fd(t2_ran)

    t1_num.append(t1_ran)
    t2_num.append(t2_ran)

    t1_sum = sum(t1_num)
    t2_sum = sum(t2_num)

    if t1_sum >= 400 :
        t1.lt(t1_ran)
        t1_cnt += 1

    if t2_sum >= 400 :
        t2.rt(t2_ran)
        t2_cnt += 1

if t1_sum > t2_sum :
    t1.begin_fill()
    for i in range(5) :
        t1.fd(70)
        t1.lt(360 / 5 * 2)
    t1.end_fill()
    t1.up()
    t1.shapesize(2,2)
    t1.goto(-200, -250)
    t1.write("%d횟수 승 t1 : t1(%d)과 t2(%d)의 차이 : %d" %(t1_cnt, t1_sum, t2_sum, t1_sum-t2_sum), False, "left", ("arial", 16, "bold"))

elif t1_sum < t2_sum :
    t2.begin_fill()
    for i in range(5) :
        t2.fd(70)
        t2.rt(360 / 5 * 2)
    t2.end_fill()
    t2.up()
    t2.shapesize(2,2)
    t2.goto(-200, -250)
    t2.write("%d횟수 승 t2 : t1(%d)과 t2(%d)의 차이 : %d" %(t2_cnt, t1_sum, t2_sum, t2_sum-t1_sum), False, "left", ("arial", 16, "bold"))

else :
    t1.up()
    t1.shapesize(2,2)
    t1.goto(-200, -250)
    t1.write("%d횟수 무승부(%d)" %(t1_cnt, t1_sum), False, "left", ("arial", 16, "bold"))
    t2.up()
    t2.shapesize(2,2)
    t2.goto(-200, -270)
    t2.write("%d횟수 무승부(%d)" %(t2_cnt, t2_sum), False, "left", ("arial", 16, "bold"))
    
print(t1_num)
print(t2_num)
