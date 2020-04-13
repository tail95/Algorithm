from copy import deepcopy
def dfs(target, index, arr, answerList):
    if len(arr) == len(target):
        answerList.append(target)
        return
    for k in range(len(arr[index])):
        tmp = deepcopy(target)  
        if arr[index][k] not in target:
            tmp.append(arr[index][k])
            dfs(tmp, index+1, arr, answerList) 
            
def check(ban, user):
    la = len(ban)
    lb = len(user)
    flag = True
    if la == lb:
        for i in range(la):
            if ban[i] == user[i] or ban[i] == "*":
                continue
            else:
                flag = False
    else:
        flag = False
    return flag

def solution(user_id, banned_id):
    answer = 0
    candidate = []
    for bid in banned_id:
        tmp = []
        for uid in user_id:
            if check(bid,uid):
                tmp.append(uid)
        candidate.append(tmp)

    answerList = []
    
    dfs([], 0, candidate, answerList)
    result = []
    for an in answerList:
        an.sort()
        if an not in result:
            result.append(an)
    
    return len(result)


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"] ))
# print(solution(["fradi", "frodo", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# a=[[1,2,3],[1,2,3],[4,5]]
# ret = []
# for aa in a:
#     if aa not in ret:
#         ret.append(aa)
# print(ret)