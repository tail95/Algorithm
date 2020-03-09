import sys
R, C = map(int, sys.stdin.readline().split())
maps = []
for _ in range(R):
    maps.append(list(sys.stdin.readline().rstrip()))

flag = True

dx = [0,-1,0,1]
dy = [-1,0,1,0]
answer = 0

# def show():
#     print("*"*30)
#     for m in maps:
#         print(m)
#     print("*"*30)

while flag:
    updateList = []
    for i in range(R):
        for j in range(C):
            if maps[i][j] == "*":
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and (maps[nx][ny] != "D" and maps[nx][ny] != "X" and maps[nx][ny] != "S"):
                        updateList.append([nx,ny])
    for x,y in updateList:
        maps[x][y] = "*"
    
    # show()
    updateList = []
    checker = False
    find = False
    for i in range(R):
        for j in range(C):
            if maps[i][j] == "S":
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if maps[nx][ny] == ".":
                            checker = True
                            updateList.append([nx,ny])
                        if maps[nx][ny] == "D":
                            find = True
                            break
                maps[i][j] = "X"
    
    if not checker:
        flag = False
    for x,y in updateList:
        maps[x][y] = "S"
    answer += 1
    if find:
        break
    # print("answer: " + str(answer))
    # show()
if find:
    print(answer)
else:
    print("KAKTUS")