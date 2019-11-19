# import itertools
# def make_num(numbers):
#     num_list = []
#     for i in range(1, len(numbers)+1):
#         perm = itertools.permutations(numbers, i)
#         for p in perm:
#             tmp = ""
#             for pp in p:
#                 tmp+=pp
#             num_list.append(tmp)
#     num_list = map(int, num_list)
#     return set(num_list)
#
# def isPrime(number):
#     if number < 2:
#         return False
#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 return False
#         else:
#             return True
# def solution(numbers):
#     answer = 0
#     num_set = make_num(numbers)
#     for ns in num_set:
#         if isPrime(ns):
#             answer += 1
#     return answer

#-------------------------------------

from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))    # 가능한 조합 set
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        print( set(range(i * 2, max(a) + 1, i)))
        a -= set(range(i * 2, max(a) + 1, i))        # 에라토스네스의 체를 이용한 소수
    return len(a)
