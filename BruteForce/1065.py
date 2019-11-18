num = int(input())
hansu = 0


for i in range(1, num+1):
    if i<100:
        hansu+=1
    else:
        i = str(i)
        tmp = int(i[1]) - int(i[0])
        for j in range(1, len(i)-1):
            if tmp == int(i[j+1]) - int(i[j]):
                hansu+=1
print(hansu)


#-------------------------------------------------
num = int(input())
hansu = 0

for n in range(1, num+1) :
    if n <= 99 : # 1부터 99까지는 모두 한수
        hansu += 1 
    
    else :     
        nums = list(map(int, str(n))) # 숫자를 자릿수대로 분리
        if nums[0] - nums[1] == nums[1] - nums[2] : #등차수열 확인
            hansu+=1