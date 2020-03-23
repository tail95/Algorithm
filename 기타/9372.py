import sys
T = int(sys.stdin.readline())
while T:
    answer = 0
    N, M = map(int, sys.stdin.readline().split())
    maps = [[0]*N for _ in range(N)]
    visited = [0]*N
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        maps[a-1][b-1] = 1
        maps[b-1][a-1] = 1
        
    for i in range(N):
        for j in range(N):
            

    T -= 1