def solution(baseball):
    answer = 0
    for i in range(123, 988): # 123~987
        x,y,z = int(i/100), int((i%100)/10), i%10
        if x == 0 or y == 0 or z == 0:
            continue
        elif x==y or y==z or z==x:
            continue
        for count, bb in enumerate(baseball):
            num, s, b = bb
            x, y, z = str(x), str(y), str(z)
            num = str(num)
            # print(num)
            strike = 0
            ball = 0
            if num[0] == x:
                strike+=1
            if num[1] == y:
                strike+=1
            if num[2] == z:
                strike+=1
            if x==num[1] or x==num[2]:
                ball+=1
            if y==num[0] or y==num[2]:
                ball+=1
            if z==num[0] or z==num[1]:
                ball+=1
            # print("STRIKE " + str(strike))
            # print("BALL " + str(ball))
            # print()
            if strike != s or ball != b:
                break
            if len(baseball) - 1 == count:
                answer+=1

    return answer



################################
from itertools import permutations


def check_score(question, candidate, s, b):
    strike = 0
    for i in range(len(question)):
        if question[i] == candidate[i]:
            strike += 1
    if s != strike:
        return False
    ball = len(set(question) & set(candidate)) - strike
    if b != ball:
        return False
    return True


def solution(baseball):
    lst = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for i in baseball:
        for item in lst[:]:
            if not check_score([int(i) for i in list(str(i[0]))], item, i[1], i[2]):
                lst.remove(item)
    return len(lst)


출처: https://geonlee.tistory.com/116 [빠리의 택시 운전사]