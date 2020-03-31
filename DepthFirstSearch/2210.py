import sys

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def find(i, j, s):
    if len(s) == 6:
        answerSet.add(s)    
        return
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < 5 and 0 <= ny < 5:
            find(nx, ny, s+plate[nx][ny])

plate = []
answerSet = set()
for _ in range(5):
    plate.append(list(sys.stdin.readline().split()))

for i in range(5):
    for j in range(5):
        find(i, j, plate[i][j])
    
print(len(answerSet))