import sys
N = int(sys.stdin.readline())
for i in range(N):
    a = list(map(int, sys.stdin.readline().split()))[1:]
    b = list(map(int, sys.stdin.readline().split()))[1:]
    aScore = [a.count(4), a.count(3), a.count(2), a.count(1)]
    bScore = [b.count(4), b.count(3), b.count(2), b.count(1)]
    flag = False
    for j in range(4):
        if not flag:
            if aScore[j] > bScore[j]:
                flag = True
                print("A")
                break
            elif aScore[j] < bScore[j]:
                flag = True
                print("B")
                break
            else:
                continue
    if not flag:
        print("D")
