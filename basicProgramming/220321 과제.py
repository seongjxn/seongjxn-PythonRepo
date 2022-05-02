##1 정수형 변환
value = "12"
value = int(value)



##2 문자열 출력
str = 'hello'
print(str[2]) # l
print(str[4]) # o



##3 index
p = int(input())
List = ['h', 'e', 'l', 'l', 'o']
print(List[p])



##4 리스트 값 추가
#[1, 2, 3, 4, 5]에서 [1, 2, 3, 4, 5, 6] 형태로

##풀이 1
ListValue = [1, 2, 3, 4, 5]
value = input()             # 6 입력
ListValue.append(value)
print(ListValue)

## 풀이 2
ListValue = [1, 2, 3, 4, 5]
value = input()             # 6 입력
ListValue.insert(5, value)
print(ListValue)



#5 리스트, 튜플, 사전 차이점 설명
"""
리스트 : 객체의 집합으로, 순서를 가짐. 수정 가능. [] 대괄호 사용
튜플 : 리스트와 유사하지만 수정이 불가능. () 소괄호 사용
사전 : 키와 값을 각각 가진 집합. 수정 가능. {} 중괄호 사용
"""


#6 len, copy, in 구체적 설명
"""
len : 변수에 자료가 몇개 들어 있는지 알기 위해 사용
ex)
a = [1, 2, 3, 4, 5]
len(a) # 5

copy : 리스트 값을 복사.
ex)
a = [1, 2, 3, 4, 5]
b = a
a를 수정하면 b도 같이 수정됨

a = [1, 2, 3, 4, 5]
b = a.copy()
copy를 사용하면 a를 수정해도 b가 바뀌지 않게 함.

in : 포함 연산 또는 반복문에서 요소를 찾는 데 사용
ex)
a = [1, 2, 3, 4, 5]

if 1 in a :
    print(True)
else :
    print(False)
포함 연산에서의 사용

for i in a :
    print(i)
반복문에서 사용
"""

#7 영한사전 구현
dict = {'apple' : '사과',
        'banana' : '바나나',
        'school' : '학교',
        'book' : '책',
        'desk' : '책상',
        'help' : '도움',
        'sad' : '슬픔',
        'laptop' : '노트북'
        }
word = input()
print(dict[word])