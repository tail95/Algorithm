import sys
from itertools import permutations
N, K = map(int , sys.stdin.readline().split())
weights = list(map(int, sys.stdin.readline().split()))
weightsCombination = list(permutations(weights,N))
answer = 0
for wc in weightsCombination:
    possible = True
    base = 500
    for w in wc:
        base = base + w - K
        if base < 500:
            possible = False
            break
    if possible:
        answer += 1
print(answer)