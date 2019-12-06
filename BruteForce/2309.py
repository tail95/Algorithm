import sys
numbers = []
for i in range(9):
    numbers.append(int(sys.stdin.readline().rstrip()))
sum = sum(numbers)
check = False
for i in range(8):
    for j in range(i+1, 9):
        if sum-numbers[i]-numbers[j] == 100:
            numbers[i]=101
            numbers[j]=101
            check = True
            break
    if check:
        break
numbers.sort()
for num in numbers[:7]:
    print(num)

# #include<iostream>
# #include<algorithm>
# using namespace std;
#
# int main() {
# 	int heights[9];
# 	int heightSum = 0;
# 	for (int i = 0; i < 9; i++) {
# 		cin >> heights[i];
# 		heightSum += heights[i];
# 	}
# 	int x, y;
# 	for (int i = 0; i < 8; i++) {
# 		for (int j = i + 1; j < 9; j++) {
# 			if (heightSum - heights[i] - heights[j] == 100) {
# 				x = i; y = j;
# 				break;
# 			}
# 		}
# 	}
# 	int result[7];
# 	int count = 0;
# 	for (int i = 0; i < 9; i++) {
# 		if (i == x || i == y) continue;
# 		result[count++] = heights[i];
# 	}
# 	sort(&result[0], &result[7]);
# 	for (int i = 0; i < 7; i++) {
# 		cout << result[i] << '\n';
# 	}
# 	return 0;
# }