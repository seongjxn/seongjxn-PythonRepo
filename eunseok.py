# 2
num = int(input('정수를 입력하세요 : '))
i = 1
total = 1

while i <= num :
    if i%3 == 0 :
        print(i, end = ' ')
        total = total * i
    i+=1
    
print('\n %d까지 3의 배수 곱셈은 %d 입니다.' %(num, total))

'''
# 3
num = int(input('정수를 입력하세요 : '))
i = 1

while i <= num :
    if i%3 == 0 :
        print(i, end = ' ')
    i+=1
'''