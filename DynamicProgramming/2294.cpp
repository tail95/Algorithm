// 나의 풀이
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

const int MAX = 100000;
int d[MAX];
int n, k;
int* coins;

int dp(int num) {
	for (int i = 0; i < n; ++i) {
		if (num == coins[i]) return 1;
	}
	if (d[num] != 0) return d[num];
	
	int result = MAX;
	for (int i = 0; i < n; ++i) {
		int tmp = num - coins[i];
		if (tmp > 0) {
			result = min(dp(tmp) + 1, result);
		}
	}
	return d[num] = result;
}

int main() {
	cin >> n >> k;
	coins = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> coins[i];
	}
	int answer = dp(k);
	if (answer == MAX) cout << -1;
	else cout << answer;
}


// 다른 사람 풀이
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

const int MAX = 100000;

int main() {
	int d[MAX] = { 0, };
	int n, k;
	int* coins;
	cin >> n >> k;
	coins = new int[n];
	for (int i = 0; i < n; ++i) {
		cin >> coins[i];
	}

	for (int i = 0; i <= k; i++) {
		d[0] = 0;
		d[i] = MAX;
	}
	for (int i = 0; i < n; i++) {
		for (int j = coins[i]; j <= k; j++) {
			d[j] = min(d[j], d[j - coins[i]] + 1);
		}
	}
	if (d[k] == MAX) cout << -1;
	else cout << d[k];
}