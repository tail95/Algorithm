def findIndex(n, m, k):
    if k % m == 0:
        x = k // m - 1
        y = m -1
    else:
        x = k // m
        y = k % m - 1
        # if x == -1:
    #     x = 0
    # if y == -1:
        # y = m - 1
    return [x,y]

def dp(start, end):
    answer = 0
    dp = [[1]*M for _ in range(N)]
    for i in range(start[0], end[0]+1):
        for j in range(start[1], end[1]+1):
            if 0 < i and 0 < j:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[end[0]][end[1]]

N, M, K = map(int, input().split())
if K == 0:
    print(dp([0,0], [N-1,M-1]))
else:
    x, y = findIndex(N, M, K)
    # print([x,y])
    a = dp([0, 0], [x, y])
    # print(a)
    b = dp([x+1, y+1], [N-1, M-1])
    # print(b)
    print(a*b)
