num = input()
count = 0
check = -1
for n in num:
    if check != int(n):
        count += 1
        check = int(n)
print(count//2)