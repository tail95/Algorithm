n, m, k = map(int, input().split())
while True:
    if k==0:
        break
    tmp_n = n/2
    if tmp_n < m:
        m-=1
        k-=1
    else:
        n-=1
        k-=1
print(min(n//2, m))