import sys
def check(i, N, answer):
    for j in range(N):
        if maps[i][j] == 1 and not visited[j]:
            visited[j] = True
            answer += 1
            answer = check(j, N, answer)
    return answer

T = int(sys.stdin.readline())
while T:
    answer = 0
    N, M = map(int, sys.stdin.readline().split())
    maps = [[0]*N for _ in range(N)]
    visited = [False]*N
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        maps[a-1][b-1] = 1
        maps[b-1][a-1] = 1
        
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1 and not visited[i]:
                visited[i] = True
                answer = check(i, N, answer)
    print(answer)

    T -= 1