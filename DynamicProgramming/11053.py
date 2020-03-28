N = int(input())
numbers = list(map(int,input().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    tmp = 0
    for j in range(i):
        if numbers[i] > numbers[j] and tmp < dp[j]:
            tmp = dp[j]
    dp[i] = tmp + 1

print(max(dp))

