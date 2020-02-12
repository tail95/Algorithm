T = int(input())
for i in range(T):
    tmp = list(map(int,input().split()))
    sisters = tmp[:3]
    n = tmp[-1]
    sisters.sort()
    # print(sisters)
    diff_1 = sisters[2]-sisters[0]
    diff_2 = sisters[2]-sisters[1]
    sisters[0] += diff_1
    sisters[1] += diff_2
    n -= diff_1 + diff_2
    if n>=0 and n%3==0:
        print("YES")
    else:
        print("NO")