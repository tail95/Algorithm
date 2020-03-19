import sys
dx = [-1, 0, 1, 1, 1, 0 ,-1, -1]
dy = [-1, -1, -1, 0, 1, 1, 1, 0]
while True:
    R, C = map(int, sys.stdin.readline().split())
    if R == C == 0:
        break
    maps = []
    for _ in range(R):
        maps.append(sys.stdin.readline().rstrip())
    answer = []
    for i in range(R):
        tmp = ""
        for j in range(C):
            if maps[i][j] == "*":
                tmp+="*"
            else:
                counter = 0
                for k in range(8):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < C and 0 <= ny < R:
                        if maps[ny][nx] == "*":
                            counter += 1
                tmp += str(counter)
        answer.append(tmp)
    print(*answer, sep="\n")
