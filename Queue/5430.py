from collections import deque
import sys

T = int(sys.stdin.readline())
while(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    flag = True
    isLeft = 0
    if n == 0:
        tmp = sys.stdin.readline().rstrip()[1:-1]
        if "D" in p:
            flag=False
    else:
        tmp = deque(map(int, sys.stdin.readline().rstrip()[1:-1].split(",")))
        for op in p:
            if op == "R":
                isLeft += 1
            elif op == "D":
                if len(tmp) == 0:
                    flag=False
                    break
                if isLeft % 2 == 0:
                    tmp.popleft()
                else:
                    tmp.pop()
    if isLeft % 2 == 1:
        tmp.reverse()
    if flag:
        print("[",end="")
        print(*tmp,sep=",",end="")
        print("]")
    else:
        print("error")
    T-=1
