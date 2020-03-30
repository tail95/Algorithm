inp = input()
flag = False
result = ""
tmp = ""
tmp2 = ""
for i in inp:
    if not flag:    
        if i == "<":
            flag = True
            result += tmp[::-1]
            tmp = "<"
            
        elif i == " ":
            if tmp:
                result += tmp[::-1] + " "
                tmp = ""
        else:
            tmp += i
    else:
        tmp += i
        if i == ">":
            flag = False
            result += tmp
            tmp = ""
        
if tmp:
    result += tmp[::-1]
print(result)