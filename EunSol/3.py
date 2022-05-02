import random

def getMax(a, b):
    if a<b:
        maxValue = b
    else:
        maxValue = a
    return maxValue

a = random.randint(0,100)
b = random.randint(0,100)

print(getMax(a, b))