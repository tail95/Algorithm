import sys

def swap(onoff):
    if onoff == 1:
        return 0
    elif onoff == 0:
        return 1

N = int(sys.stdin.readline())
switch = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
for _ in range(M):
    sex, number = map(int,sys.stdin.readline().split())
    
    if sex == 1:
        for i in range(number, N+1, number):
            switch[i] = swap(switch[i])
    elif sex == 2:
        switch[number] = swap(switch[number])
        k = 1
        while True:
            if number - k < 1 or number + k > N:
                break
            if switch[number-k] == switch[number+k]:
                switch[number-k] = swap(switch[number-k])
                switch[number+k] = swap(switch[number+k])
                k+=1
            else:
                break
switch = switch[1:]
i = 0 
for s in switch:
    print(s, end=" ")
    i += 1
    if i % 20 == 0:
        print()