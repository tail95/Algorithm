import math
M,N = map(int, (input().split()))
prime = [True for _ in range(N+1)]
prime[1] = False
for i in range(2, int(math.sqrt(N+1)+1)):
    if prime[i]:
        for j in range(i+i, N+1, i):        # step i 를 이용해서 배수 제거 ☆
            prime[j] = False

for i in range(M, N+1):
    if prime[i]:
        print(i)
