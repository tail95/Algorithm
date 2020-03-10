import sys
N = int(sys.stdin.readline())
tp = []
for _ in range(N):
    tp.append(list(map(int ,sys.stdin.readline().split())))
dp = [0 for _ in range(N+1)]

for i in range(N):
    if i + tp[i][0] <= N:
        tmp = 0
        for j in range(i):
            tmp = max(tmp, dp[j])
        
        dp[i+tp[i][0]] = max(dp[i+tp[i][0]], max(tmp,dp[i])+tp[i][1])
print(max(dp))