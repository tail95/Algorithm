import sys
T = int(sys.stdin.readline())
while T:    
    V, E = map(int, sys.stdin.readline().split())
    print(2+E-V)
    T -= 1