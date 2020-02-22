import sys

def matching(c):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == c:
                match[i][j] = True
def check():
    count = 0
    for i in range(5):
        c1 = True
        c2 = True
        for j in range(5):
            if not match[i][j]:
                c1 = False
            if not match[j][i]:
                c2 = False
        if c1:
            count += 1
        if c2:
            count += 1
    for i in range(5):
        c1 = True
        c2 = True
        if not match[i][i]:
            c1 = False
        if not match[i][4-i]:
            c2 = False
    if c1:
        count += 1
    if c2:
        count += 1
    return count

bingo = []
call = []
match = [[False]*5 for _ in range(5)]

for _ in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))

for _ in range(5):
    call.append(list(map(int, sys.stdin.readline().split())))

answer = 0
flag = False
for i in range(5):
    if flag:
        break
    for j in range(5):
        cal = call[i][j]
        matching(cal)
        answer = check()
        if answer >= 3:
            
            flag = True
            for m in match:
                print(m)
            print((i)*5 + (j+1))
            break