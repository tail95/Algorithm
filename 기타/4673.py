selfnumbers = [False for _ in range(1,10001)]
number = 1
while True:
    if number>10000:
        break
    tmp = number
    selfnum = number
    while tmp:
        selfnum += tmp%10
        tmp = tmp//10
    if selfnum < 10000:
        selfnumbers[selfnum] = True
    number += 1

for i, sn in enumerate(selfnumbers):
    if not sn and i != 0:
        print(i)

# 숏코딩
# r=range(9999)
# print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))

# 풀이 
# a =1234
# print(a + sum(map(int, str(a))))  # 숫자 + 각자리수 합
# {*r}-{n+sum(map(int,str(n)))for n in r} # set형 
# sorted로 정렬 후 *로 언팩킹