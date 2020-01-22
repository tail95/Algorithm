# # 멍청이 Version
# import sys 
# rect = []
# sub = 0
# total = 0
# for _ in range(4):
#     tmp = list(map(int, sys.stdin.readline().rstrip().split()))
#     total += (tmp[2]-tmp[0])*(tmp[3]-tmp[1])
#     points = []
#     for i in range(tmp[0], tmp[2]):
#         for j in range(tmp[1], tmp[3]):
#             points.append([i,j])
    
#     for p in points:
#         if p not in rect:
#             rect.append(p)
#         else:
#             sub += 1
# print(total - sub)

import sys
maps = [[False]*101 for _ in range(101)]
answer = 0
for _ in range(4):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(tmp[0], tmp[2]):
        for j in range(tmp[1], tmp[3]):
            maps[i][j] = True
for m in maps:
    answer += m.count(True)
print(answer)