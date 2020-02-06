import sys

def pow(a, b):
    b = b % 1000000007
    if b == 0: 
        return 1
    div = pow(a, b//2) % 1000000007 
    if b % 2 == 0: # 짝수일때
        return (div * div) % 1000000007
    else:  # 홀수일떄
        return (div * div * a) % 1000000007

T = int(sys.stdin.readline())
answer = 1
while T:
    N = int(sys.stdin.readline())
    if N == 1:
        print(1)
    else:
        print(pow(2, N-2))
    T -= 1


# 고속 지수 연산 알고리즘
# a의 b승에서 b가
# *짝수일 경우
# a의 b/2승 * a의 b/2승 
# *홀수일 경우
# a의 b/2승 * a의 b/2승 * abs

