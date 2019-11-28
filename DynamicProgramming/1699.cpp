#include<iostream>
#include<algorithm>
#include<math.h>   // 백준에서 sqrt사용을 위해 (안쓰면 컴파일 에러)
using namespace std;

int dp[100001];
int main() {
	int N;
	cin >> N;
	dp[0] = 0;
	dp[1] = 1;
	int tmp_min;			// 필요없음
	for (int i = 2; i <= N; i++) {
		tmp_min = 123456789; // 필요없음
		for (int j = 1; j <= sqrt(N); j++) {
			int jj = j * j; 
			if (i - jj < 0) // 필요없음
				break;     // 필요없음
			if (tmp_min > dp[i - jj]) {
				tmp_min = dp[i - jj];
			}
		}
		dp[i] = min(dp[i - 1] + 1, tmp_min + 1);
	}
	cout << dp[N];
}


// 개선안
#include<iostream>
#include<algorithm>
using namespace std;

int dp[100001];
int main() {
	int N;
	cin >> N;
	dp[0] = 0;
	dp[1] = 1;
	for (int i = 2; i <= N; i++) {
		dp[i] = i;   // dp[i] = 1^2 i개
		for (int j = 1; j * j <= i; j++) {
			dp[i] = min(dp[i], dp[i - (j * j)] + 1);
		}
	}
	cout << dp[N];
}