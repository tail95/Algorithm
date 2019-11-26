#include<iostream>
#include<algorithm>
using namespace std;

int d[1000001];

int dp(int num) {
	if (num == 1) return 0;
	if (d[num] != 0) return d[num];
	int result = dp(num - 1) + 1;
	if (num % 3 == 0) result = min(dp(num / 3) + 1, result);
	if (num % 2 == 0) result = min(dp(num / 2) + 1, result);
	return d[num] = result;
}

int main() {
	int num;
	cin >> num;
	cout << dp(num);
}

