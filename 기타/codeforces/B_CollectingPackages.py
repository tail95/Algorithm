import sys
T = int(sys.stdin.readline())
while T:
    n = int(sys.stdin.readline())
    packages = []
    for i in range(n):
        packages.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for pack in packages:
        pack.append(pack[0]+pack[1])
    packages.sort(key=lambda x: x[2])
    prev=[0,0]
    flag = True
    answer = ""
    for pack in packages:
        if pack[0] < prev[0] or pack[1] < prev[1]:
            flag=False
            break
        right = pack[0] - prev[0]
        up = pack[1] - prev[1]
        answer += right*"R" + up*"U"
        prev[0] = pack[0]
        prev[1] = pack[1]
        
    if flag:
        print("YES")
        print(answer)
    else:
        print("NO")
    T-=1