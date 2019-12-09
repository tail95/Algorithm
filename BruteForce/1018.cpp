#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main() {
	int N, M, diff, tmp, answer=123456789;
	cin >> N >> M;
	string chess[51];
	char target;
	for (int i = 0; i < N; ++i) {
		cin >> chess[i];
	}

	for (int i = 0; i <= N-8; ++i) {
		for (int j = 0; j <= M - 8; ++j) {
			target = chess[i][j];
			tmp = 0;
			for (int x = i; x < i+8; ++x) {
				for (int y = j; y < j+8; ++y) {
					diff = (x - i + y - j) % 2;
					if ((diff == 0 && target != chess[x][y]) || (diff == 1 && target == chess[x][y])) {
						tmp++;
					}
				}
			}
			tmp = min(tmp, 64 - tmp);  // 반대로 시작할 경우
			if (tmp < answer) answer = tmp;
		}
	}
	cout << answer;
}

//
// 9 9      제일 첫 번째 B만 W로 변경하면 되는데 min(tmp, 64-tmp)가 없을 경우 63개를 출력
// BBWBWBWBW
// BWBWBWBWB
// WBWBWBWBW
// BWBWBWBWB
// WBWBWBWBW
// BWBWBWBWB
// WBWBWBWBW
// BWBWBWBWB
// WBWBWBWBW