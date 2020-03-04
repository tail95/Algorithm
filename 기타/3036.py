import sys

def gcd(x, y):
    while True:
        if x==y:
            break
        if x > y:
            x=x-y
        else:
            y=y-x
    return x
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
a, b = numbers[0] , numbers[1:]
for num in b:
    tmp = a
    g = gcd(tmp, num)
    print(str(tmp//g) + "/" + str(num//g))

