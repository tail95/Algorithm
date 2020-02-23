import sys
N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))
total = [0] * (N - 1)
total[0] = road[0] * city[0]
minOil = city[0]
for i in range(1, N - 1):
    if city[i] <= minOil:
        minOil = city[i]
    total[i] = total[i-1] + (minOil * road[i])
print(total[-1])