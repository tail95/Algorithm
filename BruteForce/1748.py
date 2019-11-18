##### Time Over #####
# num = int(input())
# answer = 0
# for i in range(1,num+1):
#     answer += len(str(i))
# print(answer)


##### Mine #####
# num = int(input())
# answer = 0
# num_len = len(str(num))
# if num<10:
#     answer = num
# else:
#     div = 10**(num_len-1)
#     answer += (num%div+1)*num_len
#     answer += ((num//div)-1)*div*num_len
#     num_len-=1
#     while num_len > 0:
#         answer += 9*(10**(num_len-1))*num_len
#         num_len-=1
# print(answer)


##### Short & Ez #####
num = input()
num_len = len(num) - 1
c = 0
i = 0
while i < num_len:
    c += 9 * (10 ** i) * (i + 1)
    i += 1
c += ((int(num) - (10 ** num_len)) + 1) * (num_len + 1)
print(c)
