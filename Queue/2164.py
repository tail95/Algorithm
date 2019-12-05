import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
numbers = [i for i in range(1,n+1)]
numbers = deque(numbers)
while len(numbers)!=1:
    numbers.popleft()
    numbers.append(numbers.popleft())
print(numbers[0])