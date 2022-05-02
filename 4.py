a, b = map(int, input().split())

def print_sub(a, b) :
    print("%d과 %d의 차는 %d입니다." %(a, b, a-b))
    return

def print_mult(a, b) :
    print("%d과 %d의 곱은 %d입니다." %(a, b, a*b))
    return

print_sub(a, b)
print_mult(a, b)
