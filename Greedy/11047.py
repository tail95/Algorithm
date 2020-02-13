import sys
N, K = map(int, sys.stdin.readline().split())
coins = []
for i in range(N):
    coins.append(int(sys.stdin.readline()))
coins.reverse()
answer = 0
while True:
    if K == 0:
        break
    for coin in coins:
        if K >= coin:
            answer += K // coin
            K %= coin
print(answer)