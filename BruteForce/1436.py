N = int(input())
count = 0
number = 0
while True:
    number += 1
    if "666" in str(number):
        count+=1
    if count == N:
        break
print(number)