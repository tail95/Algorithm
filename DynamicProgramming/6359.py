import sys
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    room = [False for _ in range(1, n+1)]
    for j in range(1, n+1):
        for k in range(0, n):
            if (k+1) % j == 0:
                # print("room[k]: " + str(room[k]) + "=>" + "not room[k]: " + str(not room[k]))
                room[k] = not room[k]
    print(room.count(True))            

