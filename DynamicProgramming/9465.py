import sys
import copy
T = int(sys.stdin.readline())
while T:    
    n = int(sys.stdin.readline())
    stickers = []
    for _ in range(2):
        stickers.append([0] + list(map(int, sys.stdin.readline().split())))
    dp = copy.deepcopy(stickers)
    for j in range(2, n+1):
        for i in range(2):
            tmp = (i+1) % 2
            dp[i][j] = max(dp[tmp][j-1], dp[tmp][j-2]) + stickers[i][j]
    answer = 0
    for d in dp:
        answer = max(answer, max(d))
    print(answer)
    T -= 1