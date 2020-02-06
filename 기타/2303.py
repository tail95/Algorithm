from itertools import combinations
import sys
N = int(sys.stdin.readline())
answer = 0
maxNum = 0
for i in range(1, N+1):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    tmp = list(combinations(numbers, 3))
    t = list(map(lambda x: x%10 ,map(sum, tmp)))
    if max(t) >= maxNum:
        answer = i
        maxNum = max(t)
print(answer)