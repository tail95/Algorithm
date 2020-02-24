sticks = [64,32,16,8,4,2,1]
X = int(input())
answer = 0
for stick in sticks:
    if X >= stick:
        X -= stick
        answer += 1
    if X == 0:
        break
print(answer)
