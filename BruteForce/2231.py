N = int(input())
for i in range(N):
    sum = i
    con = i
    while i > 0:
        sum += i % 10
        i = i // 10
    if sum == N:
        print(con)
        break
else:
    print(0)

# #include<iostream>
# using namespace std;
# int calculate(int number) {
# 	int sum = number;
# 	while (number!=0) {
# 		sum += number % 10;
# 		number = number / 10;
# 	}
# 	return sum;
# }
# int main() {
# 	int N;
# 	cin >> N;
# 	bool flag = false;
# 	for (int i = 1; i <= 1000000; i++) {
# 		if (N == calculate(i)) {
# 			cout << i;
# 			flag = true;
# 			break;
# 		}
# 	}
# 	if(!flag) cout << 0;
# 	return 0;
# }


# 
