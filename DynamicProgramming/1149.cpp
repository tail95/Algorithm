#include<iostream>
#include<algorithm>
using namespace std;

int house[1001][3];
int dp[1001][3];

int main() {
	int N;
	cin >> N;

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < 3; ++j) {
			cin >> house[i][j];
			if (i == 0) {
				dp[i][j] = house[i][j];
			}
		}
	}
	for (int i = 1; i < N; ++i) {
		for (int j = 0; j < 3; ++j) {
			dp[i][j] = min(house[i][j] + dp[i - 1][(j + 1) % 3], house[i][j] + dp[i - 1][(j + 2) % 3]);
		}
	}
	cout << min(dp[N - 1][0], min(dp[N - 1][1], dp[N - 1][2]));
}