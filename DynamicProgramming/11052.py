import sys
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    tmp = numbers[i]
    for j in range(i):
        tmp = max(tmp, dp[i - j - 1] + numbers[j])
    dp[i] = tmp
print(dp[-1])
