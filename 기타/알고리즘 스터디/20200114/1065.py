n= int(input())
answer = 0
for i in range(1, n+1):
    if i <= 99:
        answer += 1
    elif  int(str(i)[2]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[0]):
        answer += 1
print(answer)
