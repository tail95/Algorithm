#include<iostream>
#include<algorithm>
using namespace std;

int N;
char candy[51][51];

int check() {
	int tmp, numcan = 0;
	for (int i = 0; i < N; ++i) {
		tmp = 1;
		for (int j = 1; j < N; ++j) {
			if (candy[i][j] == candy[i][j - 1]) tmp++;
			else {
				numcan = max(numcan, tmp);
				tmp = 1;
			}
		}
		numcan = max(numcan, tmp);
	}
	for (int j = 0; j < N; ++j) {
		tmp = 1;
		for (int i = 1; i < N; ++i) {
			if (candy[i][j] == candy[i - 1][j]) tmp++;
			else {
				numcan = max(numcan, tmp);
				tmp = 1;
			}
		}
		numcan = max(numcan, tmp);
	}
	return numcan;
}
int main() {
	int tmpCandy, maxCandy = 0;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		cin >> candy[i];
	}

	for (int i = 0; i < N; ++i) {
		for (int j = 0; j < N - 1; ++j) {
			swap(candy[i][j], candy[i][j + 1]);
			maxCandy = max(check(), maxCandy);
			swap(candy[i][j], candy[i][j + 1]);

			swap(candy[j][i], candy[j + 1][i]);
			maxCandy = max(check(), maxCandy);
			swap(candy[j][i], candy[j + 1][i]);
		}
	}
	cout << maxCandy;
}


// 탐색 범위 인덱스를 N으로 설정하지 않고 N-1로 설정하는 바람에 계속 틀림
// swap하는 과정이 있을 경우 범위를 정확하게 파악할 것