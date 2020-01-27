N = input()
tmp = list(map(int, list(N)))
if sum(tmp) % 3 == 0 and "0" in N:
    tmp.sort(reverse=True)
    print(*tmp, sep="")
else:
    print(-1)