height = float(input("키를 입력하세요(단위는 미터입니다) : "))
weight = float(input("몸무게를 입력하세요(단위는 kg입니다) : "))
bmi = weight/height ** 2
if bmi < 18.5 :
    print("저체중")
elif bmi < 23 :
    print ("정상")
elif bmi < 25 :
    print("과체중")
elif bmi < 30 :
    print("비만 1단계")
elif bmi < 40 :
    print("비만 2단계")
else :
    print("심각한 비만 상태")
print("비만도 = {:2f}" . format(bmi))
               
count = 1 
while count < 5 :
    print("count의 값 =" , count)
    count = count + 1
print("반복문이 종료되었습니다")
               
sum = 0
num = 1
while num <=100 :
    sum = sum + num
    num = num + 1
print("1qnxj 100까지의 합 =", sum)
               
factorial = 1 
num = 2 
while num <= 10 :
    factorial = factorial + num
    num = num + 1
print("10! =" , factorial)