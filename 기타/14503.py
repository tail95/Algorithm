import sys
# def show():
#     t = 0
#     print("*"*30)
#     for i in range(N):
#         print(area[i])
#         t += area[i].count(2)

def find(row, col, di):
    global answer
    if area[row][col] == 0:
        area[row][col] = 2
        answer += 1
    al = True
    for i in range(4):
        if area[row+to[i][0]][col+to[i][1]] == 0:
            al = False
            break
    if al:
        tmp = (di + 2) % 4
        if area[row+to[tmp][0]][col+to[tmp][1]] != 1:
            find(row+to[tmp][0], col+to[tmp][1], di)
    else:
        di = (di - 1) % 4
        # print(di)
        if 0 <= row+to[di][0] < N and 0 <= col+to[di][1] < M and area[row+to[di][0]][col+to[di][1]] == 0:
            find(row+to[di][0], col+to[di][1], di)
        else:
            find(row,col,di)    
            

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
# direction = [0,1,2,3] # 북 동 남 서
to = [[-1,0], [0,1], [1,0], [0,-1]]
area = []
for _ in range(N):
    area.append(list(map(int, sys.stdin.readline().split())))
answer = 0
find(r,c,d)
print(answer)
