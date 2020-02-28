import sys

T = int(sys.stdin.readline())
apart = [[0]*15 for _ in range(15)]
for i in range(15):
    for j in range(15):
        if i == 0:
            apart[i][j] = j + 1
        else:
            tmp = 0
            for k in range(j):
                tmp += apart[i-1][k]
            apart[i][j-1] = tmp

while T:
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(apart[k][n-1])
    T -= 1