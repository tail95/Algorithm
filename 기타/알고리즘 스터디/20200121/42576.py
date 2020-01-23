# def solution(participant, completion):
#     checkdict= {}
#     answer = ''
    
#     for p in participant:
#         if p in checkdict.keys():
#             checkdict[p] += 1
#         else:
#             checkdict[p]=1

#     for c in completion:
#         if c in checkdict.keys():
#             checkdict[c] -= 1
#     for key, value in checkdict.items():
#         if value ==1:
#             answer = key
#             break
    
    
#     # for c in completion:
#     #     if c in participant:
#     #         participant.remove(c)
#     # answer = participant[0]
#     return answer

def solution(participant, completion):
    answer =''
    checker = {}
    for p in participant:
        if p in checker:
            checker[p] += 1
        else:
            checker[p] = 1
    for c in completion:
        checker[c] -= 1
    
    for key, value in checker.items():
        if value == 1:
            answer += key
    return answer

print(solution(["a","b","c","c"], ["a","b","c"]))




