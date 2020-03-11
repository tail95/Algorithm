import sys
n = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
dp = [0 for _ in range(n)]
if n > 0:
    dp[0] = stairs[0]
if n > 1:
    dp[1] = stairs[0] + stairs[1]
if n > 2:
    dp[2] = max(stairs[0], stairs[1]) + stairs[2]
for i in range(3, n):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
print(dp[-1])



n = int(input())
stairs = [0]  # 0을 넣고 시작
for i in range(n):
    stairs.append(int(input()))
score = [0] * (n+1)
score[1] = stairs[1]
if 1 < n:
    score[2] = stairs[1]+stairs[2]   # 2번째만확인
    for i in range(3, n+1): # 3번째 (dp[2] = max(stairs[0], stairs[1]) + stairs[2])가 무의미
        score[i] = max(score[i-2] + stairs[i], stairs[i] + stairs[i-1] + score[i-3])
print(score[n])