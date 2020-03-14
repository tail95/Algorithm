N = int(input())
numbers = list(map(int, input().split()))
dp = [[0] for _ in range(N)]

for i in range(N):
    dp[i] = 1
    for j in range(i-1, -1, -1):
        if numbers[i] < numbers[j]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
