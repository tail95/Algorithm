# expression = input()
# neg = False
# tmp = ""
# answer = 0
# for ex in expression:
#     if ex == "-":
#         if "+" in tmp:
#             if neg:
#                 answer -= sum(list(map(int, tmp.split("+"))))
#             else:
#                 answer += sum(list(map(int, tmp.split("+"))))
#         else:
#             if neg:
#                 answer -= int(tmp)
#             else:
#                 answer += int(tmp)
#         tmp = ""
#         neg = True
#     else:
#         tmp += ex
# if "+" in tmp:
#     if neg:
#         answer -= sum(list(map(int, tmp.split("+"))))
#     else:
#         answer += sum(list(map(int, tmp.split("+"))))
# else:
#     if neg:
#         answer -= int(tmp)
#     else:
#         answer += int(tmp)
# print(answer)


# 수정 ver  
# split에 반드시 그 기호를 포함할 필요 X => neg변수 필요 X
expression = input().split("-")
answer = sum(list(map(int, expression[0].split("+"))))
for ex in expression[1:]:
    answer -= sum(list(map(int, ex.split("+"))))
print(answer)