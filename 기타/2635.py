def sub(a, b, li):
    c = a - b
    if c < 0:
        return
    li.append(c)
    sub(b, c, li)

n = int(input())
counter = 0
for i in range(n+1):
    tmp = [n,i]
    sub(n, i, tmp)
    if len(tmp) > counter:
        counter = len(tmp)
        max_list = tmp
print(counter)
print(*max_list)