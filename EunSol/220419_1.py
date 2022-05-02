# 1
def add_from_x1_to_x2(x1, x2) :
    result = 0
    for i in range(x1, x2+1) :
        result+=i
    print('ret:', result)
    return

x1 = int(input())
x2 = int(input())
add_from_x1_to_x2(x1, x2)

# 2
def calc_base_a_exponent_n(a, n) :
    for i in range(n+1):
        print(f"%d ^ %d = {a**i:.1f}" %(a, i))
    return

a = int(input())
n = int(input())
calc_base_a_exponent_n(a, n)